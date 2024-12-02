from rest_framework import serializers
from .models import User, SavedItem

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class SavedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavedItem
        fields = ['name', 'price']
