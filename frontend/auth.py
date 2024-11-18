import utils
import streamlit as st

def login():
    if 'user' in st.session_state:
        return st.session_state['user']

    email = st.text_input('Email', autocomplete='email')
    password = st.text_input('Password', type='password', autocomplete='current-password')

    if st.button('Login', type='primary'):
        with st.spinner('Logging in...'):
            user = utils.login(email, password)

        if user:
            st.session_state.user = user
            st.rerun()
        else:
            st.error('Invalid email/password')

    st.stop()
