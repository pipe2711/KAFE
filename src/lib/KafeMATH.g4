// KafeMATH.g4  (parser grammar sin el bloque options)
parser grammar KafeMATH;

// Importa los tokens del lexer
import Kafe_Lexer;

mathLibrary
    : MATH_LIB DOT SIN        LPAREN expr RPAREN                 # sinFunction
    | MATH_LIB DOT COS        LPAREN expr RPAREN                 # cosFunction
    | MATH_LIB DOT TAN        LPAREN expr RPAREN                 # tanFunction
    | MATH_LIB DOT ASIN       LPAREN expr RPAREN                 # asinFunction
    | MATH_LIB DOT ACOS       LPAREN expr RPAREN                 # acosFunction
    | MATH_LIB DOT ATAN       LPAREN expr RPAREN                 # atanFunction
    | MATH_LIB DOT SINH       LPAREN expr RPAREN                 # sinhFunction
    | MATH_LIB DOT COSH       LPAREN expr RPAREN                 # coshFunction
    | MATH_LIB DOT TANH       LPAREN expr RPAREN                 # tanhFunction
    | MATH_LIB DOT EXP        LPAREN expr RPAREN                 # expFunction
    | MATH_LIB DOT LOG        LPAREN expr (COMMA expr)? RPAREN   # logFunction
    | MATH_LIB DOT SQRT       LPAREN expr RPAREN                 # sqrtFunction
    | MATH_LIB DOT POW_FUNC   LPAREN expr COMMA expr RPAREN      # powFunction
    | MATH_LIB DOT FACT       LPAREN expr RPAREN                 # factorialFunction
    | MATH_LIB DOT GCD        LPAREN expr (COMMA expr)+ RPAREN   # gcdFunction
    | MATH_LIB DOT LCM        LPAREN expr (COMMA expr)+ RPAREN   # lcmFunction
    | MATH_LIB DOT ABS        LPAREN expr RPAREN                 # absFunction
    | MATH_LIB DOT FLOOR      LPAREN expr RPAREN                 # floorFunction
    | MATH_LIB DOT CEIL       LPAREN expr RPAREN                 # ceilFunction
    | MATH_LIB DOT ROUND      LPAREN expr (COMMA expr)? RPAREN   # roundFunction
    | MATH_LIB DOT SUM        LPAREN expr COMMA expr RPAREN      # sumRangeFunction
    | MATH_LIB DOT PROD       LPAREN expr COMMA expr RPAREN      # prodRangeFunction
    | MATH_LIB DOT DEG        LPAREN expr RPAREN                 # degreesFunction
    | MATH_LIB DOT RAD        LPAREN expr RPAREN                 # radiansFunction
    | MATH_LIB DOT PI_CONST   LPAREN RPAREN                      # piFunction
    | MATH_LIB DOT E_CONST    LPAREN RPAREN                      # eFunction
    | MATH_LIB DOT PI_CONST                                      # piConstant
    | MATH_LIB DOT E_CONST                                       # eConstant
    ;
