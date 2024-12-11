from django.http import JsonResponse
from rest_framework.decorators import api_view
from shophop.models import User, SavedItem, productData  
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



grocery_items = [
    "Potato", "Bell Peppers", "Onion", "Avocado", "Cabbage", "Cauliflower", 
    "Garlic", "Tomato", "Broccoli", "Spinach", "Brussel Sprouts", "Zucchini", 
    "Apple", "Orange", "Banana", "Watermelon", "Cantaloupe", "MuskMelon", 
    "Grapes", "Pineapple", "Eggs", "Flour", "Sugar", "Milk", "Vanilla Extract", 
    "Butter", "Chocolate Chips", "Salt", "Baking Soda", "Baking Powder"
]

grocery_items = ["Apple"]


def get_cheapest_from_web_scrape_data(items):

    #  fetch cheapest sfor all the grocery items
    
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
                    "store": cheapest_product["store"]
                }

        # Update to cheapest db 
        for category, details in cheapest_prices.items():
            try:
                # Check if the category exists in the database
                product = productData.objects.get(category=category)
                product.price = details["Current_Price"]
                product.save()
                print(f"Updated {category} with new price: ${details['Current_Price']}")
                      
            except productData.DoesNotExist:
                # If the product does not exist, create a new entry
                new_product = productData.objects.create( category=category, price=details["Current_Price"])
                print(f"Added new product: {category} with price: ${details['Current_Price']}")

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

def update_saved_items_db(mailing_list):
    for email, items in mailing_list.items():
        try:
        # Get the user object for the given email
            user = User.objects.get(email=email)
            for item in items:
                duplicates = SavedItem.objects.filter(user=user, name=item["name"])
                print(duplicates)
                if duplicates.exists():
                # If duplicates exist, keep the first one and delete the rest
                    first_item = duplicates.first()
                    duplicates.exclude(id=first_item.id).delete()
                    
                    # Update the remaining record
                    first_item.price = item["new_price"]
                    first_item.save()
                    print(f"Updated duplicate item: {first_item.name}, Price: {first_item.price} for user: {user.email}")
                else:
                # If no duplicates exist, create a new entry
                    new_item = SavedItem.objects.create(
                        user=user,
                        name=item["name"],
                        price=item["new_price"]
                    )
                    print(f"Created new item: {new_item.name}, Price: {new_item.price} for user: {user.email}")

        except User.DoesNotExist:
            print(f"User with email {email} does not exist.")
            

def get_mailing_list():
    try:
        cheapest_prices = get_cheapest_from_web_scrape_data(grocery_items)
        for item, details in cheapest_prices.items():
            print(f"Cheapest {item}: {details}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cheapest data: {e}")
        return {} 


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
                    "store": cheapest_item["store"],
                    "product": cheapest_item["Product"]
                })
    # from mailing list users, get the user object. then 
    # update to saved items 
    update_saved_items_db(mailing_list)
                
    return mailing_list


def send_email(mail_to_user, subject, body):
    try:
        smtp_server = "smtp.gmail.com"  # Replace with the correct server
        smtp_port = 587 
    
        with smtplib.SMTP(smtp_server, smtp_port) as smtp: 
            smtp.set_debuglevel(1)
            smtp.starttls()
            smtp.login(SENDER_EMAIL_ID, SENDER_EMAIL_PASSWORD)#must initialize the mail_user(usename) and mail_pass(account password) assuming we would get this from login account details, same with the mail_to(email)
            smtp.sendmail(SENDER_EMAIL_ID, mail_to_user, f'Subject: {subject}\n\n{body}')  # Initialise mail_user and mail_pass and figure out subject 
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
    mailing_list = get_mailing_list()
    print("mailing_list",mailing_list)
    notify_users(mailing_list)

    return JsonResponse(mailing_list, safe=False)
        