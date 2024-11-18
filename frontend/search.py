import streamlit as st
import utils

st.markdown('## Find the best deals!')

def search_product(query):
    st.write(f'Searching for {query}...')
    products = utils.search(st.session_state.user, query)
    st.write(products)

col1, col2 = st.columns([0.8, 0.2], vertical_alignment='bottom')

with col1:
    search_query = st.text_input('Product', label_visibility='hidden', placeholder='Look for an item', autocomplete='product-name')

with col2:
    search_button = st.button('Search')

if search_query:
    search_product(search_query)
