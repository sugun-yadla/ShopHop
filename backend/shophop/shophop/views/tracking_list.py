# get data from frontend and save it to saved items 
from rest_framework.decorators import authentication_classes, permission_classes, api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from shophop.models import SavedItem, User
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
    # user_id = request.user.id                             #change this later 
    user_id = 2
    try:
        # Retrieve the specific user
        current_user = User.objects.get(id=user_id)        

    except User.DoesNotExist:
        return Response(
            {"error": f"User with ID {user_id} does not exist."},
            status=status.HTTP_404_NOT_FOUND,
        )

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
       
        existing_item = SavedItem.objects.filter(user=current_user, name=name).first()
        if existing_item:
            # If the item exists, update the price
            existing_item.price = price
            existing_item.save()  # Save the updated item
            saved_items.append(existing_item)
        else:
            
            saved_item = SavedItem.objects.create(user=current_user, name=name, price=price)
            saved_items.append(saved_item)

    serializer = SavedItemSerializer(saved_items, many=True)
    
    return Response(
        {"message": "Grocery items saved successfully.", "items":  serializer.data},
        status=status.HTTP_201_CREATED,
    )

 