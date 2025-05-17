grammar KafeMATH;

mathLibrary: 'math.sin' '(' expr ')' #sinFunction;

// Integración en primaryExpr: mathLibraryExpr
mathLibrary
    : SIN LPAREN expr RPAREN               # sinFunction
    | COS LPAREN expr RPAREN               # cosFunction
    | TAN LPAREN expr RPAREN               # tanFunction
    | ASIN LPAREN expr RPAREN              # asinFunction
    | ACOS LPAREN expr RPAREN              # acosFunction
    | ATAN LPAREN expr RPAREN              # atanFunction
    | SINH LPAREN expr RPAREN              # sinhFunction
    | COSH LPAREN expr RPAREN              # coshFunction
    | TANH LPAREN expr RPAREN              # tanhFunction
    | EXP LPAREN expr RPAREN               # expFunction
    | LOG LPAREN expr (COMMA expr)? RPAREN # logFunction
    | SQRT LPAREN expr RPAREN              # sqrtFunction
    | POW LPAREN expr COMMA expr RPAREN    # powFunction
    | FACT LPAREN expr RPAREN              # factorialFunction
    | GCD LPAREN expr COMMA expr RPAREN    # gcdFunction
    | LCM LPAREN expr COMMA expr RPAREN    # lcmFunction
    | ABS LPAREN expr RPAREN               # absFunction
    | FLOOR LPAREN expr RPAREN             # floorFunction
    | CEIL LPAREN expr RPAREN              # ceilFunction
    | ROUND LPAREN expr (COMMA expr)? RPAREN # roundFunction
    | SUM LPAREN expr COMMA expr RPAREN    # sumRangeFunction
    | PROD LPAREN expr COMMA expr RPAREN   # prodRangeFunction
    | DEG LPAREN expr RPAREN               # degreesFunction
    | RAD LPAREN expr RPAREN               # radiansFunction
    | PI                                   # piConstant
    | E                                    # eConstant
    ;

SIN     : 'sin';
COS     : 'cos';
TAN     : 'tan';
ASIN    : 'asin';
ACOS    : 'acos';
ATAN    : 'atan';
SINH    : 'sinh';
COSH    : 'cosh';
TANH    : 'tanh';
EXP     : 'exp';
LOG     : 'log';
SQRT    : 'sqrt';
POW     : 'pow';
FACT    : 'factorial';
GCD     : 'gcd';
LCM     : 'lcm';
ABS     : 'abs';
FLOOR   : 'floor';
CEIL    : 'ceil';
ROUND   : 'round';
SUM     : 'sum';
PROD    : 'prod';
DEG     : 'degrees';
RAD     : 'radians';
PI      : 'pi';
E       : 'e';

WS      : [ \t\r\n]+ -> skip;
