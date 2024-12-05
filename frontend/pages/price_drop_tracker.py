import utils
import st_utils
import streamlit as st

utils.get_auth_cookies()
st_utils.show_sidebar()

st.title("Price Tracker 🔔")
st.write('Receive email notifications for your favorite grocery items when we detect a price drop!')

saved_items = sorted(item['name'] for item in utils.get('/api/saved_items'))
grocery_items = sorted(utils.get('/api/products'), key=lambda x: x['category'])
prices = {item['category']: item['price'] for item in grocery_items}

def display_saved_items(saved_items):
    st.subheader("Your Saved Items")
    if saved_items:
        cols = st.columns(3)  # Adjust the number based on preference
        for i, item in enumerate(saved_items):
            with cols[i % len(cols)]:
                if st.button(label=item, icon=':material/remove_circle_outline:', use_container_width=True, ):
                    utils.delete('/api/saved_items/delete', {'items': [item]})
                    st.rerun()

    else:
        st.info("You haven't saved any items yet!")


display_saved_items(saved_items)

# Display grocery items for selection
st.subheader("Available Grocery Items")

available_items = [item['category'] for item in grocery_items if item['category'] not in saved_items]
selected_items = st.multiselect("Select items to track:", available_items)

# Button to save selected items
if st.button("Add to Saved Items"):
    if selected_items:
        payload = {'items': [{'name': item, 'price': prices[item]} for item in selected_items]}
        response = utils.post('/api/saved_items/add', payload)
        st.rerun()
    else:
        st.warning("Please select at least one item to save.")
