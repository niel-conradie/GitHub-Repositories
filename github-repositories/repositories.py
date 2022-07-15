import requests


# Make an API call and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
request = requests.get(url, headers=headers)
print(f"Status code: {request.status_code}")

# Store API response in a variable.
data = request.json()
print(f"Total repositories: {data['total_count']}")

# Explore information about the repositories.
items = data["items"]
print(f"Repositories returned: {len(items)}")

# Examine each repository.
print("\nSelected information about each repository:")
for item in items:
    print(f"\nName: {item['name']}")
    print(f"Owner: {item['owner']['login']}")
    print(f"Stars: {item['stargazers_count']}")
    print(f"Repository: {item['html_url']}")
    print(f"Created: {item['created_at']}")
    print(f"Updated: {item['updated_at']}")
    print(f"Description: {item['description']}")
