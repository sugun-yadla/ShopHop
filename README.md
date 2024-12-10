# ShopHop

ShopHop is a webapp to quickly find out the cheapest price for your groceries. Simply search for the product you want, and ShopHop will fetch prices from multiple stores to show you the best deals.

## Frontend

The frontend of this application is built using [Streamlit](https://streamlit.io/), a Python library. To start the frontend server, follow the steps:

1. Setup and activate a virtual environment for Python dependencies (using either `virtualenv` or `venv`)

```bash
cd frontend
virtualenv env -p python3
source env/bin/activate
```

2. Install dependencies

```bash
pip3 install -r requirements.txt
```

3. Run the app

```bash
streamlit run main.py
```

## Backend

The backend of this application is built using Django and uses PostgreSQL for the database. To start the backend server, follow the steps:

1. Setup and activate a virtual environment for Python dependencies. Navigate to the backend directory.

```bash
cd backend/
python3 -m venv env
source env/bin/activate
```

2. Install dependencies

```bash
cd shophop/
pip3 install -r requirements.txt
```

3. Configure Environment Variables. Navigate to the project directory and create a .env file. Add the following details to the .env file (replace placeholders with actual values).

```bash
cd shophop/
```

```
DB_NAME='your_database_name'
DB_USER='your_database_user'
DB_PASSWORD='your_database_password'
DB_HOST='your_database_host'
DB_PORT='your_database_port'
```

4. Run the Django development server

```bash
python3 manage.py runserver
```

## Features

## **`Price Drop Tracker`**

This feature provides a cron job service that tracks price drops for grocery items, maintains user-saved items, and notifies all users of discounts, via email.
Functions Executed:
a. Fetches the lowest prices for a predefined list of grocery items from a web-scraping API which will be used to compare.
b. Fetches the list of all users and their saved items from SavedItems db.
c. Compares prices fetched from the SavedItem database with the current lowest prices fetched from the scraping.
d. Creates a mailing list of users to notify about price drops.
e. Updates the Cheapest Product database with new prices if they are lower than previously saved.
f. Simultaneously, updates the SavedItems db for all users if the new prices are lower.
g. Sends email notifications to all users with details about the price drops, using the SMTP Library.
h. This is a cron job that is scheduled to run daily.

## Models Overview for Databases used:

### 1. **`SavedItem` Model**

Tracks items saved by users for price alerts.

- **Fields**:
  - `user`: Links to the user who saved the item.
  - `name`: Name of the grocery item (e.g., "Onion").
  - `price`: Price at which the item was saved.

### 2. **`productData` Model**

Stores the latest prices for grocery categories.

- **Fields**:
  - `category`: Name of the grocery category (e.g., "Eggs").
  - `price`: Current lowest price for the category.

### Purpose:

- **`SavedItem`**: Tracks user-specific items and their saved prices.
- **`productData`**: Maintains the cheapest prices from scraping, used to detect price drops.

**Workflow**:
When a price drop is found in `productData`, it's compared with `SavedItem` to notify users via Email.
