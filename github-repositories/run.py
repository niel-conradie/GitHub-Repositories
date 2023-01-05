from repositories import Repositories


def run():
    """GitHub-Repositories."""
    run = Repositories()

    try:
        # Starting the application.
        run.start_app()
    except KeyboardInterrupt:
        # Stopping the application.
        quit("\n\nProgram Terminated")


if __name__ == "__main__":
    run()
