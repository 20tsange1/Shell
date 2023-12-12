from application import Application


class HelpDecorator(Application):
    def __init__(self, wrapped_application: Application):
        self.wrapped_application = wrapped_application

    def execute(self, args, out):
        """
        Adds the -h and --help flags to the wrapped application

        Parameters:
            args (List[str]): Arguments to be passed
            out (List[str]): Output for stdout
        """
        if args and (args[0] == "-h" or args[0] == "--help"):
            out.append(self.wrapped_application.__doc__ + "\n")
        else:
            self.wrapped_application.execute(args, out)
