# Generated from Comp0010Shell.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,129,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,3,0,24,8,0,1,0,1,0,1,0,5,0,
        29,8,0,10,0,12,0,32,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,42,8,
        1,10,1,12,1,45,9,1,1,2,3,2,48,8,2,1,2,1,2,3,2,52,8,2,5,2,54,8,2,
        10,2,12,2,57,9,2,1,2,1,2,3,2,61,8,2,1,2,5,2,64,8,2,10,2,12,2,67,
        9,2,1,2,3,2,70,8,2,1,3,1,3,3,3,74,8,3,1,4,1,4,4,4,78,8,4,11,4,12,
        4,79,1,5,1,5,3,5,84,8,5,1,5,1,5,1,5,3,5,89,8,5,1,5,3,5,92,8,5,1,
        6,1,6,1,6,3,6,97,8,6,1,7,1,7,1,7,1,7,1,7,5,7,104,8,7,10,7,12,7,107,
        9,7,1,7,1,7,1,8,1,8,3,8,113,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,5,9,
        122,8,9,10,9,12,9,125,9,9,1,9,1,9,1,9,0,2,0,2,10,0,2,4,6,8,10,12,
        14,16,18,0,0,144,0,23,1,0,0,0,2,33,1,0,0,0,4,47,1,0,0,0,6,73,1,0,
        0,0,8,77,1,0,0,0,10,91,1,0,0,0,12,96,1,0,0,0,14,98,1,0,0,0,16,110,
        1,0,0,0,18,116,1,0,0,0,20,21,6,0,-1,0,21,24,3,2,1,0,22,24,3,4,2,
        0,23,20,1,0,0,0,23,22,1,0,0,0,24,30,1,0,0,0,25,26,10,2,0,0,26,27,
        5,1,0,0,27,29,3,0,0,3,28,25,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,
        30,31,1,0,0,0,31,1,1,0,0,0,32,30,1,0,0,0,33,34,6,1,-1,0,34,35,3,
        4,2,0,35,36,5,2,0,0,36,37,3,4,2,0,37,43,1,0,0,0,38,39,10,1,0,0,39,
        40,5,2,0,0,40,42,3,0,0,0,41,38,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,
        0,43,44,1,0,0,0,44,3,1,0,0,0,45,43,1,0,0,0,46,48,5,9,0,0,47,46,1,
        0,0,0,47,48,1,0,0,0,48,55,1,0,0,0,49,51,3,10,5,0,50,52,5,9,0,0,51,
        50,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,49,1,0,0,0,54,57,1,0,0,
        0,55,53,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,65,
        3,8,4,0,59,61,5,9,0,0,60,59,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,
        62,64,3,6,3,0,63,60,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,
        0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,68,70,5,9,0,0,69,68,1,0,0,0,69,
        70,1,0,0,0,70,5,1,0,0,0,71,74,3,10,5,0,72,74,3,8,4,0,73,71,1,0,0,
        0,73,72,1,0,0,0,74,7,1,0,0,0,75,78,3,12,6,0,76,78,5,8,0,0,77,75,
        1,0,0,0,77,76,1,0,0,0,78,79,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,
        80,9,1,0,0,0,81,83,5,3,0,0,82,84,5,9,0,0,83,82,1,0,0,0,83,84,1,0,
        0,0,84,85,1,0,0,0,85,92,3,8,4,0,86,88,5,4,0,0,87,89,5,9,0,0,88,87,
        1,0,0,0,88,89,1,0,0,0,89,90,1,0,0,0,90,92,3,8,4,0,91,81,1,0,0,0,
        91,86,1,0,0,0,92,11,1,0,0,0,93,97,3,14,7,0,94,97,3,16,8,0,95,97,
        3,18,9,0,96,93,1,0,0,0,96,94,1,0,0,0,96,95,1,0,0,0,97,13,1,0,0,0,
        98,105,5,5,0,0,99,104,5,8,0,0,100,104,5,9,0,0,101,104,3,14,7,0,102,
        104,3,16,8,0,103,99,1,0,0,0,103,100,1,0,0,0,103,101,1,0,0,0,103,
        102,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,
        108,1,0,0,0,107,105,1,0,0,0,108,109,5,5,0,0,109,15,1,0,0,0,110,112,
        5,6,0,0,111,113,3,0,0,0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,
        1,0,0,0,114,115,5,6,0,0,115,17,1,0,0,0,116,123,5,7,0,0,117,122,5,
        8,0,0,118,122,5,9,0,0,119,122,3,18,9,0,120,122,3,16,8,0,121,117,
        1,0,0,0,121,118,1,0,0,0,121,119,1,0,0,0,121,120,1,0,0,0,122,125,
        1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,126,1,0,0,0,125,123,
        1,0,0,0,126,127,5,7,0,0,127,19,1,0,0,0,21,23,30,43,47,51,55,60,65,
        69,73,77,79,83,88,91,96,103,105,112,121,123
    ]

class Comp0010ShellParser ( Parser ):

    grammarFileName = "Comp0010Shell.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'|'", "'<'", "'>'", "'''", "'`'", 
                     "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "UNQUOTED", "WHITESPACE" ]

    RULE_command = 0
    RULE_pipe = 1
    RULE_call = 2
    RULE_atom = 3
    RULE_argument = 4
    RULE_redirection = 5
    RULE_quoted = 6
    RULE_singlequote = 7
    RULE_backquote = 8
    RULE_doublequote = 9

    ruleNames =  [ "command", "pipe", "call", "atom", "argument", "redirection", 
                   "quoted", "singlequote", "backquote", "doublequote" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    UNQUOTED=8
    WHITESPACE=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pipe(self):
            return self.getTypedRuleContext(Comp0010ShellParser.PipeContext,0)


        def call(self):
            return self.getTypedRuleContext(Comp0010ShellParser.CallContext,0)


        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.CommandContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.CommandContext,i)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)



    def command(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Comp0010ShellParser.CommandContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_command, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 21
                self.pipe(0)
                pass

            elif la_ == 2:
                self.state = 22
                self.call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Comp0010ShellParser.CommandContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_command)
                    self.state = 25
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 26
                    self.match(Comp0010ShellParser.T__0)
                    self.state = 27
                    self.command(3) 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.CallContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.CallContext,i)


        def pipe(self):
            return self.getTypedRuleContext(Comp0010ShellParser.PipeContext,0)


        def command(self):
            return self.getTypedRuleContext(Comp0010ShellParser.CommandContext,0)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_pipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipe" ):
                listener.enterPipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipe" ):
                listener.exitPipe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipe" ):
                return visitor.visitPipe(self)
            else:
                return visitor.visitChildren(self)



    def pipe(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Comp0010ShellParser.PipeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_pipe, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.call()
            self.state = 35
            self.match(Comp0010ShellParser.T__1)
            self.state = 36
            self.call()
            self._ctx.stop = self._input.LT(-1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Comp0010ShellParser.PipeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_pipe)
                    self.state = 38
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 39
                    self.match(Comp0010ShellParser.T__1)
                    self.state = 40
                    self.command(0) 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(Comp0010ShellParser.ArgumentContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(Comp0010ShellParser.WHITESPACE)
            else:
                return self.getToken(Comp0010ShellParser.WHITESPACE, i)

        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.RedirectionContext,i)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.AtomContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.AtomContext,i)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = Comp0010ShellParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 46
                self.match(Comp0010ShellParser.WHITESPACE)


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 49
                self.redirection()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 50
                    self.match(Comp0010ShellParser.WHITESPACE)


                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self.argument()
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==9:
                        self.state = 59
                        self.match(Comp0010ShellParser.WHITESPACE)


                    self.state = 62
                    self.atom() 
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 68
                self.match(Comp0010ShellParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def redirection(self):
            return self.getTypedRuleContext(Comp0010ShellParser.RedirectionContext,0)


        def argument(self):
            return self.getTypedRuleContext(Comp0010ShellParser.ArgumentContext,0)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = Comp0010ShellParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.redirection()
                pass
            elif token in [5, 6, 7, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.QuotedContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.QuotedContext,i)


        def UNQUOTED(self, i:int=None):
            if i is None:
                return self.getTokens(Comp0010ShellParser.UNQUOTED)
            else:
                return self.getToken(Comp0010ShellParser.UNQUOTED, i)

        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = Comp0010ShellParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 77
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [5, 6, 7]:
                        self.state = 75
                        self.quoted()
                        pass
                    elif token in [8]:
                        self.state = 76
                        self.match(Comp0010ShellParser.UNQUOTED)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 79 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(Comp0010ShellParser.ArgumentContext,0)


        def WHITESPACE(self):
            return self.getToken(Comp0010ShellParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_redirection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirection" ):
                listener.enterRedirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirection" ):
                listener.exitRedirection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirection" ):
                return visitor.visitRedirection(self)
            else:
                return visitor.visitChildren(self)




    def redirection(self):

        localctx = Comp0010ShellParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(Comp0010ShellParser.T__2)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 82
                    self.match(Comp0010ShellParser.WHITESPACE)


                self.state = 85
                self.argument()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(Comp0010ShellParser.T__3)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 87
                    self.match(Comp0010ShellParser.WHITESPACE)


                self.state = 90
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singlequote(self):
            return self.getTypedRuleContext(Comp0010ShellParser.SinglequoteContext,0)


        def backquote(self):
            return self.getTypedRuleContext(Comp0010ShellParser.BackquoteContext,0)


        def doublequote(self):
            return self.getTypedRuleContext(Comp0010ShellParser.DoublequoteContext,0)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted" ):
                listener.enterQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted" ):
                listener.exitQuoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuoted" ):
                return visitor.visitQuoted(self)
            else:
                return visitor.visitChildren(self)




    def quoted(self):

        localctx = Comp0010ShellParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_quoted)
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.singlequote()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.backquote()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.doublequote()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SinglequoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNQUOTED(self, i:int=None):
            if i is None:
                return self.getTokens(Comp0010ShellParser.UNQUOTED)
            else:
                return self.getToken(Comp0010ShellParser.UNQUOTED, i)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(Comp0010ShellParser.WHITESPACE)
            else:
                return self.getToken(Comp0010ShellParser.WHITESPACE, i)

        def singlequote(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.SinglequoteContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.SinglequoteContext,i)


        def backquote(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.BackquoteContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.BackquoteContext,i)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_singlequote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinglequote" ):
                listener.enterSinglequote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinglequote" ):
                listener.exitSinglequote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinglequote" ):
                return visitor.visitSinglequote(self)
            else:
                return visitor.visitChildren(self)




    def singlequote(self):

        localctx = Comp0010ShellParser.SinglequoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_singlequote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(Comp0010ShellParser.T__4)
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 103
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 99
                        self.match(Comp0010ShellParser.UNQUOTED)
                        pass
                    elif token in [9]:
                        self.state = 100
                        self.match(Comp0010ShellParser.WHITESPACE)
                        pass
                    elif token in [5]:
                        self.state = 101
                        self.singlequote()
                        pass
                    elif token in [6]:
                        self.state = 102
                        self.backquote()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 108
            self.match(Comp0010ShellParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BackquoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(Comp0010ShellParser.CommandContext,0)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_backquote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackquote" ):
                listener.enterBackquote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackquote" ):
                listener.exitBackquote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBackquote" ):
                return visitor.visitBackquote(self)
            else:
                return visitor.visitChildren(self)




    def backquote(self):

        localctx = Comp0010ShellParser.BackquoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_backquote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(Comp0010ShellParser.T__5)
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 111
                self.command(0)


            self.state = 114
            self.match(Comp0010ShellParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoublequoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNQUOTED(self, i:int=None):
            if i is None:
                return self.getTokens(Comp0010ShellParser.UNQUOTED)
            else:
                return self.getToken(Comp0010ShellParser.UNQUOTED, i)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(Comp0010ShellParser.WHITESPACE)
            else:
                return self.getToken(Comp0010ShellParser.WHITESPACE, i)

        def doublequote(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.DoublequoteContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.DoublequoteContext,i)


        def backquote(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.BackquoteContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.BackquoteContext,i)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_doublequote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoublequote" ):
                listener.enterDoublequote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoublequote" ):
                listener.exitDoublequote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoublequote" ):
                return visitor.visitDoublequote(self)
            else:
                return visitor.visitChildren(self)




    def doublequote(self):

        localctx = Comp0010ShellParser.DoublequoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_doublequote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(Comp0010ShellParser.T__6)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 121
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 117
                        self.match(Comp0010ShellParser.UNQUOTED)
                        pass
                    elif token in [9]:
                        self.state = 118
                        self.match(Comp0010ShellParser.WHITESPACE)
                        pass
                    elif token in [7]:
                        self.state = 119
                        self.doublequote()
                        pass
                    elif token in [6]:
                        self.state = 120
                        self.backquote()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 126
            self.match(Comp0010ShellParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.command_sempred
        self._predicates[1] = self.pipe_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def command_sempred(self, localctx:CommandContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def pipe_sempred(self, localctx:PipeContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         