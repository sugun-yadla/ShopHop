import utils
import streamlit as st


def show_sidebar():
    user, _, _ = utils.get_auth_cookies()
    st.sidebar.write(f'Welcome, {user["first_name"]}!')

    st.sidebar.page_link('pages/search.py', label='Search', icon=":material/search:")
    st.sidebar.page_link('pages/price_drop_tracker.py', label='Price Tracker', icon=":material/notifications:")
    st.sidebar.page_link('pages/recipe_recommender.py', label='What\'s for dinner?', icon=":material/restaurant:")
    st.sidebar.divider()
    st.sidebar.page_link('pages/logout.py', label='Logout', icon=":material/logout:")
