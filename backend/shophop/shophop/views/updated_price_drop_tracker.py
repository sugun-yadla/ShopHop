from django.http import JsonResponse
from rest_framework.decorators import api_view
from shophop.models import User, SavedItem  
from shophop.views.price_comparison import fetch_products
from shophop.models import User
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()

SENDER_EMAIL_ID = os.getenv('SENDER_EMAIL_ID')
SENDER_EMAIL_PASSWORD = os.getenv('SENDER_EMAIL_PASSWORD')

# users_selected_items=[]
# # user will choose the grocery_items from frontend 

# # Loop through each user and create SavedItems for them
# for user in User.objects.all():  # Iterate over all users in the database
#     for item_name in users_selected_items:  # Loop through the grocery items list
#         # Create a SavedItem instance for each user and item
#         saved_item = SavedItem(user=user, name=item_name, price=0.0)  # Set a default price of 0.0 or any value
#         saved_item.save()  # Save the SavedItem to the database

#     print(f"Saved items initialized for {user}")


# - user specific list of items(fetch from user db) - do backend code for this 
# - store cheapest to db (before itself) - done 
# - run web scraping to fetch data again 
# - compare the two 
# - send email 
# - run cron job daily  

# grocery_items = [
#     "Potato", "Bell Peppers", "Onion", "Avocado", "Cabbage", "Cauliflower", 
#     "Garlic", "Tomato", "Broccoli", "Spinach", "Brussel Sprouts", "Zucchini", 
#     "Apple", "Orange", "Banana", "Watermelon", "Cantaloupe", "MuskMelon", 
#     "Grapes", "Pineapple", "Eggs", "Flour", "Sugar", "Milk", "Vanilla Extract", 
#     "Butter", "Chocolate Chips", "Salt", "Baking Soda", "Baking Powder"
# ]
grocery_items = [
    "Onion", "Garlic", "Eggs", "Tomato", "Broccoli","Potato", "Apple", "Banana", "Orange"
]

def get_cheapest_from_web_scrape_data(items):

    #  fetch cheapest for all the grocery items
    
    # change this endpoint later
    base_url = "http://127.0.0.1:8000/api/products/"
    items_query = ",".join(items)
    url = f"{base_url}{items_query}"
    print("url", url)
    try:
        
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        scraped_data = response.json()
        
        # Create a dictionary for the cheapest price per item
        cheapest_prices = {}
        for item in items:
            item_data = [d for d in scraped_data if d["Category"].lower() == item.lower()]
            if item_data:
                # Find the product with the lowest price
                cheapest_product = min(item_data, key=lambda x: x["Price"])
                cheapest_prices[item] = {
                    "Product": cheapest_product["Product"],
                    "Current_Price": cheapest_product["Price"],
                    "Store": cheapest_product["store"]
                }
        # saved to cheapest db 
        
        return cheapest_prices

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {} 

def get_users_saved_data():
    saved_items_data = SavedItem.objects.all()
    user_saved_items_info = []
    for item in saved_items_data:
        user_saved_items_info.append({
            "user": item.user.email,  # Use the user's email
            "name": item.name,  # Add the grocery item name
            "price": item.price,  # Add the price of the grocery item
        })

    return user_saved_items_info

def get_mailing_list():


    try:
        cheapest_prices = get_cheapest_from_web_scrape_data(grocery_items)
        for item, details in cheapest_prices.items():
            print(f"Cheapest {item}: {details}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cheapest data: {e}")
        return {} 

    # user_saved_items_info = [
    # {"id": 1, "user": "vdaber@umass.edu", "name": "Eggs", "price": 150.99},
    # {"id": 2, "user": "vdaber@umass.edu", "name": "Onion", "price": 19.99},
    # {"id": 3, "user": "vaishu.daber@gmail.com", "name": "Tomato", "price": 12.50}
    # ] 
    user_saved_items_info = get_users_saved_data()
    print("Saved Items in User DB",user_saved_items_info)
    # creating a mailing list 
    mailing_list = {}
    
    for item in user_saved_items_info:
        
        user = item["user"]
        item_name = item["name"]
        saved_price = item["price"]
        

        if item_name in cheapest_prices:
            cheapest_item = cheapest_prices[item_name]
            cheapest_price = cheapest_item["Current_Price"]

            if cheapest_price < saved_price:
                if user not in mailing_list:
                    mailing_list[user] = []

                mailing_list[user].append({
                    "name": item_name,
                    "old_price": saved_price,
                    "new_price": cheapest_price,
                    "store": cheapest_item["Store"],
                    "product": cheapest_item["Product"]
                })
                # update to saved items 

    return mailing_list

    # fetch items and their price from the user db  
    # Adding the cheapest price to the saved item using scraping


    # do it for all users 

    # for user in User.objects.all():
    #     # fetch users from saved_items 

    #     for item_name in user_saved_items_info:
    #         # check item and price, and check from the made up dictionary 

def send_email(mail_to_user, subject, body):
    try:
        smtp_server = "smtp.gmail.com"  # Replace with the correct server
        smtp_port = 587 
    
        with smtplib.SMTP(smtp_server, smtp_port) as smtp: 
            smtp.set_debuglevel(1)
            smtp.starttls()
            smtp.login(SENDER_EMAIL_ID, SENDER_EMAIL_PASSWORD)#must initialize the mail_user(usename) and mail_pass(account password) assuming we would get this from login account details, same with the mail_to(email)
            smtp.sendmail(SENDER_EMAIL_ID, mail_to_user, body)  # Initialise mail_user and mail_pass and figure out subject 
            print(f"Email sent successfully to {mail_to_user}")
    except Exception as e:
        print(f"Failed to send email to {mail_to_user}: {e}")

def notify_users(mailing_list):
        for user, items in mailing_list.items():

            subject = "Price Drop Alert!"
            body = f"Hello {user},\n\nWe have some great news! The prices for the following items you saved have dropped:\n\n"
            
            for item in items:
                body += f"Item: {item['name']}\n"
                body += f"Old Price: ${item['old_price']}\n"
                body += f"New Price: ${item['new_price']} at {item['store']}\n"
                body += f"Product: {item['product']}\n\n"
            
            body += "Hurry up and grab the deal before it's gone!\n\nBest regards,\nYour Shopping Helper"
            
            # Send the email to the user
            send_email(user, subject, body)

        
@api_view(('GET',))
def price_drop_tracker(request):
    
    # print("SENDER_EMAIL_ID", SENDER_EMAIL_ID)
    # print("SENDER_EMAIL_PASSWORD", SENDER_EMAIL_PASSWORD)

    mailing_list = get_mailing_list()
    print("mailing_list",mailing_list)
    # notify_users(mailing_list)

    return JsonResponse(mailing_list, safe=False)
        