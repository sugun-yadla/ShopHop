import streamlit as st
from streamlit.components.v1 import html

@st.dialog('Logout')
def logout():
    st.write('Are you sure you want to logout?')
    if st.button('Yes'):
        del st.session_state['user']
        html('<script>parent.window.location.reload()</script>')

logout()
