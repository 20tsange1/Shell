import sys
from error import ArgumentError
from typing import List


class Application:
    def execute(
        self, args: List[str], out: List[str]
    ) -> None:  # pragma: no cover
        pass

    def stdin_check(self) -> List[str]:
        """
        Stdin handling with exception

        Returns:
            (List[str]): Returns list of lines read from stdin

        Exceptions:
            ArgumentError: If no standard input detected
        """
        lines = sys.stdin.readlines()
        if lines:
            return lines
        else:
            raise ArgumentError("No standard input detected")
