from shophop.models import User, SavedItem  


# dummy data - List of grocery items
grocery_items = [
    "Potato",
    "Bell Peppers",
    "Onion",
    "Avocado",
    "Cabbage",
    "Cauliflower"
]

# Loop through each user and create SavedItems for them
for user in User.objects.all():  # Iterate over all users in the database
    for item_name in grocery_items:  # Loop through the grocery items list
        # Create a SavedItem instance for each user and item
        saved_item = SavedItem(user=user, name=item_name, price=0.0)  # Set a default price of 0.0 or any value
        saved_item.save()  # Save the SavedItem to the database

    print(f"Saved items initialized for {user}")