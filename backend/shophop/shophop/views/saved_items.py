from rest_framework import status
from shophop.models import SavedItem
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from shophop.serializers import SavedItemSerializer
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


@authentication_classes((JWTAuthentication,))
@permission_classes([IsAuthenticated])
@api_view(('DELETE',))
@renderer_classes((JSONRenderer,))
def delete_saved_items(request):
    item_names = request.data.get('items', [])
    items = SavedItem.objects.get(user=request.user.id, name__in=item_names)
    items.delete()
    return Response({
            "message": "Deleted successfully"
        }, status=status.HTTP_200_OK
    )
