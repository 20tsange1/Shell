from error import ArgumentError, FileError, FlagError
from typing import List
from application import Application


class Sort(Application):
    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Sorts the input in order

        Parameters:
            args (List[str]): Arguments to be passed
            out (List[str]): Output for stdout

        Exceptions:
            ArgumentError: If wrong number of arguments passed
            FileError: If file does not exist
        """
        reverse = False
        filename = None

        if len(args) > 2:
            raise ArgumentError(
                "Wrong number of command line arguments [sort -r? <file>?]"
            )
        elif len(args) == 1:
            if args[0] == "-r":
                reverse = True
            else:
                filename = args[0]
        elif len(args) == 2:
            if args[0] == "-r":
                reverse = True
                filename = args[1]
            else:
                raise FlagError("Wrong flags [sort -r? <file>?]")
        else:
            pass

        if filename:
            try:
                with open(filename, "r") as file:
                    lines = file.readlines()
                    if len(lines) > 0 and lines[-1][-1] != "\n":
                        lines[-1] += "\n"
            except FileNotFoundError:
                raise FileError(f"File does not exist - {filename}")

        else:
            # If no filename, read from stdin
            lines = self.stdin_check()

        sorted_lines = sorted(lines, reverse=reverse)

        out.extend(sorted_lines)
