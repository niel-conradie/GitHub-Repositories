from repositories import Repositories


if __name__ == "__main__":
    run = Repositories()

    try:
        # Starting the application.
        run.start_app()
    except KeyboardInterrupt:
        # Stopping the application.
        quit("\n\nProgram Terminated")
