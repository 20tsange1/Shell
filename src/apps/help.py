from application import Application


class Help(Application):
    """
    Prints the help message.
    """
    def execute(self, args=None, out=None) -> None:
        """
        Executes the help command
        """
        out.append(
    """
    Usage 🚀:

        <command> [<args>] : Run one of the available commands.
        > <file> : Redirect output to a file.
        >> <file> : Append output to a file.
        < <file> : Use a file as input.
        <command> | <command> : Pipe output from one command to another.
        <command> ; <command> : Run multiple commands sequentially.

    The following commands are available 🤖:

        pwd, cd, echo, ls, ls, cat, head, tail, grep, sort, cut, find, uniq, mkdir, touch, rm, rmdir, mv, cp, color, font, sed, wc, exit

    Use <command> --help or <command> -h for more information about a command.
    """ + "\n"
        )
