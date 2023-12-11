from error import ArgumentError, FileError, FlagError
from typing import List
from application import Application


class Cut(Application):
    def define_ranges(self, byte_ranges: List[str]) -> List[str]:
        """
        Splits and defines the ranges for cut

        Parameters:
            byte_ranges (List[str]): Initial input arguments

        Returns:
            (List[str]): Returns list of ranges
        """
        byte_ranges = byte_ranges.split(",")
        byte_ranges.sort(key=lambda a: a[0])

        for i, j in enumerate(byte_ranges):
            byte_ranges[i] = j.split("-")
            if len(byte_ranges[i]) == 1:
                byte_ranges[i].append(byte_ranges[i][0])

        intervals = []

        start, end = None, None

        for rng in byte_ranges:
            if start is None and end is None:
                start, end = rng
            elif rng[0] <= end and rng[1] == "":
                intervals.append([start, ""])
                break
            elif rng[1] == "":
                intervals.append([start, end])
                start, end = rng
                break
            elif rng[0] <= end and rng[1] > end:
                end = rng[1]
            elif rng[0] > end:
                intervals.append([start, end])
                start, end = rng
            # else:
            #     continue

        if len(intervals) == 0:
            intervals.append([start, end])
        else:
            if intervals[-1][1] != "":
                intervals.append([start, end])

        return intervals

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Extracts bytes from an input

        Parameters:
            args (List[str]): Arguments to be passed
            out (List[str]): Output for stdout

        Exceptions:
            ArgumentError: If wrong number of arguments passed
            FlagError: If wrong flags passed
            FileError: If file does not exist
        """
        if len(args) == 0 or len(args) > 3:
            raise ArgumentError(
                """Wrong number of command line arguments \
                [cut -b <byte_range> <file>?]"""
            )

        if args[0] != "-b":
            raise FlagError("Wrong flag [cut -b <byte_range> <file>?]")

        bytes_range = args[1]
        if len(args) == 2:
            lines = self.stdin_check()
        else:
            try:
                with open(args[2], "r") as file:
                    lines = file.readlines()
            except FileNotFoundError:
                raise FileError(f"File does not exist - {args[2]}")

        byte_ranges_interval = self.define_ranges(bytes_range)

        for line in lines:
            line_output = []
            line = line.strip()
            for byte_range in byte_ranges_interval:
                start, end = byte_range
                start = int(start) - 1 if start else None
                end = int(end) if end else None
                line_output.append(line[start:end])

            out.append("".join(line_output) + "\n")
