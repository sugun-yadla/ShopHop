import decimal
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shophop.models import productData
from shophop.serializers import ProductDataSerializer

@api_view(['GET'])
def get_products_data(request):
    products = productData.objects.all().exclude(price=decimal.Decimal('NaN'))  # Query all products from the database
    serializer = ProductDataSerializer(products, many=True)  # Serialize data
    return Response(serializer.data) 
