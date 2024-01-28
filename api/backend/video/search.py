import requests
import json
import os

API_URL = os.getenv("API_URL")
assert API_URL, "API_URL is not set"

API_KEY = os.getenv("API_KEY")
assert API_KEY, "API_KEY is not set"

INDEX_ID = "<YOUR_INDEX_ID>"

SEARCH_URL = f"{API_URL}/search"

headers = {
    "x-api-key": API_KEY
}

data = {
    "query": "car accidents",
    "index_id": INDEX_ID,
    "search_options": ["visual"],
}

# Explicitly encoding the data
encoded_data = json.dumps(data).encode('utf-8')

response = requests.post(SEARCH_URL, headers=headers, data=encoded_data)
print(f"Status code: {response.status_code}")
print(response.json())
