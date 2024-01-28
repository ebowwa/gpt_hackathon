python
Copy code
import requests
import os
from pprint import pprint

# Set up the environment variables for API URL and API Key
API_URL = os.getenv("API_URL")
assert API_URL, "API_URL environment variable is not set."

API_KEY = os.getenv("API_KEY")
assert API_KEY, "API_KEY environment variable is not set."

# Set your Index ID
INDEX_ID = "<YOUR_INDEX_ID>"

# Define the search endpoint URL
SEARCH_URL = f"{API_URL}/search"

# Set up the headers with your API Key
headers = {"x-api-key": API_KEY}

# Define the data payload for your request
data = {
    "query": "car accidents",
    "index_id": INDEX_ID,
    "search_options": ["visual"],
}

# Make the POST request to the search endpoint
response = requests.post(SEARCH_URL, headers=headers, json=data)

# Check the response status and print the JSON result
print(f"Status code: {response.status_code}")
pprint(response.json())