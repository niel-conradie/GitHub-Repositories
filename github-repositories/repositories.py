import requests

from plotly.graph_objs import Bar
from plotly import offline


class Repositories:
    """Most-Starred Projects on Github."""

    def user_input(self):
        """Requesting user input and validating choice."""
        while True:
            user_input = input("\nPick a language: ").lower()
            choices = [
                "c",
                "c++",
                "c#",
                "go",
                "java",
                "javascript",
                "php",
                "python",
                "ruby",
                "scala",
                "typescript",
            ]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            else:
                return user_input

    def request_data(self, user_input):
        """Request API data from Github and store in a variable."""
        # Make an API call and store the response.
        url = f"https://api.github.com/search/repositories?q=language:{user_input}&sort=stars"
        headers = {"Accept": "application/vnd.github.v3+json"}
        request = requests.get(url, headers=headers)
        print(f"Status code: {request.status_code}")

        # Store API response in a variable.
        data = request.json()
        print(f"Total repositories: {data['total_count']}")

        return data

    def display_request_data(self, data):
        """Display requested data in the terminal."""
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

    def prepare_visualization(self, data):
        """Preparing relevant data for visualization."""
        items = data["items"]

        links, stars, labels = [], [], []
        for item in items:
            name = item["name"]
            url = item["html_url"]
            link = f"<a href='{url}'>{name}</a>"
            links.append(link)

            stars.append(item["stargazers_count"])

            owner = item["owner"]["login"]
            description = item["description"]
            label = f"{owner}<br />{description}"
            labels.append(label)

        return links, stars, labels

    def visualization(self, user_input, links, stars, labels):
        """Visualize prepared data, generate graph with plotly."""
        data = [
            {
                "type": "bar",
                "x": links,
                "y": stars,
                "hovertext": labels,
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

        layout = {
            "title": f"Most-Starred {user_input.title()} Projects on Github",
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

        fig = {"data": data, "layout": layout}
        offline.plot(fig, filename=f"github-repositories/{user_input}.html")
