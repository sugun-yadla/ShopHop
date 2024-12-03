#$ pip install pandas requests beautifulsoup4 price-parser|| do this on the terminal before running the code
import smtplib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price

PRODUCT_URL_CSV = "products.csv" #The CSV that contains the target URLs, the csv needs to have two fields, url and alert_price(can be changed accordingly)
SAVE_TO_CSV = True
PRICES_CSV = "prices.csv" # if needed, we can make it so that it saves the data to a database instead, I just made it a csv since its easier to work with, but we can edit accordingly
SEND_MAIL = True


def get_urls(csv_file):
    df = pd.read_csv(csv_file)
    return df


def get_response(url):
    response = requests.get(url)
    return response.text

def get_price(html):
    soup = BeautifulSoup(html, "lxml")
    el = soup.select_one(".price_color")
    price = Price.fromstring(el.text)
    return price.amount_float

def process_products(df):
    updated_products = []
    for product in df.to_dict("records"):
        html = get_response(product["url"])
        product["price"] = get_price(html)
        product["alert"] = product["price"] < product["alert_price"]
        updated_products.append(product)
    return pd.DataFrame(updated_products)

def get_mail(df):
    subject = "Price Drop Alert"
    body = df[df["alert"]].to_string()
    subject_and_message = f"Subject:{subject}\n\n{body}"
    return subject_and_message

def send_mail(df):
    message_text = get_mail(df)
    with smtplib.SMTP("smtp.server.address", 587) as smtp:
        smtp.starttls()
        smtp.login(mail_user, mail_pass)#must initialize the mail_user(usename) and mail_pass(account password) assuming we would get this from login account details, same with the mail_to(email)
        smtp.sendmail(mail_user, mail_to, message_text)

def main():
    df = get_urls(PRODUCT_URL_CSV)
    df_updated = process_products(df)
    if SAVE_TO_CSV:
        df_updated.to_csv(PRICES_CSV, index=False, mode="a")
    if SEND_MAIL:
        send_mail(df_updated)

