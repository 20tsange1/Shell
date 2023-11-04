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
        4,1,11,91,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,3,0,19,8,0,1,0,1,0,3,0,23,8,0,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,3,0,32,8,0,3,0,34,8,0,1,1,1,1,1,1,3,1,39,8,1,1,
        2,1,2,4,2,43,8,2,11,2,12,2,44,1,3,1,3,1,3,3,3,50,8,3,1,3,1,3,1,3,
        3,3,55,8,3,3,3,57,8,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,
        5,69,8,5,10,5,12,5,72,9,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,81,8,7,
        1,7,1,7,1,7,5,7,86,8,7,10,7,12,7,89,9,7,1,7,0,2,10,14,8,0,2,4,6,
        8,10,12,14,0,0,97,0,33,1,0,0,0,2,38,1,0,0,0,4,42,1,0,0,0,6,56,1,
        0,0,0,8,58,1,0,0,0,10,60,1,0,0,0,12,73,1,0,0,0,14,80,1,0,0,0,16,
        34,5,11,0,0,17,19,3,6,3,0,18,17,1,0,0,0,18,19,1,0,0,0,19,20,1,0,
        0,0,20,22,3,8,4,0,21,23,3,6,3,0,22,21,1,0,0,0,22,23,1,0,0,0,23,27,
        1,0,0,0,24,26,3,4,2,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,
        27,28,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,30,32,3,6,3,0,31,30,1,
        0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,16,1,0,0,0,33,18,1,0,0,0,34,
        1,1,0,0,0,35,39,5,9,0,0,36,39,5,10,0,0,37,39,3,12,6,0,38,35,1,0,
        0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,3,1,0,0,0,40,43,3,2,1,0,41,43,
        5,7,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,44,1,0,0,0,44,42,1,0,0,0,
        44,45,1,0,0,0,45,5,1,0,0,0,46,49,5,1,0,0,47,50,5,7,0,0,48,50,3,2,
        1,0,49,47,1,0,0,0,49,48,1,0,0,0,50,57,1,0,0,0,51,54,5,2,0,0,52,55,
        5,7,0,0,53,55,3,2,1,0,54,52,1,0,0,0,54,53,1,0,0,0,55,57,1,0,0,0,
        56,46,1,0,0,0,56,51,1,0,0,0,57,7,1,0,0,0,58,59,5,7,0,0,59,9,1,0,
        0,0,60,61,6,5,-1,0,61,62,3,0,0,0,62,63,5,3,0,0,63,64,3,0,0,0,64,
        70,1,0,0,0,65,66,10,1,0,0,66,67,5,3,0,0,67,69,3,14,7,0,68,65,1,0,
        0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,11,1,0,0,0,72,70,
        1,0,0,0,73,74,5,5,0,0,74,75,3,0,0,0,75,76,5,5,0,0,76,13,1,0,0,0,
        77,78,6,7,-1,0,78,81,3,10,5,0,79,81,3,0,0,0,80,77,1,0,0,0,80,79,
        1,0,0,0,81,87,1,0,0,0,82,83,10,3,0,0,83,84,5,4,0,0,84,86,3,14,7,
        4,85,82,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,15,
        1,0,0,0,89,87,1,0,0,0,14,18,22,27,31,33,38,42,44,49,54,56,70,80,
        87
    ]

class Comp0010ShellParser ( Parser ):

    grammarFileName = "Comp0010Shell.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "'|'", "';'", "'`'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "LEFT_ARROW", "RIGHT_ARROW", "PIPE", 
                      "SEMICOL", "BACKQUOTE", "DOUBLEQUOTE", "UNQUOTED", 
                      "WHITESPACE", "SINGLE_QUOTED", "DOUBLE_QUOTED", "NON_KEYWORD" ]

    RULE_call = 0
    RULE_quoted = 1
    RULE_argument = 2
    RULE_redirection = 3
    RULE_function = 4
    RULE_pipe = 5
    RULE_subcmd = 6
    RULE_command = 7

    ruleNames =  [ "call", "quoted", "argument", "redirection", "function", 
                   "pipe", "subcmd", "command" ]

    EOF = Token.EOF
    LEFT_ARROW=1
    RIGHT_ARROW=2
    PIPE=3
    SEMICOL=4
    BACKQUOTE=5
    DOUBLEQUOTE=6
    UNQUOTED=7
    WHITESPACE=8
    SINGLE_QUOTED=9
    DOUBLE_QUOTED=10
    NON_KEYWORD=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NON_KEYWORD(self):
            return self.getToken(Comp0010ShellParser.NON_KEYWORD, 0)

        def function(self):
            return self.getTypedRuleContext(Comp0010ShellParser.FunctionContext,0)


        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.RedirectionContext,i)


        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.ArgumentContext,i)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = Comp0010ShellParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(Comp0010ShellParser.NON_KEYWORD)
                pass
            elif token in [1, 2, 7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1 or _la==2:
                    self.state = 17
                    self.redirection()


                self.state = 20
                self.function()
                self.state = 22
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 21
                    self.redirection()


                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 24
                        self.argument() 
                    self.state = 29
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 31
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.redirection()


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

        def SINGLE_QUOTED(self):
            return self.getToken(Comp0010ShellParser.SINGLE_QUOTED, 0)

        def DOUBLE_QUOTED(self):
            return self.getToken(Comp0010ShellParser.DOUBLE_QUOTED, 0)

        def subcmd(self):
            return self.getTypedRuleContext(Comp0010ShellParser.SubcmdContext,0)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted" ):
                listener.enterQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted" ):
                listener.exitQuoted(self)




    def quoted(self):

        localctx = Comp0010ShellParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_quoted)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(Comp0010ShellParser.SINGLE_QUOTED)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(Comp0010ShellParser.DOUBLE_QUOTED)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.subcmd()
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




    def argument(self):

        localctx = Comp0010ShellParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 42
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [5, 9, 10]:
                        self.state = 40
                        self.quoted()
                        pass
                    elif token in [7]:
                        self.state = 41
                        self.match(Comp0010ShellParser.UNQUOTED)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 44 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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

        def LEFT_ARROW(self):
            return self.getToken(Comp0010ShellParser.LEFT_ARROW, 0)

        def UNQUOTED(self):
            return self.getToken(Comp0010ShellParser.UNQUOTED, 0)

        def quoted(self):
            return self.getTypedRuleContext(Comp0010ShellParser.QuotedContext,0)


        def RIGHT_ARROW(self):
            return self.getToken(Comp0010ShellParser.RIGHT_ARROW, 0)

        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_redirection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirection" ):
                listener.enterRedirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirection" ):
                listener.exitRedirection(self)




    def redirection(self):

        localctx = Comp0010ShellParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_redirection)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(Comp0010ShellParser.LEFT_ARROW)
                self.state = 49
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 47
                    self.match(Comp0010ShellParser.UNQUOTED)
                    pass
                elif token in [5, 9, 10]:
                    self.state = 48
                    self.quoted()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(Comp0010ShellParser.RIGHT_ARROW)
                self.state = 54
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 52
                    self.match(Comp0010ShellParser.UNQUOTED)
                    pass
                elif token in [5, 9, 10]:
                    self.state = 53
                    self.quoted()
                    pass
                else:
                    raise NoViableAltException(self)

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


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNQUOTED(self):
            return self.getToken(Comp0010ShellParser.UNQUOTED, 0)

        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = Comp0010ShellParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(Comp0010ShellParser.UNQUOTED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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


        def PIPE(self):
            return self.getToken(Comp0010ShellParser.PIPE, 0)

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



    def pipe(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Comp0010ShellParser.PipeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_pipe, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.call()
            self.state = 62
            self.match(Comp0010ShellParser.PIPE)
            self.state = 63
            self.call()
            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Comp0010ShellParser.PipeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_pipe)
                    self.state = 65
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 66
                    self.match(Comp0010ShellParser.PIPE)
                    self.state = 67
                    self.command(0) 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SubcmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACKQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(Comp0010ShellParser.BACKQUOTE)
            else:
                return self.getToken(Comp0010ShellParser.BACKQUOTE, i)

        def call(self):
            return self.getTypedRuleContext(Comp0010ShellParser.CallContext,0)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_subcmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubcmd" ):
                listener.enterSubcmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubcmd" ):
                listener.exitSubcmd(self)




    def subcmd(self):

        localctx = Comp0010ShellParser.SubcmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subcmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(Comp0010ShellParser.BACKQUOTE)
            self.state = 74
            self.call()
            self.state = 75
            self.match(Comp0010ShellParser.BACKQUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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


        def SEMICOL(self):
            return self.getToken(Comp0010ShellParser.SEMICOL, 0)

        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)



    def command(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Comp0010ShellParser.CommandContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_command, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 78
                self.pipe(0)
                pass

            elif la_ == 2:
                self.state = 79
                self.call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Comp0010ShellParser.CommandContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_command)
                    self.state = 82
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 83
                    self.match(Comp0010ShellParser.SEMICOL)
                    self.state = 84
                    self.command(4) 
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.pipe_sempred
        self._predicates[7] = self.command_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def pipe_sempred(self, localctx:PipeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def command_sempred(self, localctx:CommandContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




