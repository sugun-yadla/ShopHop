import streamlit as st
import utils

st.markdown('## Saved Items')
st.write('Add items to this list to receive an email notification when we detect a price drop!')

st.button('Add')

cart = utils.get_cart(st.session_state.user)

st.write(cart)
