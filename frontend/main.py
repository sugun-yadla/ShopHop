import auth
import streamlit as st

st.title('ShopHop')

user = auth.login()

pages = {
    f'Welcome, {user["name"].split(" ")[0]}!': [
        st.Page('search.py', title='Search', icon=":material/search:"),
        st.Page('price_drop_tracker.py', title='Price Drop Tracker', icon=":material/notifications:"),
    ],
    'Manage your account': [
        st.Page('reset_password.py', title='Reset password', icon=':material/lock_reset:'),
        st.Page('logout.py', title='Logout', icon=':material/logout:'),
    ],
}

pg = st.navigation(pages)
pg.run()
