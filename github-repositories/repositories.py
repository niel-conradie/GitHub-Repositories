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

# Examine the first repository.
repository = items[0]
print("\nSelected information about each repository:")
for data in items:
    print(f"\nName: {repository['name']}")
    print(f"Owner: {repository['owner']['login']}")
    print(f"Stars: {repository['stargazers_count']}")
    print(f"Repository: {repository['html_url']}")
    print(f"Created: {repository['created_at']}")
    print(f"Updated: {repository['updated_at']}")
    print(f"Description: {repository['description']}")
