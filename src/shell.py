import io
import os
import sys
from antlr.Comp0010ShellLexer import Comp0010ShellLexer
from antlr.Comp0010ShellParser import Comp0010ShellParser
from antlr4 import InputStream, CommonTokenStream
from collections import deque
from error import (
    ArgumentError,
    FlagError,
    FileError,
    RedirectError,
    ApplicationError,
    DirectoryError,
)
from typing import List
from visitor import Visitor


def parse(cmdline: str, out: List[str]):
    """
    Parses a command line input and appends execution result to output

    Parameters:
        cmdline (str): Command line input
        out (List[str]): Output deque
    """
    input_stream = InputStream(io.StringIO(cmdline).read())
    lexer = Comp0010ShellLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Comp0010ShellParser(stream)
    tree = parser.command()
    visitor = Visitor()
    visitor.visit(tree)
    for i in visitor.output:
        out.extend(i)


def catch_error(cmdline: str, out: List[str]):  # pragma: no cover
    """
    Catches errors for interactive mode

    Parameters:
        cmdline (str): Command line input
        out (List[str]): Output deque
    """
    try:
        parse(cmdline, out)
    except ValueError as e:
        print("The following error has occured [USER]: " + str(e))
    except ArgumentError as e:
        print("The following error has occured [ARGUMENT]: " + str(e))
    except ApplicationError as e:
        print("The following error has occured [APPLICATION]: " + str(e))
    except DirectoryError as e:
        print("The following error has occured [DIRECTORY]: " + str(e))
    except FileError as e:
        print("The following error has occured [FILE]: " + str(e))
    except FlagError as e:
        print("The following error has occured [FLAG]: " + str(e))
    except RedirectError as e:
        print("The following error has occured [REDIRECT]: " + str(e))
    # except Exception as e:
    #     print("An unknown error has occured: " + str(e))


def run():  # pragma: no cover
    """
    Runs the shell
    """
    args_num = len(sys.argv) - 1
    if args_num > 0:
        if args_num != 2:
            raise ValueError("Wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"Unexpected command line argument {sys.argv[1]}")
        out = deque()
        parse(sys.argv[2], out)
        while len(out) > 0:
            print(out.popleft(), end="")
    else:
        while True:
            print(os.getcwd() + "> ", end="")
            cmdline = input()
            out = deque()
            catch_error(cmdline, out)
            while len(out) > 0:
                print(out.popleft(), end="")


if __name__ == "__main__":  # pragma: no cover
    run()
