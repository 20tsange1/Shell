# Generated from Comp0010Shell.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,69,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,1,2,
        1,3,1,3,1,4,1,4,1,5,1,5,1,6,4,6,37,8,6,11,6,12,6,38,1,7,4,7,42,8,
        7,11,7,12,7,43,1,7,1,7,1,8,1,8,4,8,50,8,8,11,8,12,8,51,3,8,54,8,
        8,1,8,1,8,1,9,1,9,4,9,60,8,9,11,9,12,9,61,3,9,64,8,9,1,9,1,9,1,10,
        1,10,0,0,11,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,
        1,0,5,8,0,10,10,32,32,34,34,39,39,59,60,62,62,96,96,124,124,2,0,
        9,9,32,32,2,0,10,10,39,39,2,0,10,10,34,34,7,0,10,10,13,13,34,34,
        39,39,59,59,96,96,124,124,74,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,1,0,0,0,3,25,1,0,0,0,5,
        27,1,0,0,0,7,29,1,0,0,0,9,31,1,0,0,0,11,33,1,0,0,0,13,36,1,0,0,0,
        15,41,1,0,0,0,17,47,1,0,0,0,19,57,1,0,0,0,21,67,1,0,0,0,23,24,5,
        60,0,0,24,2,1,0,0,0,25,26,5,62,0,0,26,4,1,0,0,0,27,28,5,124,0,0,
        28,6,1,0,0,0,29,30,5,59,0,0,30,8,1,0,0,0,31,32,5,96,0,0,32,10,1,
        0,0,0,33,34,5,34,0,0,34,12,1,0,0,0,35,37,8,0,0,0,36,35,1,0,0,0,37,
        38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,14,1,0,0,0,40,42,7,1,0,
        0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,45,
        1,0,0,0,45,46,6,7,0,0,46,16,1,0,0,0,47,53,5,39,0,0,48,50,8,2,0,0,
        49,48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,54,1,
        0,0,0,53,49,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,39,0,0,56,
        18,1,0,0,0,57,63,5,34,0,0,58,60,8,3,0,0,59,58,1,0,0,0,60,61,1,0,
        0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,59,1,0,0,0,63,64,
        1,0,0,0,64,65,1,0,0,0,65,66,5,34,0,0,66,20,1,0,0,0,67,68,8,4,0,0,
        68,22,1,0,0,0,7,0,38,43,51,53,61,63,1,6,0,0
    ]

class Comp0010ShellLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LEFT_ARROW = 1
    RIGHT_ARROW = 2
    PIPE = 3
    SEMICOL = 4
    BACKQUOTE = 5
    DOUBLEQUOTE = 6
    UNQUOTED = 7
    WHITESPACE = 8
    SINGLE_QUOTED = 9
    DOUBLE_QUOTED = 10
    NON_KEYWORD = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'|'", "';'", "'`'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "LEFT_ARROW", "RIGHT_ARROW", "PIPE", "SEMICOL", "BACKQUOTE", 
            "DOUBLEQUOTE", "UNQUOTED", "WHITESPACE", "SINGLE_QUOTED", "DOUBLE_QUOTED", 
            "NON_KEYWORD" ]

    ruleNames = [ "LEFT_ARROW", "RIGHT_ARROW", "PIPE", "SEMICOL", "BACKQUOTE", 
                  "DOUBLEQUOTE", "UNQUOTED", "WHITESPACE", "SINGLE_QUOTED", 
                  "DOUBLE_QUOTED", "NON_KEYWORD" ]

    grammarFileName = "Comp0010Shell.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


