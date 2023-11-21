# Generated from Comp0010Shell.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Comp0010ShellParser import Comp0010ShellParser
else:
    from Comp0010ShellParser import Comp0010ShellParser

# This class defines a complete listener for a parse tree produced by Comp0010ShellParser.
class Comp0010ShellListener(ParseTreeListener):

    # Enter a parse tree produced by Comp0010ShellParser#command.
    def enterCommand(self, ctx:Comp0010ShellParser.CommandContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#command.
    def exitCommand(self, ctx:Comp0010ShellParser.CommandContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#pipe.
    def enterPipe(self, ctx:Comp0010ShellParser.PipeContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#pipe.
    def exitPipe(self, ctx:Comp0010ShellParser.PipeContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#call.
    def enterCall(self, ctx:Comp0010ShellParser.CallContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#call.
    def exitCall(self, ctx:Comp0010ShellParser.CallContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#atom.
    def enterAtom(self, ctx:Comp0010ShellParser.AtomContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#atom.
    def exitAtom(self, ctx:Comp0010ShellParser.AtomContext):
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


    # Enter a parse tree produced by Comp0010ShellParser#quoted.
    def enterQuoted(self, ctx:Comp0010ShellParser.QuotedContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#quoted.
    def exitQuoted(self, ctx:Comp0010ShellParser.QuotedContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#singlequote.
    def enterSinglequote(self, ctx:Comp0010ShellParser.SinglequoteContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#singlequote.
    def exitSinglequote(self, ctx:Comp0010ShellParser.SinglequoteContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#backquote.
    def enterBackquote(self, ctx:Comp0010ShellParser.BackquoteContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#backquote.
    def exitBackquote(self, ctx:Comp0010ShellParser.BackquoteContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#doublequote.
    def enterDoublequote(self, ctx:Comp0010ShellParser.DoublequoteContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#doublequote.
    def exitDoublequote(self, ctx:Comp0010ShellParser.DoublequoteContext):
        pass



del Comp0010ShellParser