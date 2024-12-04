import time
import json
import requests
import streamlit as st

BACKEND_URL = 'http://127.0.0.1:8000'


def search(query):
    products = get(f'/api/products/{query}')

    def prettify(item: dict):
        item = item.copy()
        item['Price'] = f'$ {item["Price"]:.2f}'
        if 'store' in item:
            item['Store'] = item['store']
            del item['store']
        del item['Image']
        del item['URL']
        item['st_quant'] = item['Standardized_Quantity']
        del item['Standardized_Quantity']
        return item

    prettified_products = [prettify(item) for item in products]
    return products, prettified_products


def get(endpoint: str, payload=None):

    def __get(endpoint: str, payload=None):
        access_token = st.session_state.get('access_token', None)
        if not access_token:
            st.switch_page('main.py')

        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.get(BACKEND_URL + endpoint, data=payload, headers=headers)
        return response

    response = __get(endpoint, payload)

    if response.status_code == 401:
        refresh_token()
        response = __get(endpoint, payload)

    return json.loads(response.content.decode('utf-8'))


def refresh_token():
    payload = {
        'refresh_token': st.session_state['refresh_token']
    }
    response = requests.get(BACKEND_URL + '/api/token/refresh', data=payload)
    response = json.loads(response.content.decode('utf-8'))

    st.session_state['user'] = response['user']
    st.session_state['access_token'] = response['access_token']
    st.session_state['refresh_token'] = response['refresh_token']
