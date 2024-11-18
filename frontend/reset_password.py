import utils
import streamlit as st
from st_keyup import st_keyup

st.markdown('## Reset Password')

def confirm_password(text):
    st.write(f'Received text - {text}')

col1, col2 = st.columns(2)
with col1:
    old_password = st.text_input('Current password', type='password', autocomplete='current-password')

col1, col2 = st.columns(2)
with col1:
    new_password = st_keyup('New password', type='password')

with col2:
    confirm_new_password = st_keyup('Retype password', type='password')

pwd_empty = confirm_new_password != '' and new_password != ''
pwd_not_matched = new_password != confirm_new_password

if pwd_empty and pwd_not_matched:
    st.error('Passwords don\'t match')

if st.button('Reset', type='primary', disabled=pwd_not_matched):
    with st.spinner('Chaning your password...'):
        success, message = utils.reset_password(st.session_state.user, old_password, new_password)
        if success:
            st.success('Your password was successfully changed!')
        else:
            st.error(f'Could not change password - {message}')
