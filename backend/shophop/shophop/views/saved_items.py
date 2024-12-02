from shophop.models import SavedItem
from shophop.serializers import SavedItemSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, renderer_classes, authentication_classes, permission_classes


@authentication_classes((JWTAuthentication,))
@permission_classes([IsAuthenticated])
@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def get_saved_items(request):
    saved_items = SavedItem.objects.filter(user=request.user.id)
    serializer = SavedItemSerializer(saved_items, many=True)
    return Response(serializer.data)
