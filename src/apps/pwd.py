import os
from typing import List
from application import Application


class Pwd(Application):
    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Returns the current directory

        Parameters:
            args (List[str]): Arguments to be passed
            out (List[str]): Output for stdout
        """
        out.append(os.getcwd() + "\n")
