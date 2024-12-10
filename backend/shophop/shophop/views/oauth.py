from shophop.models import User
from django.conf import settings
from rest_framework.response import Response
from shophop.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from shophop.utils import google_get_access_token, google_get_user_info, generate_tokens_for_user
from rest_framework.decorators import api_view, renderer_classes


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def get_tokens(request):
    code = request.data['code'] if 'code' in request.data else None

    if not code:
        return Response({'error': 400})     # TODO: improve response

    redirect_uri = f'{settings.BASE_FRONTEND_URL}/google/'
    access_token = google_get_access_token(code=code, redirect_uri=redirect_uri)

    user_data = google_get_user_info(access_token=access_token)

    try:
        user = User.objects.get(email=user_data['email'])

    except User.DoesNotExist:
        username = user_data['email'].split('@')[0]
        first_name = user_data.get('given_name', '')
        last_name = user_data.get('family_name', '')

        user = User.objects.create(
            username=username,
            email=user_data['email'],
            first_name=first_name,
            last_name=last_name,
            registration_method='google'
        )

    access_token, refresh_token = generate_tokens_for_user(user)
    response_data = {
        'user': UserSerializer(user).data,
        'access_token': str(access_token),
        'refresh_token': str(refresh_token)
    }

    return Response(response_data)


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def refresh_tokens(request):
    if 'refresh_token' not in request.data:
        return Response({'info': 'refresh_token not found'}, status=400)       # TODO: improve response

    try:
        token_data = RefreshToken(request.data['refresh_token'])
    except TokenError:
        return Response({
            'message': 'invalid or expired token'
        }, status=401)


    user_id = token_data.payload['user_id']
    user = User.objects.get(id=user_id)

    response_data = {
        'user': UserSerializer(user).data,
        'access_token': str(token_data.access_token),
        'refresh_token': str(token_data)
    }

    return Response(response_data)
