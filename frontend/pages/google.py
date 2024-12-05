import json
import requests
import streamlit as st
import utils

st.title('ShopHop')

with st.spinner('Signing in...'):
    code = st.query_params['code']

    response = requests.get(f'{utils.BACKEND_URL}/api/token', data={'code': code})
    response = json.loads(response.content.decode('utf-8'))


if 'user' in response:
    utils.set_auth_cookies(response['user'], response['access_token'], response['refresh_token'])
    st.switch_page('pages/search.py')

else:
    st.write('Something went wrong.')
