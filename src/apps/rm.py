import os
from error import ArgumentError, FileError, DirectoryError
from typing import List
from application import Application


class Rm(Application):
    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Removes a file

        Parameters:
            args (List[str]): Arguments to be passed

        Exceptions:
            ArgumentError: If wrong number of arguments passed
            FileError: If file does not exist
        """
        if len(args) != 1:
            raise ArgumentError("Wrong number of command line arguments")
        elif os.path.isdir(args[0]):
            raise DirectoryError(f"Cannot remove a directory - {args[0]}")
        else:
            try:
                os.remove(args[0])
            except FileNotFoundError:
                raise FileError(f"File does not exist - {args[0]}")
