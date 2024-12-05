import time
import json
import requests
import streamlit as st
from streamlit_cookies_controller import CookieController


cc = CookieController()
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
    _, access_token, _ = verify_and_get_auth_cookies()

    def __get(endpoint: str, payload=None):
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

    set_auth_cookies(response['user'], response['access_token'], response['refresh_token'])


@st.dialog("Logged out")
def show_log_out_dialog():
    # TODO
    st.switch_page('main.py')


def set_auth_cookies(user, access_token, refresh_token):
    cc.set('shophop-user', json.dumps(user))
    cc.set('shophop-access-token', access_token)
    cc.set('shophop-refresh-token', refresh_token)


def verify_and_get_auth_cookies(auto_logout=True):
    user = cc.get('shophop-user')
    access_token = cc.get('shophop-access-token')
    refresh_token = cc.get('shophop-refresh-token')

    if auto_logout and ((not user) or (not access_token) or (not refresh_token)):
        print('cookies:', user, access_token, refresh_token)
        remove_auth_cookies()
        st.toast('Session inactive, please log in again...')
        st.switch_page('main.py')

    return json.loads(user) if user else None, access_token, refresh_token


def remove_auth_cookies():
    for cookie in ['shophop-user', 'shophop-access-token', 'shophop-refresh-token']:
        try:
            cc.remove(cookie)
        except KeyError:
            pass
