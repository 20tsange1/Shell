from application import Application


class UnsafeDecorator(Application):
    def __init__(self, wrapped_application: Application):
        self.wrapped_application = wrapped_application

    def execute(self, args, out):
        """
        Wraps the application in a try except block

        Parameters:
            args (List[str]): Arguments to be passed
            out (List[str]): Output for stdout
        """
        try:
            # Execute the wrapped command
            self.wrapped_application.execute(args, out)
        except Exception as e:
            # Catch any exceptions and print them to out
            out.append(f"An exception occurred: {str(e)}\n")
