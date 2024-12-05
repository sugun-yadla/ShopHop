import utils
import streamlit as st


def show_sidebar():
    user, _, _ = utils.get_auth_cookies()
    st.sidebar.write(f'Welcome, {user["first_name"]}!')

    st.sidebar.page_link('pages/search.py', label='Search', icon=":material/search:")
    st.sidebar.page_link('pages/price_drop_tracker.py', label='Price Drop Tracker', icon=":material/notifications:")
    st.sidebar.divider()
    st.sidebar.page_link('pages/logout.py', label='Logout', icon=":material/logout:")
