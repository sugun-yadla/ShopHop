import time
import json
import requests
import streamlit as st

BACKEND_URL = 'http://127.0.0.1:8000'

def login(email, password):
    # TODO
    time.sleep(1)
    if email == 'adwaitbhope@gmail.com' and password == 'abc':
        return { 'first_name': 'Adwait', 'last_name': 'Bhope', 'email': email, 'password': password }   # Return user object

    return False


def reset_password(user, old_password, new_password):
    # TODO
    time.sleep(1.5)
    if old_password != user['password']:
        return False, 'current password is incorrect'

    return True, ''


def search(user, query):
    # TODO
    time.sleep(0.5)
    return [{
            'store': 'Walmart',
            'name': 'Potatoes',
            'price': 4.99
        }, {
            'store': 'ALDI',
            'name': 'Potatoes',
            'price': 3.99
        }
    ]


def get(endpoint, payload=None):
    def __get(endpoint, payload=None):
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
