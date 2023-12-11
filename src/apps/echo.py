from typing import List
from application import Application


class Echo(Application):
    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Writes arguments passed to stdout

        Parameters:
            args (List[str]): Arguments to be repeated by function
            out (List[str]): Output for stdout
        """
        # if len(args) >= 0:
        out.append(" ".join(args) + "\n")
        # else:
        #     raise ValueError("Wrong number of command line arguments")
        # else:
        #     out.extend(self.stdin_check())
