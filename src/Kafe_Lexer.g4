lexer grammar Kafe_Lexer;

//  Casting
INT_CAST    : 'int';
FLOAT_CAST  : 'float';
STR_CAST    : 'str';
BOOL_CAST   : 'bool';


//  Palabras clave y funciones
DRIP        : 'drip';
POUR        : 'pour';
SHOW        : 'show';
RETURN      : 'return';
IF          : 'if';
ELIF        : 'elif';
ELSE        : 'else';
MATCH       : 'match';
FUNC        : 'FUNC';
RANGE      :  'range';
IMPORT      : 'import';


//  Operadores
ADD         : '+';
SUB         : '-';
MUL         : '*';
DIV         : '/';
MOD         : '%';
POW         : '^';
AND         : '&&';
OR          : '||';
EQ          : '==';
NEQ         : '!=';
LT          : '<';
GT          : '>';
LE          : '<=';
GE          : '>=';
ARROW       : '=>';
ASSIGN      : '=';
NOT         : '!';


//  Símbolos de agrupación y separación
LPAREN      : '(';
RPAREN      : ')';
LBRACK      : '[';
RBRACK      : ']';
COLON       : ':';
PIPE        : '|';
SEMI        : ';';
COMMA       : ',';
UNDERSCORE  : '_';


//  Tipos básicos
LIST        : 'List';
INT_TYPE    : 'INT';
FLOAT_TYPE  : 'FLOAT';
BOOL_TYPE   : 'BOOL';
VOID_TYPE   : 'VOID';
STRING_TYPE : 'STR';


//  Literales
INT         : [0-9]+;
BOOL        : 'True' | 'False';
FLOAT       : [0-9]+ '.' [0-9]+;
STRING      : '"' (~["\\])* '"' | '\'' (~['\\])* '\'';


//  Identificadores
ID          : [a-zA-Z_] [a-zA-Z0-9_]*;


//  Comentarios y espacios en blanco
LINE_COMMENT  : '--' ~[\r\n]*        -> skip;
BLOCK_COMMENT : '->' .*? '<-'        -> skip;
WS            : [ \t\r\n]+           -> skip;
