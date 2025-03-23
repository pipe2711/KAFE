lexer grammar kafe_Lexer;

DRIP       : 'drip';
RETURN     : 'return';
LPAREN     : '(';
RPAREN     : ')';
COLON      : ':';
ASSIGN     : '=';
COMMA      : ',';
END_LINE   : '$';

INT_TYPE   : 'INT';
FLOAT_TYPE : 'FLOAT';
CHAR_TYPE  : 'CHAR';
BOOL_TYPE  : 'BOOL';

NUMBER     : [0-9]+;
IDENT      : [a-zA-Z_][a-zA-Z0-9_]*;

WS         : [ \t\r\n]+ -> skip;
