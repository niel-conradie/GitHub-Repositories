import requests

from plotly.graph_objs import Bar
from plotly import offline


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

# Preparing visualization data.
names, stars = [], []
for item in items:
    names.append(item["name"])
    stars.append(item["stargazers_count"])

# Make visualization.
visual_data = [
    {
        "type": "bar",
        "x": names,
        "y": stars,
        "marker": {
            "color": "rgb(60, 100, 150)",
            "line": {
                "width": 1.5,
                "color": "rgb(25, 25, 25)",
            },
        },
        "opacity": 0.6,
    }
]

my_layout = {
    "title": "Most-Starred Python Projects on Github",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Repository",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
    "yaxis": {
        "title": "Stars",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
}

fig = {"data": visual_data, "layout": my_layout}
offline.plot(fig, filename="github-repositories/languages/python.html")
