import os
from typing import List, Tuple
from application import Application
from error import FileError, FlagError


class Wc(Application):
    def parse_arguments(self, args: List[str]) -> Tuple[List[str], List[str]]:
        """
        Parses command-line arguments into flags and file paths

        Parameters:
            args (List[str]): Command-line arguments

        Returns:
            Tuple[List[str], List[str]]: Lists of flags and file paths
        """
        flags = []
        file_paths = []
        for arg in args:
            if arg.startswith("-"):
                flags.extend(arg[1:])
            else:
                file_paths.append(arg)
        return flags, file_paths

    def count(self, lines: List[str]) -> Tuple[int, int, int]:
        """
        Counts the number of lines, words, and characters in a list of strings

        Parameters:
            lines (List[str]): List of strings representing lines of text

        Returns:
            Tuple[int, int, int]: Count of lines, words, and characters
        """
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
        return num_lines, num_words, num_chars

    def handle_flags(
        self,
        flags: List[str],
        num_lines: int,
        num_words: int,
        num_chars: int,
        out: List[str],
    ) -> None:
        """
        Handles specified flags and appends corresponding output

        Parameters:
            flags (List[str]): List of flags to be processed
            num_lines (int): Number of lines
            num_words (int): Number of words
            num_chars (int): Number of characters
            out (List[str]): List to which the output will be appended

        Exceptions:
            ValueError: If an invalid flag is passed
        """
        if not flags:
            out += [f"{num_lines}\n", f"{num_words}\n", f"{num_chars}\n"]
        for flag in flags:
            if flag == "l":
                out.append(f"{num_lines}\n")
            elif flag == "w":
                out.append(f"{num_words}\n")
            elif flag == "m":
                out.append(f"{num_chars}\n")
            else:
                raise FlagError(f"Invalid flag: {flag}")

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Counts the number of lines, words, and characters in a file

        Parameters:
            args (List[str]): Arguments to be passed

        Exceptions:
            ArgumentError: If wrong number of arguments passed
            FileNotFoundError: If file does not exist
        """
        flags, file_paths = self.parse_arguments(args)
        if not file_paths:
            lines = self.stdin_check()
            num_lines, num_words, num_chars = self.count(lines)
            self.handle_flags(flags, num_lines, num_words, num_chars, out)
        else:
            eol, words, chars = 0, 0, 0
            for file_path in file_paths:
                if not os.path.exists(file_path):
                    raise FileError(f"File '{file_path}' does not exist")
                with open(file_path, "r") as f:
                    lines = f.readlines()
                file_lines, file_words, file_chars = self.count(lines)
                eol += file_lines
                words += file_words
                chars += file_chars
            self.handle_flags(flags, eol, words, chars, out)
