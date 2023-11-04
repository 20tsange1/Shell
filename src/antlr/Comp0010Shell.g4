grammar Comp0010Shell;

//parser

call: NON_KEYWORD 
   | redirection? function redirection? argument* redirection?
   ;

quoted: SINGLE_QUOTED 
   | DOUBLE_QUOTED 
   | subcmd
   ;

argument: (quoted | UNQUOTED)+;

redirection: (LEFT_ARROW (UNQUOTED|quoted)) 
   | (RIGHT_ARROW (UNQUOTED|quoted))
   ;

function: UNQUOTED;

pipe: call PIPE call 
   | pipe PIPE command
   ;

subcmd: BACKQUOTE call BACKQUOTE;

command: command SEMICOL command
   | pipe 
   | call
   ;

// lexer 

LEFT_ARROW: '<';
RIGHT_ARROW: '>';
PIPE: '|';
SEMICOL: ';';
BACKQUOTE: '`';
DOUBLEQUOTE: '"';


UNQUOTED: ~[;'\n"`|<> ]+;

//needed to remove all whitespace from command
WHITESPACE: [ \t]+ -> skip;

SINGLE_QUOTED: '\'' (~[\n']+)? '\'';
DOUBLE_QUOTED: '"' (~[\n"]+)? '"';
NON_KEYWORD: ~[\r\n'"`|;];