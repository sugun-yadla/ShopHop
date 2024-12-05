import math
import utils
import st_utils
import streamlit as st

print('Opening search.py')

utils.get_auth_cookies()
st_utils.show_sidebar()

st.title('Find the best deals! 🔍')

def show_results(products, pretty_products):
    st.markdown('#')
    ITEMS_PER_ROW = 3

    for row in range(math.ceil(len(products) / ITEMS_PER_ROW - 1)):
        for col_id, col in enumerate(st.columns(ITEMS_PER_ROW)):
            i = ITEMS_PER_ROW * row + col_id
            if i >= len(products):
                break

            product = products[i]
            product["URL"] = product["URL"].split('?')[0]
            print(product)

            col.image(product['Image'], use_container_width=True)

            css_style = '''<style>
            a, a:visited {
                text-decoration: none;
                color: inherit;
            }
            a:hover {
                color: brown;
            }
            </style>
            '''

            c1, c2 = col.columns([0.8, 0.2])

            c1.html(css_style + f'''
                <a href="{product["URL"]}">
                    <div>
                        {product["Product"]}<br>
                        {product["Quantity"]}<br>
                        $ {product["Price"]:.2f}
                    </div>
                </a>
            ''')

            c2.image(utils.STORE_LOGO_URLS[product['Store']])
            col.write('Effective price: ' + product['price_per_unit_pretty'])

        if row == math.floor(len(products) / ITEMS_PER_ROW - 1):
            break

        st.divider()

    st.table(pretty_products)

col1, col2 = st.columns([0.8, 0.2], vertical_alignment='bottom')

with col1:
    search_query = st.text_input('Product', label_visibility='hidden', placeholder='Look for an item', autocomplete='product-name')

with col2:
    search_button = st.button('Search')

if search_query:
    with st.spinner(f'Searching for {search_query}...'):
        products, prettified_products = utils.search(search_query)

    show_results(products, prettified_products)
