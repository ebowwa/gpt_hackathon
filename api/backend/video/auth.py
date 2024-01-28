# auth.py
# This script provides a function to create headers for API requests

import os

def get_headers(api_key=None):
    if api_key is None:
        api_key = os.environ.get('API_KEY', 'YOUR_API_KEY_HERE')

    headers = {
        "x-api-key": api_key
    }
    return headers
  
if __name__ == "__main__":
  print("Task Complete")