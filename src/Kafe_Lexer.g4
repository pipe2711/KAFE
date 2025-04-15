lexer grammar Kafe_Lexer;

// Palabras clave y funciones
DRIP       : 'drip';
POUR       : 'pour';
SHOW       : 'show';
RETURN     : 'return';
IF         : 'if';
ELSE       : 'else';
MATCH      : 'match';
FUNC       : 'FUNC';
IMPORT     : 'import';

// Operadores
ADD        : '+';
SUB        : '-';
MUL        : '*';
DIV        : '/';
MOD        : '%';
POW        : '^';
AND        : '&&';
OR         : '||';
EQ         : '==';
NEQ        : '!=';
LT         : '<';
GT         : '>';
LE         : '<=';
GE         : '>=';
ARROW      : '=>';
ASSIGN     : '=';
NOT        : '!';

// Símbolos
LPAREN     : '(';
RPAREN     : ')';
LBRACK     : '[';
RBRACK     : ']';
COLON      : ':';
PIPE       : '|';
SEMI       : ';';
COMMA      : ',';
UNDERSCORE : '_';

// Tipos
LIST: 'List';
INT_TYPE   : 'INT';
FLOAT_TYPE : 'FLOAT';
CHAR_TYPE  : 'CHAR';
BOOL_TYPE  : 'BOOL';
VOID_TYPE  : 'VOID';

// Comentarios
LINE_COMMENT : '--' ~[\r\n]* -> skip;
BLOCK_COMMENT : '->' .*? '<-' -> skip;

// Literales
INT     : [0-9]+;
BOOL    : 'True' | 'False';
FLOAT   : [0-9]+ '.' [0-9]+;
CHAR    : '\'' . '\'';
STRING  : '"' .*? '"';

// Identificadores
ID      : [a-zA-Z_][a-zA-Z0-9_]*;

// Espacios
WS      : [ \t\r\n]+ -> skip;
