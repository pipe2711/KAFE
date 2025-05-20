lexer grammar Kafe_Lexer;

// Casting
INT_CAST    : 'int';
FLOAT_CAST  : 'float';
STR_CAST    : 'str';
BOOL_CAST   : 'bool';

// Palabras clave y funciones
DRIP        : 'drip';
POUR        : 'pour';
SHOW        : 'show';
RETURN      : 'return';
IF          : 'if';
ELIF        : 'elif';
ELSE        : 'else';
FUNC        : 'FUNC';
IMPORT      : 'import';

// Librerías
NUMK_LIB    : 'numk';
PLOT_LIB    : 'plot';
MATH_LIB    : 'math';

// Math Library Tokens (constantes con lookahead)
PI_CONST
    : 'pi' { self._input.LA(1)=='(' }?   // solo si viene '('
;
E_CONST
    : 'e'  { self._input.LA(1)=='(' }?   // solo si viene '('
;

// Funciones matemáticas
SIN         : 'sin';
COS         : 'cos';
TAN         : 'tan';
ASIN        : 'asin';
ACOS        : 'acos';
ATAN        : 'atan';
SINH        : 'sinh';
COSH        : 'cosh';
TANH        : 'tanh';
EXP         : 'exp';
LOG         : 'log';
SQRT        : 'sqrt';
POW_FUNC    : 'pow';
FACT        : 'factorial';
GCD         : 'gcd';
LCM         : 'lcm';
ABS         : 'abs';
FLOOR       : 'floor';
CEIL        : 'ceil';
ROUND       : 'round';
SUM         : 'sum';
PROD        : 'prod';
DEG         : 'degrees';
RAD         : 'radians';

// Operadores
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
ASSIGN      : '=';
NOT         : '!';

// Símbolos
LPAREN      : '(';
RPAREN      : ')';
LBRACK      : '[';
RBRACK      : ']';
DOT         : '.';
COLON       : ':';
SEMI        : ';';
COMMA       : ',';
PIPE        : '|';
ARROW       : '=>';

// Tipos
LIST        : 'List';
INT_TYPE    : 'INT';
FLOAT_TYPE  : 'FLOAT';
BOOL_TYPE   : 'BOOL';
VOID_TYPE   : 'VOID';
STRING_TYPE : 'STR';

// Literales
FLOAT       : [0-9]+ '.' [0-9]+;
INT         : [0-9]+;
BOOL        : 'True' | 'False';
STRING      : '"' (~["\\])* '"' | '\'' (~['\\])* '\'';

// Identificadores
ID          : [a-zA-Z_] [a-zA-Z0-9_]*;

// Comentarios
LINE_COMMENT  : '--' ~[\r\n]* -> skip;
BLOCK_COMMENT : '->' .*? '<-'       -> skip;

// Espacios
WS           : [ \t\r\n]+ -> skip;
