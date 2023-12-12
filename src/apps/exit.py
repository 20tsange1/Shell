import sys
from application import Application


class Exit(Application):
    """
    Exits the shell.
    
    Usage: exit
    """
    def execute(self, args=None, out=None) -> None:
        """
        Executes the exit command
        """
        print("Exiting shell. Goodbye! 👋")
        sys.exit()
