# ShopHop
ShopHop is a convenient web application designed to help users find the best deals on groceries. It combines price comparison, notifications, intelligent recipe recommendations and chrome extension to simplify your grocery shopping experience.  

Video Submission: [https://drive.google.com/file/d/1lzRxBgzZMD0YbC2msIhyY7S3Kgf5tcTM/view?usp=sharing](https://drive.google.com/file/d/1lzRxBgzZMD0YbC2msIhyY7S3Kgf5tcTM/view?usp=sharing)

### Features

1. **Google OAuth 2.0 Login**:  
A seamless and secure sign-in experience using Google OAuth, ensuring quick access to your personalized shopping experience.  

2. **Grocery Price Comparison**:  
Users can search for grocery items, and ShopHop will compare the per-unit prices across three major stores—Aldi, Walmart, and Target. The results are displayed in ascending order, with the lowest price highlighted for easy decision-making.  

3. **Price Tracking and Alerts**:
Add grocery items to your price tracking list, and our daily cron job will monitor price changes for these products. If a price drop is detected, users are promptly notified via email, ensuring they never miss a deal.  

4. **Recipe Recommendations**:
Mention the ingredients you have, and ShopHop will generate recipe ideas using advanced Large Language Models (LLM). This feature offers creative and personalized cooking suggestions based on the ingredients you specify.  

5. **Chrome Extension**:  
Enhance your shopping experience with our Chrome extension! While browsing websites like Target, Walmart, or Aldi, the extension will notify you if the same product is available at a lower price on any of these stores, helping you save effortlessly.
  
# Installation and Configuration  
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
  
3. Configure Environment Variables. Navigate to the project directory and create a .env file. Add the following details to the .env file (replace placeholders with actual values).
```bash
GOOGLE_OAUTH_CLIENT_ID='your_GOOGLE_OAUTH_CLIENT_ID'
``` 

4. Run the app
```bash
streamlit run main.py
```

### Testing

```bash
cd frontend/test
pytest
```

## Backend

The backend of this application is built using Django and uses PostgreSQL for the database. To start the backend server, follow the steps:

1. Setup and activate a virtual environment for Python dependencies. Navigate to the backend directory.
```bash
cd backend/shophop/
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

## Chrome Extension

As the Chrome Extension is not published to the Chrome Marketplace, it needs to be added to Chrome be enabling Developer Options.
It is developed using HTML, CSS and JavaScript and uses JS libraries to communicate with the backend using REST APIs.

1. Go to `chrome://extensions`

2. Enable Developer Mode by clicking the toggle switch next to Developer mode

3. Click the Load unpacked button and select the extension directory (which is `ShopHop/chrome-extension/`)


# Database  
The application uses two primary PostgreSQL tables to manage and store data:  
`shophop_user`, `⁠ productData` and `shophop_saveditem`.  
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

3. `⁠shophop_productData`  
Stores the latest prices for grocery categories.  
* Usage:  
    category ⁠: Name of the grocery category (e.g., "Eggs").  
    price ⁠: Current lowest price for the category.  

* Purpose:  
    Maintains the cheapest prices from scraping, used to detect price drops.  

*Workflow*:
When a price drop is found in ⁠ productData ⁠, it's compared with ⁠ SavedItem ⁠ to notify users via Email.  

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
  We use a prompt that specifies the format in which the output should be generated, so that the outputs remains consistent among multiple different inputs.  
  We also specify what information we want from the recipe itself.
  
  ### 2. Input Transformation:

  The user's ingredient list is then converted into a structured prompt that is separated by commas, which then guides the AI to generate specific, structured recipe 
  recommendations. The prompt includes clear instructions about the desired output format.
  
### 3. API Communication
```python
url = "http://localhost:11434/api/generate"
payload = {
  "model": "mistral",
  "prompt": prompt,
  "stream": False
}
```
Uses Ollama's local API endpoint and specifies the Mistral model.
'stream: False' means the entire response is generated at once
 ### 4. Mistral Model Specs
 a.  Model Type: Large Language Model (LLM)  
 b.  Parameters: 7 Billion parameters  
 c.  Architecture: Transformer-based  
 d.  Provider: Ollama  
 
### 5. Installation
Visit https://ollama.com/ and download the application  
Install the Mistral model by running:
```ollama pull mistral```

