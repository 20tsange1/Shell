import os
from typing import List
from application import Application
from error import ArgumentError, FlagError, DirectoryError, FileError


class Cp(Application):
    def copy_file(
        self, source: str, destination: str, force: bool, recursive: bool
    ) -> None:
        """
        Checks whether desired destination exists and copies file

        Parameters:
            source (str): Source file or pattern
            destination (str): Destination directory
            force (bool): force overwrite
            recursive (bool): copy directories recursively

        Exceptions:
            FileNotFoundError: If source file does not exist
        """
        if os.path.isfile(source):
            dest_file = destination
        elif os.path.isdir(source):
            if os.path.exists(destination) and os.path.isfile(destination):
                raise DirectoryError("Cannot copy a directory into a file.")
            dest_file = (
                os.path.join(destination, os.path.basename(source))
                if os.path.isdir(destination)
                else destination
            )
        else:
            raise FileError(f"Source '{source}' does not exist.")
        if os.path.exists(dest_file):
            if not force:
                raise FileError(
                    f"""Destination file '{dest_file}' already exists. \
                    Use -f to force overwrite"""
                )
        if os.path.isdir(source) and recursive:
            for root, dirs, files in os.walk(source):
                rel_root = os.path.relpath(root, source)
                dest_root = os.path.join(destination, rel_root)
                os.makedirs(dest_root, exist_ok=True)
                for file in files:
                    src_path = os.path.join(root, file)
                    dest_path = os.path.join(dest_root, file)
                    with open(src_path, "r") as f:
                        source_lines = f.readlines()
                    with open(dest_path, "w") as f:
                        f.writelines(source_lines)
        else:
            with open(source, "r") as f:
                source_lines = f.readlines()
            with open(dest_file, "w") as f:
                f.writelines(source_lines)

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Copies a file

        Parameters:
            args (List[str]): Arguments to be passed
            out (List[str]): Output for stdout

        Exceptions:
            ArgumentError: If wrong number of arguments passed
        """
        if len(args) < 2 or len(args) > 3:
            raise ArgumentError(
                "Insufficient number of command line arguments"
            )
        force = False
        recursive = False
        while args[0].startswith("-"):
            option = args.pop(0)
            if option == "-f":
                force = True
            elif option == "-r" or option == "-R":
                recursive = True
            else:
                raise FlagError(f"Invalid option: {option}")
        for i in range(0, len(args), 2):
            source = args[i]
            destination = args[i + 1]
            self.copy_file(source, destination, force, recursive)
