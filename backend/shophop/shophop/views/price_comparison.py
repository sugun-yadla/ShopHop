from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from rest_framework.decorators import api_view
from shophop.models import Product
from shophop.views.target_data import get_target_data
import json
from datetime import datetime


def standardize_quantity(row):
    try:
        quantity = row['Quantity']
        
        if pd.isna(quantity):
            return None  
        
        quantity = quantity.lower()
        quantity = quantity.replace("ounce", "oz")
        match = re.search(r'([\d.]+)\s*(fl oz|gallon|gal|oz|carton|ct|dozen|count|lb|pk|pack)', quantity)
        
        if match:
            value, unit = match.groups()
            value = float(value)
            
            if "gallon" in unit or "gal" in unit:
                return f"{value * 128:.2f} oz"
            elif "fl oz" in unit or "oz" in unit:
                return f"{value:.2f} oz"
            elif "carton" in unit or "ct" in unit or "dozen" in unit or "count" in unit or "pk" in unit or "pack" in unit:
                return f"{value:.2f} ct"
            elif "lb" in unit:
                return f"{value * 16:.2f} oz"
        
        return None
    except Exception as e:
        print(f"Error in standardize_quantity: {e}")
        return None


def fetch_aldi_products(product):
    try:
        details = []
        url = f'https://new.aldi.us/results?q={product}'
        headers = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            # print(f"Failed to fetch Aldi products: {response.status_code}")
            return response.status_code

        page_soup = BeautifulSoup(response.content, 'html.parser')
        elements = page_soup.find('div', class_="product-grid")
        
        if elements:
            count = 0
            for product_tile in elements.find_all("div", class_="product-tile"):
                if count >= 10:
                    break
                
                title = product_tile.find("div", class_="product-tile__name")                    
                price = product_tile.find("div", class_="base-price base-price--product-tile product-tile__price")
                size = product_tile.find("div", class_="product-tile__unit-of-measurement")

                if title:
                    title = title.text.strip()
                else:
                    title = None
                if price:
                    price = price.text.strip() 
                else:
                    price = None
                if size:
                    size = size.text.strip()
                else:
                    size = None

                details.append({
                        "Product": title,
                        "Price": price,
                        "Quantity": size
                })
                count += 1  
        return details
    except Exception as e:
        print(f"Error in fetch_aldi_products: {e}")
        return []


def fetch_walmart_products(product):
    try:
        details = []
        url = f'https://www.walmart.com/search?q={product}'
        headers = {
            "Referer": "https://www.google.com",
            "Connection": "Keep-Alive",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch Walmart products: {response.status_code}")
            return response.status_code

        walmart_soup = BeautifulSoup(response.content, 'html.parser')
        spans = walmart_soup.find_all('span', {'class': 'w_iUH7'})

        current_name = None
        for span in spans:
            text = span.text.strip()
            if text.startswith("current price"):
                if current_name:
                    details.append({'Product': current_name, 'Price': text, 'Category': f'{product}'})
                current_name = None
            else:
                current_name = text

        return details
    except Exception as e:
        print(f"Error in fetch_walmart_products: {e}")
        return []

def fetch_target_products(product):
    try:
        details =  get_target_data(product)
        return details
    except Exception as e:
        print(f"Error in fetch_target_products: {e}")
        return []


@api_view(('GET',))
def fetch_products(request, product):
    try:
        dairy_products = [product.strip() for product in product.split(',')] 
        database = []
        walmart_data = []
        target_data = []
        aldi_data = []

        for product in dairy_products:

            aldi_details = fetch_aldi_products(product)
            if aldi_details:
                try:
                    for entry in aldi_details:
                        name = entry["Product"]
                        price_str = entry["Price"].replace('$', '')

                        if '/' in price_str:
                            price_str = price_str.split('/')[0]

                        aldi_data.append({
                            "Product": name,
                            "Price": price_str,
                            "Quantity": entry["Quantity"],
                            "Category": product,
                            "store": "Aldi"
                        })

                    aldi_df = pd.DataFrame(aldi_data)
                    database.append(aldi_df)
                except Exception as e:
                    print(f"Error processing Aldi data: {e}")

            walmart_details = fetch_walmart_products(product)
            
            if walmart_details:
                try:
                    for entry in walmart_details:
                        name = entry["Product"]
                        size = name[::-1].split(",", 1)[0][::-1].strip()
                        price_str = entry["Price"].split("$")[-1]
                        price = float(price_str.strip().replace(",", ""))
                        walmart_data.append({
                            "Product": name.split(",")[0].strip(),
                            "Price": price,
                            "Quantity": size,
                            "Category": entry["Category"],
                            "store": "Walmart"
                        })
                    
                    walmart_df = pd.DataFrame(walmart_data)
                    database.append(walmart_df)   
                except Exception as e:
                    print(f"Error processing Walmart data: {e}")
            
            target_details = fetch_target_products(product)
            if target_details:
                try:
                    for entry in target_details:
                         target_data.append({
                            'Product': entry["Product"],
                            "Price": entry["Price"],
                            'Quantity': entry["Quantity"],
                            'Category': entry["Category"],
                            "store": "Target"
                            })
                         
                    target_df = pd.DataFrame(target_data)
                    database.append(target_df)

                    # Saving target data to db
                    valid_entries = [
                    entry for entry in target_details
                    if (
                        entry.get("Product") and
                        entry.get("Category") and
                        entry.get("Price") is not None and
                        entry.get("Quantity") and
                        standardize_quantity(entry) is not None
                    )]

                    products = [
                    Product(
                        product=entry["Product"],
                        category=entry["Category"],
                        price=float(entry["Price"]),
                        quantity=entry["Quantity"] or None,
                        standardized_quantity=standardize_quantity(entry) or None,
                        store="Target"
                    )
                    for entry in valid_entries ]
                    # Product.objects.bulk_create(products)

                    # if not Product.objects.filter(product__in=[product.product for product in products]).exists():
                    #     raise Exception("Data was not saved to the database.")
    
                    # print(f"Successfully saved {len(products)} products to the database.")

                except Exception as e:
                    print(f"Error processing Target data: {e}")

        if database == []:
            return JsonResponse("No data found", status=500)
        
        
        return data_cleaning(database)
        
    
    except Exception as e:
        print(f"Error in fetch_products: {e}")
        return JsonResponse({"error": "An error occurred while processing the request."}, status=500)

def data_cleaning(dairyDatabase):

    if isinstance(dairyDatabase, list):
        grocery_db = pd.concat(dairyDatabase, ignore_index=True)
    elif isinstance(dairyDatabase, pd.DataFrame):
        grocery_db = dairyDatabase

    cleaned_grocery_db = grocery_db.dropna()
    cleaned_grocery_db['Standardized_Quantity'] = cleaned_grocery_db.apply(standardize_quantity, axis=1)
    cleaned_grocery_db = cleaned_grocery_db[cleaned_grocery_db['Standardized_Quantity'].notnull()]

    if cleaned_grocery_db.empty:
        return JsonResponse({'message': 'No valid data after cleaning.'}, status=200)
        
    get_cheapest_products = priceComparison(cleaned_grocery_db)
    return JsonResponse(get_cheapest_products.to_dict(orient='records'), safe=False)

def priceComparison(database):

    database['Price'] = pd.to_numeric(database['Price'], errors='coerce')

    cheapest_products_sorted = database.sort_values(by=['store', 'Price'], ascending=[True, True])

    # for index, row in cheapest_products_sorted.iterrows():
    #     product = row['Product']
    #     category = row['Category']
    #     price = row['Price']
    #     quantity = row['Quantity']
    #     standardized_quantity = row['Standardized_Quantity']
    #     store = row['store']
    #     added_on = datetime.now()  # Set current datetime

    #     # Save to the database
    #     cheapProduct = cheapProducts(
    #         product=product,
    #         category=category,
    #         price=price,
    #         quantity=quantity,
    #         standardized_quantity=standardized_quantity,
    #         store=store,
    #         added_on=added_on
    #     )
    #     cheapProduct.save()

    #print("Data saved successfully!")
    # print(json.dumps(cheapest_products_sorted.to_dict(orient='records'), indent=2))
    return cheapest_products_sorted





