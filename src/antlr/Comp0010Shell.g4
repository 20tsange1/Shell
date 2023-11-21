grammar Comp0010Shell;

command: pipe | command ';' command | call;
pipe: call '|' call | pipe '|' command;


call: WHITESPACE? (redirection WHITESPACE?)* argument (WHITESPACE? atom)* WHITESPACE?;
atom: redirection | argument;
argument: (quoted | UNQUOTED)+;
redirection: '<' WHITESPACE? argument | '>' WHITESPACE? argument;


UNQUOTED: ~[ \t\n'"`|;<>]+;
quoted: singlequote | backquote | doublequote;
singlequote: '\''(UNQUOTED | WHITESPACE | singlequote | backquote)*'\'';
backquote: '`'command?'`';
doublequote: '"'(UNQUOTED | WHITESPACE | doublequote | backquote)*'"';
WHITESPACE: [ \t]+;