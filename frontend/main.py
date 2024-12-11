import os
import utils
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title('ShopHop')
st.subheader('Find the best grocery deals in one place!')

user, _, _ = utils.get_auth_cookies(auto_logout=False, validate_token=True)
if user:
    st.switch_page('pages/search.py')

redirect_uri = 'http://localhost:8501/google/'
client_id = os.getenv('GOOGLE_OAUTH_CLIENT_ID')
sign_in_url = f'https://accounts.google.com/o/oauth2/v2/auth?scope=profile%20email&access_type=offline&include_granted_scopes=true&response_type=code&state=state_parameter_passthrough_value&redirect_uri={redirect_uri}&client_id={client_id}'

st.markdown(
    """
    <style>
    .main-title {
        font-size: 3em;
        color: #2c3e50;
        font-weight: bold;
        text-align: center;
        margin-top: -50px;
    }
    .subtitle {
        font-size: 1.5em;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 30px;
    }
    .search-bar {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .button-container {
        display: flex;
        justify-content: center;
    }
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    img {
        max-width: 150px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Logo (Assume logo is saved in the same directory as "shophop_logo.png")
st.image('shophop-white.png', use_container_width=True)
# st.markdown('<div class="logo-container"><img src="shophop.png" alt="ShopHop Logo"></div>', unsafe_allow_html=True)

# App name and subtitle
# st.markdown('<div class="main-title">ShopHop</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Find the best grocery deals in one place!</div>', unsafe_allow_html=True)

# Sign-In Button
st.markdown('<div class="button-container">', unsafe_allow_html=True)
st.link_button(
    url=sign_in_url,
    label=f'Sign in with Google',
    use_container_width=True,
    icon=':material/account_circle:'
)
st.markdown('</div>', unsafe_allow_html=True)

