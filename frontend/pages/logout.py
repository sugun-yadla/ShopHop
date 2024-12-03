import streamlit as st
from st_utils import show_sidebar

@st.dialog('Logout')
def logout():
    st.write('Are you sure you want to logout?')
    if st.button('Yes'):
        if 'user' in st.session_state:
            del st.session_state['user']
            del st.session_state['access_token']
            del st.session_state['refresh_token']

        st.switch_page('main.py')

show_sidebar()
logout()
