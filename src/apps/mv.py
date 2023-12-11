import os
from error import ArgumentError, FileError
from typing import List
from application import Application


class Mv(Application):
    def move_file(self, source: str, destination: str, force: bool) -> None:
        """
        Checks whether desired destination exists and moves file

        Parameters:
            source (str): Source file or pattern
            destination (str): Destination directory
            force (bool): force overwrite

        Exceptions:
            FileNotFoundError: If source file does not exist
            FileExistsError: If destination file already exists
        """
        if not os.path.exists(source):
            raise FileError(f"Source file '{source}' does not exist.")
        if os.path.isdir(destination):
            dest_file = os.path.join(destination, os.path.basename(source))
        elif os.path.exists(destination):
            if not force:
                raise FileError(
                    """Destination file already exists. \
                    Use -f to force overwrite"""
                )
            dest_file = destination
        else:
            dest_file = destination
        os.rename(source, dest_file)

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Moves a file

        Parameters:
            args (List[str]): Arguments to be passed

        Exceptions:
            ArgumentError: If wrong number of arguments passed
        """
        if len(args) < 2 or len(args) > 3:
            raise ArgumentError(
                "Insufficient number of command line arguments"
            )
        force = False
        if args[0] == "-f":
            force = True
            args = args[1:]

        for i in range(0, len(args), 2):
            source = args[i]
            destination = args[i + 1]
            self.move_file(source, destination, force)
