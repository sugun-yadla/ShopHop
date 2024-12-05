import utils
import st_utils
import streamlit as st

utils.get_auth_cookies()
st_utils.show_sidebar()

st.markdown('## Saved Items')
st.write('Add items to this list to receive an email notification when we detect a price drop!')

if st.button('Add'):
    pass

saved_items = utils.get('/api/saved_items')

st.table(saved_items)
