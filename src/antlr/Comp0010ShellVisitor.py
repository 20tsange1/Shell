# Generated from Comp0010Shell.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Comp0010ShellParser import Comp0010ShellParser
else:
    from Comp0010ShellParser import Comp0010ShellParser

# This class defines a complete generic visitor for a parse tree produced by Comp0010ShellParser.

class Comp0010ShellVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Comp0010ShellParser#command.
    def visitCommand(self, ctx:Comp0010ShellParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#pipe.
    def visitPipe(self, ctx:Comp0010ShellParser.PipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#call.
    def visitCall(self, ctx:Comp0010ShellParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#atom.
    def visitAtom(self, ctx:Comp0010ShellParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#argument.
    def visitArgument(self, ctx:Comp0010ShellParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#redirection.
    def visitRedirection(self, ctx:Comp0010ShellParser.RedirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#quoted.
    def visitQuoted(self, ctx:Comp0010ShellParser.QuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#singlequote.
    def visitSinglequote(self, ctx:Comp0010ShellParser.SinglequoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#backquote.
    def visitBackquote(self, ctx:Comp0010ShellParser.BackquoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#doublequote.
    def visitDoublequote(self, ctx:Comp0010ShellParser.DoublequoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#bcommand.
    def visitBcommand(self, ctx:Comp0010ShellParser.BcommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#bpipe.
    def visitBpipe(self, ctx:Comp0010ShellParser.BpipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#bcall.
    def visitBcall(self, ctx:Comp0010ShellParser.BcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#batom.
    def visitBatom(self, ctx:Comp0010ShellParser.BatomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#bargument.
    def visitBargument(self, ctx:Comp0010ShellParser.BargumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#bredirection.
    def visitBredirection(self, ctx:Comp0010ShellParser.BredirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#bquoted.
    def visitBquoted(self, ctx:Comp0010ShellParser.BquotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#bsinglequote.
    def visitBsinglequote(self, ctx:Comp0010ShellParser.BsinglequoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#bdoublequote.
    def visitBdoublequote(self, ctx:Comp0010ShellParser.BdoublequoteContext):
        return self.visitChildren(ctx)



del Comp0010ShellParser