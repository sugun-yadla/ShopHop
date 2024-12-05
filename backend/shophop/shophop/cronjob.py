from shophop.views import updated_price_drop_tracker
import os

def print_hello():
    updated_price_drop_tracker.printData()
    # current_dir = os.path.dirname(os.path.abspath(__file__))  # Path to 'cronjob.py'
    # log_file_path = os.path.join(current_dir, "cron_test.log")
    
    # with open(log_file_path, "a") as f:
    #     f.write("hello\n")