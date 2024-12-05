import time
import json
import requests
import streamlit as st
from streamlit_cookies_controller import CookieController


cc = CookieController()
BACKEND_URL = 'http://127.0.0.1:8000'

STORE_LOGO_URLS = {
    'Aldi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/AldiWorldwideLogo.svg/400px-AldiWorldwideLogo.svg.png',
    'Walmart': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Walmart_Spark.svg/451px-Walmart_Spark.svg.png'
}

def search(query):
    products = get(f'/api/products/{query}')

    def transform(item: dict):
        item = item.copy()
        if 'store' in item:
            item['Store'] = item['store']
            del item['store']
        # del item['Image']
        # del item['URL']

        if item['Standardized_Quantity']:
            item['st_val'] = float(item['Standardized_Quantity'].split(' ')[0])
            item['st_unit'] = item['Standardized_Quantity'].split(' ')[1]

            price_per_unit = item['Price'] / item['st_val']
            if price_per_unit < 0.1:
                price_per_unit = f"¢ {(price_per_unit * 100):.2f}"
            elif price_per_unit < 1:
                price_per_unit = f"¢ {round(price_per_unit * 100)}"
            else:
                price_per_unit = f"$ {price_per_unit:.2f}"

            item['price_per_unit'] = item['Price'] / item['st_val']
            item['price_per_unit_pretty'] = f"{price_per_unit} per {item['st_unit']}"

        # item['Price'] = f'$ {item["Price"]:.2f}'
        # del item['Standardized_Quantity']
        return item

    products = [transform(item) for item in products]
    products.sort(key=lambda x: x['price_per_unit'])
    return products, products


def get(endpoint: str, payload=None):
    print(f'Executing GET on {endpoint}')
    _, access_token, refresh_token = get_auth_cookies()

    def __get(endpoint: str, access_token, payload=None):
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.get(BACKEND_URL + endpoint, data=payload, headers=headers)
        return response

    response = __get(endpoint, access_token, payload)

    if response.status_code == 401:
        print('GET failed, access_token not valid, getting new access_token')
        _, access_token, _  = get_new_access_token()
        response = __get(endpoint, access_token, payload)

    return json.loads(response.content.decode('utf-8'))


def get_new_access_token(auto_logout=True):
    print(f'Fetching new access_token with auto_logout={auto_logout}')
    _, _, refresh_token = get_auth_cookies(auto_logout=auto_logout, validate_token=False)
    response = requests.get(BACKEND_URL + '/api/token/refresh', data={ 'refresh_token': refresh_token })

    if response.status_code == 401 and auto_logout:
        print('Auto logging out, refresh_token not valid')
        remove_auth_cookies()
        st.switch_page('main.py')

    print('Retrieved new access_token')
    response = json.loads(response.content.decode('utf-8'))
    return set_auth_cookies(response['user'], response['access_token'], response['refresh_token'])


@st.dialog("Logged out")
def show_log_out_dialog():
    # TODO
    st.switch_page('main.py')


def set_auth_cookies(user, access_token, refresh_token):
    print('Setting cookies')
    cc.set('shophop-user', json.dumps(user))
    cc.set('shophop-access-token', access_token)
    cc.set('shophop-refresh-token', refresh_token)
    print(cc.getAll())
    return user, access_token, refresh_token


def get_auth_cookies(auto_logout=True, validate_token=False, retries=1):
    # time.sleep(1)
    user = cc.get('shophop-user')
    user = json.loads(user) if user else None
    access_token = cc.get('shophop-access-token')
    refresh_token = cc.get('shophop-refresh-token')

    if retries < 3 and ((not user) or (not access_token) or (not refresh_token)):
        print(f'Did not find cookies on retry #{retries}')
        return get_auth_cookies(auto_logout=auto_logout, validate_token=validate_token, retries=retries + 1)

    if auto_logout and ((not user) or (not access_token) or (not refresh_token)):
        print(f'Did not find cookies on retry #{retries}')
        print('Auth Cookie not set:', user, access_token, refresh_token)
        print('Auto logging out')
        remove_auth_cookies()
        st.toast('Session inactive, please log in again...')
        st.switch_page('main.py')

    print(f'Retry #{retries}. validate_token={validate_token}, refresh_token={refresh_token}')

    if refresh_token and validate_token:
        print('Validating token')
        user, access_token, refresh_token = get_new_access_token(auto_logout=auto_logout)

    return user, access_token, refresh_token


def remove_auth_cookies():
    print('Removing cookies (why?)')
    for cookie in ['shophop-user', 'shophop-access-token', 'shophop-refresh-token']:
        try:
            cc.remove(cookie)
        except KeyError:
            print(f'Tried deleting {cookie} but it wasn\'t there!')
