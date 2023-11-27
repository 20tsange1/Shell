grammar Comp0010Shell;

command: pipe | command ';' command | call;
pipe: call '|' call | pipe '|' command;


call: WHITESPACE? (redirection WHITESPACE?)* argument (WHITESPACE? atom)* WHITESPACE?;
atom: redirection | argument;
argument: (quoted | UNQUOTED)+;
redirection: '<' WHITESPACE? argument | '>' WHITESPACE? argument;


UNQUOTED: ~[ \t\n'"`|;<>]+;

quoted: singlequote | backquote | doublequote;
singlequote: '\''(UNQUOTED | WHITESPACE | backquote | '"' |'`' | '|' | ';' | '<' | '>' | '\n')*'\'';
backquote: '`'bcommand?'`';
doublequote: '"'(UNQUOTED | WHITESPACE | backquote | '\'' |'`' | '|' | ';' | '<' | '>' | '\n')*'"';


bcommand: bpipe | bcommand ';' bcommand | bcall;
bpipe: bcall '|' bcall | bpipe '|' bcommand;


bcall: WHITESPACE? (bredirection WHITESPACE?)* bargument (WHITESPACE? batom)* WHITESPACE?;
batom: bredirection | bargument;
bargument: (bquoted | UNQUOTED)+;
bredirection: '<' WHITESPACE? bargument | '>' WHITESPACE? bargument;


bquoted: bsinglequote | bdoublequote;
bsinglequote: '\''(UNQUOTED | WHITESPACE)*'\'';
bdoublequote: '"'(UNQUOTED | WHITESPACE)*'"';

WHITESPACE: [ \t]+;