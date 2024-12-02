import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.title('ShopHop')

redirect_uri = 'http://localhost:8501/google/'
client_id = os.getenv('GOOGLE_OAUTH_CLIENT_ID')
sign_in_url = f'https://accounts.google.com/o/oauth2/v2/auth?scope=profile%20email&access_type=offline&include_granted_scopes=true&response_type=code&state=state_parameter_passthrough_value&redirect_uri={redirect_uri}&client_id={client_id}'

st.link_button(
    url=sign_in_url,
    label=f'Sign in with Google'
)
