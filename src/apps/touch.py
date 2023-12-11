import os
from error import ArgumentError, FileError
from typing import List
from application import Application


class Touch(Application):
    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Creates an empty file if it doesn't already exist

        Parameters:
            args (List[str]): Arguments to be passed.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            FileError: If file already exists.
        """
        if len(args) != 1:
            raise ArgumentError("Wrong number of command line arguments")
        else:
            file_path = args[0]
            if not os.path.exists(file_path):
                with open(file_path, "w+"):
                    pass
            else:
                raise FileError(f"File '{file_path}' already exists")
