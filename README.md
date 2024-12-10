# ShopHop
ShopHop is a convenient web application designed to help users find the best deals on groceries. It combines price comparison, notifications, intelligent recipe recommendations and chrome extension to simplify your grocery shopping experience.  
1. Google Login:  
A seamless and secure sign-in experience using Google OAuth, ensuring quick access to your personalized shopping experience.  
2. Grocery Price Comparison:  
Users can search for grocery items, and ShopHop will compare the per-unit prices across three major stores—Aldi, Walmart, and Target. The results are displayed in ascending order, with the lowest price highlighted for easy decision-making.  
3. Price Tracking and Alerts:  
Add grocery items to your price tracking list, and our weekly (every Sunday) cron job will monitor price changes for these products. If a price drop is detected, users are promptly notified via email, ensuring they never miss a deal.  
4. Recipe Recommendations:  
Mention the ingredients you have, and ShopHop will generate recipe ideas using advanced Large Language Models (LLM). This feature offers creative and personalized cooking suggestions based on the ingredients you specify.  
5. Chrome Extension:  
Enhance your shopping experience with our Chrome extension, allowing you to access ShopHop’s features directly while browsing the web. Quickly check prices, track items, and get recipe recommendations without leaving your browser.  
  
# Installation and Configuration  
### Frontend

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
  
3. Configure Environment Variables. Navigate to the project directory and create a .env file. Add the following details to the .env file (replace placeholders with actual values).
```bash
GOOGLE_OAUTH_CLIENT_ID='your_GOOGLE_OAUTH_CLIENT_ID'
``` 

4. Run the app
```bash
streamlit run main.py
```

### Backend

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
SENDER_EMAIL_ID='your_email_address for price drop alert'
SENDER_EMAIL_PASSWORD='your_password'
CLIENT_ID='your_client_id'
CLIENT_SECRET='your_client_secret'
```

4. Run the Django development server
```bash
python3 manage.py runserver
```  
  
# Dataset  
The application uses two primary PostgreSQL tables to manage and store data:  
`shophop_user` and `shophop_saveditem`.  
These tables are designed to track user information and the products they wish to monitor for price changes.  
1. `shophop_user`  
This table stores details about the users of the ShopHop platform. It serves as the foundational dataset for all user-related operations, including authentication, user activity, and user account management.  

* Usage:  
    a. `id`: Automatically increments with each new user. It is the primary key.  
    b. `is_superuser`: If true, the user has the highest level of access (admin privileges).  
    c. `username`: Unique username chosen by the user for login  
    d. `first_name`: First name of the user  
    e. `last_name`: Last name of the user  
    f. `date_joined`: Timestamp of when the user login to their account.   
    g. `email`: Email address of the user, must be unique for each user  
    
* Purpose:  
    a. `Authentication`: Stores password and login details for user authentication.  
    b. `User Management`: Tracks user status (is_superuser, is_staff, is_active) to manage permissions.  
    c. `Profile Information`: Stores user profile details such as first_name, last_name, email, and username.   
    d.  `User Activity`: The last_login and date_joined columns track user activity and account creation timestamps.  
    e. `Registration Method`: Identifies how a user registered, which could be useful for analytics or troubleshooting.  

2. `shophop_saveditem`  
This table stores information about products that users have selected for price tracking. Each entry represents a saved item, including the product's name, price, and the user who saved it.  
* Usage :  
    a. `id`: Automatically increments with each new saved item. It is the primary key.  
    b. `name`: The name of the product being tracked by the user.  
    c. `price`: The price of the product when it was saved.  
    d. `user_id`: Links to the `id` in the `shophop_user` table, indicating which user saved the item.  
    
    This table helps track the products each user is interested in for price monitoring and allows users to see the price history of their saved items.  

* Purpose:  
    This table plays a crucial role in the weekly price tracking process. When the weekly cron job runs, it checks the prices of all the items saved in the `shophop_saveditem` table. The cron job compares the current price of each product with the saved price. If there is a price drop for any item, the system notifies the respective user about the updated price. This ensures users are always alerted to any changes in the prices of the products they are monitoring.

# AI models

  In our recipe recommender, the AI model (Mistral) is utilized through a key function get_recipe_recommendations(). 
  
  ### 1. Prompt Engineering
    prompt = f"""Please suggest some creative and delicious recipes using the following ingredients: {', '.join(ingredients)}. 
    For each recipe, provide:
    - Recipe name
    - Brief description
    - Key ingredients
    - Simple cooking instructions
    
    Aim for diverse and interesting recipe ideas that make the most of these ingredients."""
  
  ### 2. Input Transformation:

  The user's raw ingredient list is converted into a structured prompt, which then guides the AI to generate specific, structured recipe recommendations.
  The prompt includes clear instructions about the desired output format
  
  ### 3. API Communication
    payload = {
    "model": "mistral",
    "prompt": prompt,
    "stream": False
    }
Uses Ollama's local API endpoint and specifies the Mistral 7B model.
'stream: False' means the entire response is generated at once
 ### 4. Mistral Model Specs
 a.  Model Type: Large Language Model (LLM)
 b.  Parameters: 7 Billion parameters
 c.  Architecture: Transformer-based
 d.  Provider: Ollama


