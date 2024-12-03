import time
import json
import requests
import streamlit as st
from utils import BACKEND_URL
from st_utils import show_sidebar
from streamlit.components.v1 import html

st.title('ShopHop')

show_sidebar()

with st.spinner('Signing in...'):
    code = st.query_params['code']

    response = requests.get(f'{BACKEND_URL}/api/token', data={'code': code})
    response = json.loads(response.content.decode('utf-8'))


if 'user' in response:
    st.session_state['user'] = response['user']
    st.session_state['access_token'] = response['access_token']
    st.session_state['refresh_token'] = response['refresh_token']
    st.switch_page('pages/search.py')

else:
    st.write('Something went wrong.')
