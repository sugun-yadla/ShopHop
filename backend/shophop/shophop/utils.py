import requests
from typing import Dict, Any
from django.conf import settings
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from shophop.models import productData
import os

GOOGLE_ID_TOKEN_INFO_URL = 'https://www.googleapis.com/oauth2/v3/tokeninfo'
GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'


def generate_tokens_for_user(user):
    '''
    Generate access and refresh tokens for the given user
    '''
    serializer = TokenObtainPairSerializer()
    token_data = serializer.get_token(user)
    access_token = token_data.access_token
    refresh_token = token_data
    return access_token, refresh_token


def google_get_access_token(*, code: str, redirect_uri: str) -> str:
    data = {
        'code': code,
        'client_id': settings.GOOGLE_OAUTH2_CLIENT_ID,
        'client_secret': settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }

    response = requests.post(GOOGLE_ACCESS_TOKEN_OBTAIN_URL, data=data)

    if not response.ok:
        raise ValidationError('Failed to obtain access token from Google.')

    access_token = response.json()['access_token']

    return access_token


def google_get_user_info(*, access_token:  str) -> Dict[str, Any]:
    response = requests.get(
        GOOGLE_USER_INFO_URL,
        params={'access_token': access_token}
    )                   

    if not response.ok:
        raise ValidationError('Failed to obtain user info from Google.')

    return response.json()

# shophop/utils.py
def get_cheapest_from_web_scrape_data():
    if os.environ.get("RUN_MAIN") == "true":

    # print("H") 
        if not productData.objects.exists():
            grocery_items = [
            {"name": "Potato", "price": 2.50},
            {"name": "Bell Peppers", "price": 3.00},
            {"name": "Onion", "price": 1.20},
            {"name": "Avocado", "price": 1.80},
            {"name": "Cabbage", "price": 1.50},
            {"name": "Cauliflower", "price": 3.25},
            {"name": "Garlic", "price": 0.80},
            {"name": "Tomato", "price": 2.00},
            {"name": "Broccoli", "price": 2.25},
            {"name": "Spinach", "price": 2.50},
            {"name": "Brussel Sprouts", "price": 3.50},
            {"name": "Zucchini", "price": 1.80},
            {"name": "Apple", "price": 1.60},
            {"name": "Orange", "price": 1.30},
            {"name": "Banana", "price": 0.99},
            {"name": "Watermelon", "price": 4.00},
            {"name": "Cantaloupe", "price": 3.50},
            {"name": "MuskMelon", "price": 2.75},
            {"name": "Grapes", "price": 3.20},
            {"name": "Pineapple", "price": 2.90},
            {"name": "Eggs", "price": 1.90},
            {"name": "Flour", "price": 1.50},
            {"name": "Sugar", "price": 1.00},
            {"name": "Milk", "price": 1.50},
            {"name": "Vanilla Extract", "price": 5.00},
            {"name": "Butter", "price": 2.50},
            {"name": "Chocolate Chips", "price": 3.00},
            {"name": "Salt", "price": 0.50},
            {"name": "Baking Soda", "price": 0.80},
            {"name": "Baking Powder", "price": 1.20}
        ]
            for item in grocery_items:
                productData.objects.create(category=item['name'], price=item['price'])

        
