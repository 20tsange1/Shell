from error import FileError
from typing import List
from application import Application


class Cat(Application):
    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Concatenates input files

        Parameters:
            args (List[str]): Arguments (filenames) to be passed
            out (List[str]): Output for stdout

        Exceptions:
            FileError: If file does not exist
        """
        if len(args) == 0:
            out.extend(self.stdin_check())
        else:
            for a in args:
                try:
                    with open(a.rstrip()) as f:
                        # out.append(f.read())
                        out.extend(f.readlines())
                except FileNotFoundError:
                    raise FileError(f"File does not exist - {a}")
        if len(out) > 0 and out[-1][-1] != "\n":
            out[-1] += "\n"
