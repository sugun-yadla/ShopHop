import streamlit as st
from st_utils import show_sidebar
from utils import remove_auth_cookies


@st.dialog('Logout')
def logout():
    st.write('Are you sure you want to logout?')
    if st.button('Yes'):
        remove_auth_cookies()
        st.switch_page('main.py')

show_sidebar()
logout()
