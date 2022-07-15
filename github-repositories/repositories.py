import requests


# Make an API call and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
request = requests.get(url, headers=headers)
print(f"Status code: {request.status_code}")

# Store API response in a variable.
data = request.json()

# Process results.
print(data.keys())
