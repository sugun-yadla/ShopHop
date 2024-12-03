from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from rest_framework.decorators import api_view
from shophop.models import Product

def standardize_quantity(row):
    try:
        quantity = row['Quantity']
        
        if pd.isna(quantity):
            return None  
        
        quantity = quantity.lower()
        quantity = quantity.replace("ounce", "oz")
        match = re.search(r'([\d.]+)\s*(fl oz|gallon|gal|oz|carton|ct|dozen|count|lb)', quantity)
        
        if match:
            value, unit = match.groups()
            value = float(value)
            
            if "gallon" in unit or "gal" in unit:
                return f"{value * 128:.2f} oz"
            elif "fl oz" in unit or "oz" in unit:
                return f"{value:.2f} oz"
            elif "carton" in unit or "ct" in unit or "dozen" in unit or "count" in unit:
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


@api_view(('GET',))
def fetch_products(request, product):
    try:
        dairy_products = [product.strip() for product in product.split(',')] 
        database = []
        walmart_data = []

        for product in dairy_products:
            aldi_details = fetch_aldi_products(product)
            
            if aldi_details:
                try:
                    aldi_df = pd.DataFrame(aldi_details)
                    aldi_df["Price"] = aldi_df["Price"].str.replace('$', '').astype(float)
                    aldi_df["Category"] = product
                    aldi_df["store"] = "Aldi"
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

        if database == []:
            return JsonResponse("No data found", status=500)
        
        #final_df = pd.concat(dairyDatabase, ignore_index=True)

        return data_cleaning(database)
        
        #print("final_df: ",final_df)


        #final_df['Standardized_Quantity'] = final_df.apply(standardize_quantity, axis=1)
        #final_df = final_df[final_df['Standardized_Quantity'].notna()]

        #cheapest_group = final_df.loc[final_df.groupby(['Category','Standardized_Quantity'])['Price'].idxmin()]
        #return JsonResponse(final_df.to_dict(orient='records'), safe=False)
    except Exception as e:
        print(f"Error in fetch_products: {e}")
        return JsonResponse({"error": "An error occurred while processing the request."}, status=500)

def data_cleaning(dairyDatabase):

    #print("dairyDatabase: ",dairyDatabase)
    #print(dairyDatabase)
    if isinstance(dairyDatabase, list):
        grocery_db = pd.concat(dairyDatabase, ignore_index=True)
    elif isinstance(dairyDatabase, pd.DataFrame):
        grocery_db = dairyDatabase
    cleaned_grocery_db = grocery_db.dropna()
    cleaned_grocery_db['Standardized_Quantity'] = cleaned_grocery_db.apply(standardize_quantity, axis=1)
    #grocery_db = grocery_db[grocery_db['Standardized_Quantity'].notna()]

    return JsonResponse(cleaned_grocery_db.to_dict(orient='records'), safe=False)