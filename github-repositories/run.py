from repositories import Repositories


def run():
    """Github-Repositories."""
    run = Repositories()

    # Requesting user input.
    user_input = run.user_input()
    # Store data in a variable.
    data = run.request_data(user_input)
    # Print data in terminal.
    run.display_request_data(data)
    # Store relevant visualization data in variable.
    links, stars, labels = run.prepare_visualization(data)
    # Generate visualization and create .html file.
    run.visualization(user_input, links, stars, labels)


if __name__ == "__main__":
    run()
