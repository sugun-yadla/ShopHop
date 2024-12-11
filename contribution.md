# Contributions by Team Members  
Our project, ShopHop, is a price comparison and product tracking platform built with a comprehensive tech stack. The following technologies were used:  
1. Backend - Django 
2. Frontend: Streamlit  
3. Database: PostgreSQL  
4. Task Scheduling: Django-cron  
5. Web Scraping: BeautifulSoup  
6. Testing: Unittest  
7. Programming Language: Python  
8. Chrome extension development - Javascript, HTML
8. Recipe Recommender Tech Stack: Mistral (via Ollama), Python, Requests, Api: local inference through Ollama, Pytest(testing)

We collaborated by dividing the features and configuration tasks to leverage individual strengths while ensuring seamless integration across components. Below is a detailed summary of each member's contributions:


1. `Gargee Shah`  
    * Responsibilities:  
            a. Configured the Django backend and established a connection to the PostgreSQL database.  
            b. Developed the scraping logic to collect price data from **Aldi** and **Walmart**, ensuring a comprehensive and accurate price comparison system across all platforms.     
            c. Designed and deployed automated periodic tasks using Django-cron to keep price comparisons updated.  

    * Collaboration:  
            a. APIs developed by Gargee powered the Streamlit-based frontend interface created by Adwait, enabling real-time display of price comparisons.  
            b. Integrated Vaishnavi's Target web scraping results, ensuring a unified and dynamic dataset for accurate and on-the-fly price comparisons.  

    * Testing:  
            a. Conducted unit testing for the price comparison logic to ensure accurate data retrieval and correct price comparisons.  
            b. Conducted unit test for cron job functionality.

2. `Adwait Bhope`
    * Responsibilities:   
            a. Developed the frontend using Streamlit, ensuring a user-friendly interface.  
            b. Created a Chrome extension for enhanced user accessibility.  
    
    * Collaboration:  
            a. Consumed APIs from Gargee’s backend to display real-time price comparisons.  
            b. Worked with Sugun to integrate the recipe recommendation feature into the user interface seamlessly.  
    
    * Testing:  
            a. Conducted unit testing for the login system to ensure smooth user authentication and secure access to the platform.

3. `Vaishnavi Daber`
    * Responsibilities:  
            a. Developed the scraping logic to collect price data from **Target** and integrated it with data from **Aldi** and **Walmart**, ensuring a comprehensive and accurate price comparison system across all platforms.    
            b. Implemented a price drop tracker to notify users of significant price changes.  
            c. Set up SMTP for sending real-time alerts.  
    
    * Collaboration:  
            a. Combined Target’s data with Aldi and Walmart’s data scraped by Gargee to enhance the backend.  
            b. Collaborated with Gargee to implement email notifications for users, triggered by the execution of the cron job.
    
    * Testing:  
            a. Conducted testing for the price drop tracker to ensure accurate detection of price changes and timely notifications.

4. `Sugun Yadla`  
    * Responsibilities:  
            a. Developed the front and back end for recipe recommendation system using LLM integration to suggest recipes based on  ingredients mentioned by the user.  
            b. Developed the code for the price drop tracker with the smtp library for sending mail notifications for when the price of an item drops.

    * Collaboration:  
            a. Collaborated with Adwait to ensure that recipe recommendations were displayed interactively on the frontend.  

    * Testing:  
            a. Conducted integration testing for the recipe recommendation system to ensure smooth functionality and accurate recommendations based on user input.  
            b. Conducted SMTP testing to ensure successful email notifications were sent to users for price changes and other alerts.


