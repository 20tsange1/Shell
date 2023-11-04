# Generated from Comp0010Shell.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Comp0010ShellParser import Comp0010ShellParser
else:
    from Comp0010ShellParser import Comp0010ShellParser

# This class defines a complete listener for a parse tree produced by Comp0010ShellParser.
class Comp0010ShellListener(ParseTreeListener):

    # Enter a parse tree produced by Comp0010ShellParser#call.
    def enterCall(self, ctx:Comp0010ShellParser.CallContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#call.
    def exitCall(self, ctx:Comp0010ShellParser.CallContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#quoted.
    def enterQuoted(self, ctx:Comp0010ShellParser.QuotedContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#quoted.
    def exitQuoted(self, ctx:Comp0010ShellParser.QuotedContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#argument.
    def enterArgument(self, ctx:Comp0010ShellParser.ArgumentContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#argument.
    def exitArgument(self, ctx:Comp0010ShellParser.ArgumentContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#redirection.
    def enterRedirection(self, ctx:Comp0010ShellParser.RedirectionContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#redirection.
    def exitRedirection(self, ctx:Comp0010ShellParser.RedirectionContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#function.
    def enterFunction(self, ctx:Comp0010ShellParser.FunctionContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#function.
    def exitFunction(self, ctx:Comp0010ShellParser.FunctionContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#pipe.
    def enterPipe(self, ctx:Comp0010ShellParser.PipeContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#pipe.
    def exitPipe(self, ctx:Comp0010ShellParser.PipeContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#subcmd.
    def enterSubcmd(self, ctx:Comp0010ShellParser.SubcmdContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#subcmd.
    def exitSubcmd(self, ctx:Comp0010ShellParser.SubcmdContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#command.
    def enterCommand(self, ctx:Comp0010ShellParser.CommandContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#command.
    def exitCommand(self, ctx:Comp0010ShellParser.CommandContext):
        pass



del Comp0010ShellParser