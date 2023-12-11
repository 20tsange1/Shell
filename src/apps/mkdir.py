import os
from error import ArgumentError, DirectoryError
from typing import List
from application import Application


class Mkdir(Application):
    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Creates a directory

        Parameters:
            args (List[str]): Arguments to be passed

        Exceptions:
            ArgumentError: If wrong number of arguments passed
        """
        if len(args) != 1:
            raise ArgumentError("Wrong number of command line arguments")
        else:
            try:
                os.mkdir(args[0])
            except FileExistsError:
                raise DirectoryError("Directory already exists")