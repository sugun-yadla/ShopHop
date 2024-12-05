from rest_framework import serializers
from .models import User, SavedItem, productData

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class SavedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavedItem
        fields = ['name', 'price']

class ProductDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = productData
        fields = ['id', 'category', 'price']