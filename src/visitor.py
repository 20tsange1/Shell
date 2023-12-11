import io
import re
from antlr4 import ParseTreeVisitor, InputStream, CommonTokenStream
from antlr.Comp0010ShellLexer import Comp0010ShellLexer
from antlr.Comp0010ShellParser import Comp0010ShellParser
from call import Call
from collections import deque
from error import ArgumentError
from glob import glob


class Visitor(ParseTreeVisitor):
    def __init__(self):
        # Application List, commands and arguments to be executed
        self.app_list = deque([])
        # Output array, for storing execution outputs to be passed to stdout
        self.output = deque([])
        self.input_io = []
        self.output_io = []

    # Visit a parse tree produced by Comp0010ShellParser#call.
    def visitCall(self, ctx: Comp0010ShellParser.CallContext, pipe=None):
        """
        Visits Call Node
            - Visits all children
            - Executes the commands and arguments left by children

        Parameters:
            ctx (CallContext): Call node context object
        """
        self.app_list.append([])
        self.output.append([])
        self.visitChildren(ctx)

        if pipe:
            pipe = io.StringIO("".join(pipe))

        Call(
            self.app_list.pop(),
            self.input_io,
            self.output_io,
            self.output,
            pipe,
        )

    def visitPipe(self, ctx: Comp0010ShellParser.PipeContext):
        """
        Visits Pipe Node

        Parameters:
            ctx (PipeContext): Pipe node context object
        """
        self.visit(ctx.getChild(0))
        self.visitCall(ctx.getChild(2), self.output.pop())

    def visitRedirection(self, ctx: Comp0010ShellParser.RedirectionContext):
        """
        Visits Redirection Node

        Parameters:
            ctx (RedirectionContext): Redirection node context object
        """
        index = 2
        if ctx.getChildCount() == 2:
            index = 1
        if ctx.getChild(0).getText() == "<":
            self.input_io.append(ctx.getChild(index).getText())
        else:
            self.output_io.append(ctx.getChild(index).getText())

    def visitArgument(self, ctx: Comp0010ShellParser.ArgumentContext):
        """
        Visits Argument Node

        Parameters:
            ctx (ArgumentContext): Argument node context object
        """
        children = ctx.getChildren()

        argument = [""]
        globbing = []

        for child in children:
            if isinstance(child, Comp0010ShellParser.QuotedContext):
                sub_arg = self.visit(child)
                if sub_arg:
                    argument[-1] += sub_arg.pop(0)
                    argument.extend(sub_arg)
            else:
                argument[-1] += child.getText()
                if "*" in child.getText():
                    globbing.append(len(argument) - 1)

        if globbing:
            globbing = list(set(globbing))
            for i in globbing:
                globbed = glob(argument[i])
                if globbed:
                    argument = argument[:i] + globbed + argument[i+1:]
                else:
                    raise ArgumentError(f"No matches found - {argument[i]}")

        self.app_list[-1].extend(argument)
        return

    def visitQuoted(self, ctx: Comp0010ShellParser.QuotedContext):
        """
        Visits Quoted Node

        Parameters:
            ctx (QuotedContext): Quoted node context object
        """

        def reparse(text, output):
            input_stream = InputStream(io.StringIO(text).read())
            lexer = Comp0010ShellLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = Comp0010ShellParser(stream)
            tree = parser.command()
            visitor = Visitor()
            visitor.visit(tree)
            for i in visitor.output:
                output.extend(i)

        quote = ctx.getText()

        if ctx.SINGLE_QUOTED():
            return [quote[1:-1]]

        elif ctx.DOUBLE_QUOTED():
            output = re.finditer('[^\\"`]+|`([^`]*)`', ctx.getText())
            quote = []
            for sub_string in output:
                if sub_string.group(1):
                    output = []
                    reparse(sub_string.group(1), output)
                    output = "".join(output).replace("\n", " ").rstrip()
                    quote.append(output)
                else:
                    quote.append(sub_string.group(0))
            return ["".join(quote)]

        else:
            output = []
            reparse(quote[1:-1], output)
            output = "".join(output).replace("\n", " ").rstrip().split(" ")
            while "" in output:
                output.remove("")
            return output
