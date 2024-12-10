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
   
