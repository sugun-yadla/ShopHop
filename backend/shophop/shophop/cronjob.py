from shophop.views import updated_price_drop_tracker
import os
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))  # Path to 'cronjob.py'
log_file_path = os.path.join(current_dir, "cron_test.log")

def sendDataToPriceDrop():
        url = 'http://127.0.0.1:8000/api/price_drop_tracking'
        try:
            response = requests.get(url)
            with open(log_file_path, "a") as f:
                f.write(f"Request sent. Response status code: {response.status_code, response.json}\n")
        except requests.exceptions.RequestException as e:
            with open(log_file_path, "a") as f:
                f.write(f"Error: {e}\n")
        
        #logger.info(f"Error fetching data: {e}")
    # log_file_path = os.path.join(current_dir, "cron_test.log")
    
    