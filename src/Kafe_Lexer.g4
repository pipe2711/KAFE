lexer grammar Kafe_Lexer;

///////////////////////////////////////////////////////////////////////////
//  Casting
///////////////////////////////////////////////////////////////////////////
INT_CAST  : 'int';
FLOAT_CAST: 'float';
STR_CAST  : 'str';
BOOL_CAST : 'bool';

///////////////////////////////////////////////////////////////////////////
//  Palabras clave
///////////////////////////////////////////////////////////////////////////
DRIP   : 'drip';
POUR   : 'pour';
SHOW   : 'show';
RETURN : 'return';
IF     : 'if';
ELIF   : 'elif';
ELSE   : 'else';
FUNC   : 'FUNC';
IMPORT : 'import';

///////////////////////////////////////////////////////////////////////////
//  Librerías
///////////////////////////////////////////////////////////////////////////
NUMK_LIB : 'numk';
PLOT_LIB : 'plot';
MATH_LIB : 'math';

///////////////////////////////////////////////////////////////////////////
//  Constantes y funciones de la librería math  ( SIEMPRE con “.” )
///////////////////////////////////////////////////////////////////////////
// --- constantes ---
DOT_PI      : '.pi';
DOT_E       : '.e';
DOT_TAU     : '.tau';
DOT_INF     : '.inf';
DOT_NAN     : '.nan';

// --- trigonometría ---
DOT_SIN     : '.sin';
DOT_COS     : '.cos';
DOT_TAN     : '.tan';
DOT_ASIN    : '.asin';
DOT_ACOS    : '.acos';
DOT_ATAN    : '.atan';
DOT_SINH    : '.sinh';
DOT_COSH    : '.cosh';
DOT_TANH    : '.tanh';

// --- exponenciales / logaritmos ---
DOT_EXP     : '.exp';
DOT_EXPM1   : '.expm1';
DOT_EXP2    : '.exp2';
DOT_LOG     : '.log';
DOT_LOG2    : '.log2';
DOT_LOG10   : '.log10';
DOT_CBRT    : '.cbrt';
DOT_SQRT    : '.sqrt';
DOT_POW     : '.pow';

// --- teoría de números ---
DOT_FACTORIAL : '.factorial';
DOT_GCD       : '.gcd';
DOT_LCM       : '.lcm';
DOT_COMB      : '.comb';
DOT_PERM      : '.perm';

// --- aritmética flotante básica ---
DOT_ABS       : '.abs';
DOT_FLOOR     : '.floor';
DOT_CEIL      : '.ceil';
DOT_ROUND     : '.round';
DOT_TRUNC     : '.trunc';
DOT_FMOD      : '.fmod';
DOT_REMAINDER : '.remainder';

// --- manipulación flotante ---
DOT_COPYSIGN  : '.copysign';
DOT_ISCLOSE   : '.isclose';
DOT_ISFINITE  : '.isfinite';
DOT_ISINF     : '.isinf';
DOT_ISNAN     : '.isnan';
DOT_ULP       : '.ulp';

// --- sumatorias y productos ---
DOT_SUM       : '.sum';
DOT_PROD      : '.prod';
DOT_DIST      : '.dist';
DOT_FSUM      : '.fsum';
DOT_HYPOT     : '.hypot';
DOT_SUMPROD   : '.sumprod';

// --- funciones especiales ---
DOT_ERF       : '.erf';
DOT_ERFC      : '.erfc';
DOT_GAMMA     : '.gamma';
DOT_LGAMMA    : '.lgamma';

// --- conversión angular ---
DOT_DEGREES   : '.degrees';
DOT_RADIANS   : '.radians';


//  Operadores

ADD   : '+';
SUB   : '-';
MUL   : '*';
DIV   : '/';
MOD   : '%';
POW   : '^';
AND   : '&&';
OR    : '||';
EQ    : '==';
NEQ   : '!=';
LT    : '<';
GT    : '>';
LE    : '<=';
GE    : '>=';
ASSIGN: '=';
NOT   : '!';


//  Símbolos

LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
DOT   : '.';               // ¡Después de todos los DOT_*!
COLON : ':';
SEMI  : ';';
COMMA : ',';
PIPE  : '|';
ARROW : '=>';


//  Tipos

LIST       : 'List';
INT_TYPE   : 'INT';
FLOAT_TYPE : 'FLOAT';
BOOL_TYPE  : 'BOOL';
VOID_TYPE  : 'VOID';
STRING_TYPE: 'STR';

FLOAT : [0-9]+ '.' [0-9]+;
INT   : [0-9]+;
BOOL  : 'True' | 'False';
STRING: '"' (~["\\])* '"' | '\'' (~['\\])* '\'';


ID : [a-zA-Z_] [a-zA-Z0-9_]*;


BLOCK_COMMENT: '->' .*? '<-'         -> skip;
WS           : [ \t\r\n]+            -> skip;
