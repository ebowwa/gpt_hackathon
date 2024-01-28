import requests
from pprint import pprint

def search(api_url, headers, index_id, query, search_options):
    # Define the search endpoint URL
    search_url = f"{api_url}/search"

    # Define the data payload for the request
    data = {
        "query": query,
        "index_id": index_id,
        "search_options": search_options,
    }

    # Make the POST request to the search endpoint
    response = requests.post(search_url, headers=headers, json=data)

    # Check the response status and print the JSON result
    print(f"Status code: {response.status_code}")
    pprint(response.json())