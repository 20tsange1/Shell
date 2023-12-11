import sys
from application import Application


class Exit(Application):
    def execute(self, args=None, out=None) -> None:
        """
        Exits the shell
        """
        print("Exiting shell. Goodbye! 👋")
        sys.exit()
