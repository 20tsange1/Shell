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


    # Enter a parse tree produced by Comp0010ShellParser#bcommand.
    def enterBcommand(self, ctx:Comp0010ShellParser.BcommandContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#bcommand.
    def exitBcommand(self, ctx:Comp0010ShellParser.BcommandContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#bpipe.
    def enterBpipe(self, ctx:Comp0010ShellParser.BpipeContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#bpipe.
    def exitBpipe(self, ctx:Comp0010ShellParser.BpipeContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#bcall.
    def enterBcall(self, ctx:Comp0010ShellParser.BcallContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#bcall.
    def exitBcall(self, ctx:Comp0010ShellParser.BcallContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#batom.
    def enterBatom(self, ctx:Comp0010ShellParser.BatomContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#batom.
    def exitBatom(self, ctx:Comp0010ShellParser.BatomContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#bargument.
    def enterBargument(self, ctx:Comp0010ShellParser.BargumentContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#bargument.
    def exitBargument(self, ctx:Comp0010ShellParser.BargumentContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#bredirection.
    def enterBredirection(self, ctx:Comp0010ShellParser.BredirectionContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#bredirection.
    def exitBredirection(self, ctx:Comp0010ShellParser.BredirectionContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#bquoted.
    def enterBquoted(self, ctx:Comp0010ShellParser.BquotedContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#bquoted.
    def exitBquoted(self, ctx:Comp0010ShellParser.BquotedContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#bsinglequote.
    def enterBsinglequote(self, ctx:Comp0010ShellParser.BsinglequoteContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#bsinglequote.
    def exitBsinglequote(self, ctx:Comp0010ShellParser.BsinglequoteContext):
        pass


    # Enter a parse tree produced by Comp0010ShellParser#bdoublequote.
    def enterBdoublequote(self, ctx:Comp0010ShellParser.BdoublequoteContext):
        pass

    # Exit a parse tree produced by Comp0010ShellParser#bdoublequote.
    def exitBdoublequote(self, ctx:Comp0010ShellParser.BdoublequoteContext):
        pass



del Comp0010ShellParser