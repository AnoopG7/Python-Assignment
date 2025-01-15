import requests

# Fetch data from a public API
url = "https://jsonplaceholder.typicode.com/posts/1"  # Sample public API for testing
try:
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP request errors
    data = response.json()  # Parse JSON response

    # Print part of the JSON data
    print("Title:", data.get("title"))
    print("Body:", data.get("body"))
except requests.exceptions.RequestException as e:
    print("An error occurred while fetching data:", e)
