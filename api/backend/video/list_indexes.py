import requests

url = "https://api.twelvelabs.io/v1.1/indexes?page=1&page_limit=10&sort_by=created_at&sort_option=desc"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.text)