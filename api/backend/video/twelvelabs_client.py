import os
from search import search
from auth import get_headers

# Set up the environment variables for API URL and Index ID
API_URL = os.getenv("API_URL", "https://api.twelvelabs.io/v1.1")  # Default API URL as an example
INDEX_ID = "<YOUR_INDEX_ID>"  # Set your Index ID here

# Get the headers using the auth module
headers = get_headers()

# Define the query and search options
query = "car accidents"
search_options = ["visual"]

# Call the search function from refactored_search.py
search(API_URL, headers, INDEX_ID, query, search_options)

if __name__ == "__main__":
    main()