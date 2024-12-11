import os
import sys
from dotenv import load_dotenv
from unittest.mock import MagicMock

mocked_st = MagicMock()
sys.modules['streamlit'] = mocked_st
sys.modules['streamlit_cookies_controller'] = MagicMock()

from frontend import utils
load_dotenv()


# Add a mock function that fetches access tokens from .env file instead of Google sign-in
def mock_get_auth_cookies(auto_logout=True, validate_token=False, retries=1):
    first_name, last_name, email = os.environ.get('SHOPHOP_USER').split(';')
    user = { 'first_name': first_name, 'last_name': last_name, 'email': email }
    access_token = os.environ.get('SHOPHOP_ACCESS_TOKEN')
    refresh_token = os.environ.get('SHOPHOP_REFRESH_TOKEN')

    return user, access_token, refresh_token


# Assign the mocked function to the module
utils.get_auth_cookies = mock_get_auth_cookies


# Test to fetch a new access token based on the refresh token that is still valid
def test_get_new_access_token():
    _, current_access_token, _ = mock_get_auth_cookies()
    new_access_token = utils.get_new_access_token(auto_logout=False)

    assert current_access_token != new_access_token


# Tests auto-logout if refresh token is invalid (has expired)
def test_auto_logout():
    # Set invalid refresh token
    os.environ['SHOPHOP_REFRESH_TOKEN'] = 'abc123pqr'

    _, new_access_token, _ = utils.get_new_access_token(auto_logout=True)
    assert new_access_token is None


# Tests invoking the product comparison API
def test_product_comparison():
    load_dotenv(override=True)

    products, categorized_products = utils.search('milk')
    assert len(products) > 0
    assert len(categorized_products) > 0

    item = products[0]
    assert item['store'] in ('Walmart', 'Target', 'Aldi')
    assert item['Price'] > 0
    assert item['Standardized_Quantity'] is not None
    assert item['st_unit'] is not None
    assert item['st_val'] is not None
    assert item['price_currency'] is not None
    assert item['price_per_unit'] is not None
    assert item['Image'] is not None
    assert item['URL'] is not None

    assert products[0]['price_per_unit'] <= products[1]['price_per_unit']


def test_get_saved_items():
    load_dotenv(override=True)

    saved = sorted(item['name'] for item in utils.get('/api/saved_items'))
    assert len(saved) > 0


def test_add_to_saved_item():
    load_dotenv(override=True)

    # Check currently saved items first
    saved = sorted(item['name'] for item in utils.get('/api/saved_items'))
    assert 'Broccoli' not in saved

    # Add Broccoli to it
    payload = {'items': [{'name': 'Broccoli', 'price': 5.00}]}
    response = utils.post('/api/saved_items/add', payload)

    # Verify Broccoli was saved
    saved_updated = sorted(item['name'] for item in utils.get('/api/saved_items'))
    assert 'Broccoli' in saved_updated


def test_delete_from_saved_item():
    load_dotenv(override=True)

    # Check currently saved items first
    saved = sorted(item['name'] for item in utils.get('/api/saved_items'))
    assert 'Apple' in saved

    # Remove Apple from it
    utils.delete('/api/saved_items/delete', {'items': ['Apple']})

    # Verify Broccoli was saved
    saved_updated = sorted(item['name'] for item in utils.get('/api/saved_items'))
    assert 'Apple' not in saved_updated
