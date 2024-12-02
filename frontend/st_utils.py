import streamlit as st

def show_sidebar():
    if 'user' in st.session_state:
        name = st.session_state['user']['first_name']
        st.sidebar.write(f'Welcome, {name}!')

    st.sidebar.page_link('pages/search.py', label='Search', icon=":material/search:")
    st.sidebar.page_link('pages/price_drop_tracker.py', label='Price Drop Tracker', icon=":material/notifications:")
    st.sidebar.divider()
    st.sidebar.page_link('pages/logout.py', label='Logout', icon=":material/logout:")
