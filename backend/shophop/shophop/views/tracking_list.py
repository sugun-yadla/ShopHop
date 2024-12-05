# get data from frontend and save it to saved items 
from rest_framework.decorators import authentication_classes, permission_classes, api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from shophop.models import SavedItem
from shophop.serializers import SavedItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse


@authentication_classes((JWTAuthentication,))
@permission_classes([IsAuthenticated])
@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def save_grocery_items(request):
    grocery_items = request.data.get("items", [])
    if not isinstance(grocery_items, list) or not grocery_items:
        return Response(
            {"error": "Invalid input. 'items' should be a non-empty list."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    saved_items = []
    for item in grocery_items:
        # Ensure each item has the required fields
        name = item.get("name")
        price = item.get("price")
        if not name or price is None:
            return Response(
                {"error": "Each item must have 'name' and 'price' fields."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        print("item", item)
        
    print("request details")
    print("here", request, request.user)

    return JsonResponse([], safe=False)


    #     # Create and save the SavedItem instance
    #     saved_item = SavedItem.objects.create(
    #         user=request.user, name=name, price=price
    #     )
    #     saved_items.append(saved_item)
    # print("saved_items", saved_items)

    # serializer = SavedItemSerializer(saved_items, many=True)
    # return Response(serializer.data, status=status.HTTP_201_CREATED)