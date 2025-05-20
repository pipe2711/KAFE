// KafeMATH.g4  – parser grammar
parser grammar KafeMATH;

import Kafe_Lexer;

mathLibrary
    // ───────── trigonometría ─────────
    : MATH_LIB DOT_SIN       LPAREN expr RPAREN               # sinFunction
    | MATH_LIB DOT_COS       LPAREN expr RPAREN               # cosFunction
    | MATH_LIB DOT_TAN       LPAREN expr RPAREN               # tanFunction
    | MATH_LIB DOT_ASIN      LPAREN expr RPAREN               # asinFunction
    | MATH_LIB DOT_ACOS      LPAREN expr RPAREN               # acosFunction
    | MATH_LIB DOT_ATAN      LPAREN expr RPAREN               # atanFunction
    | MATH_LIB DOT_SINH      LPAREN expr RPAREN               # sinhFunction
    | MATH_LIB DOT_COSH      LPAREN expr RPAREN               # coshFunction
    | MATH_LIB DOT_TANH      LPAREN expr RPAREN               # tanhFunction

    // ───────── exponenciales / logaritmos ─────────
    | MATH_LIB DOT_EXP       LPAREN expr RPAREN               # expFunction
    | MATH_LIB DOT_EXPM1     LPAREN expr RPAREN               # expm1Function
    | MATH_LIB DOT_EXP2      LPAREN expr RPAREN               # exp2Function
    | MATH_LIB DOT_LOG       LPAREN expr (COMMA expr)? RPAREN # logFunction
    | MATH_LIB DOT_LOG2      LPAREN expr RPAREN               # log2Function
    | MATH_LIB DOT_LOG10     LPAREN expr RPAREN               # log10Function
    | MATH_LIB DOT_CBRT      LPAREN expr RPAREN               # cbrtFunction
    | MATH_LIB DOT_SQRT      LPAREN expr RPAREN               # sqrtFunction
    | MATH_LIB DOT_POW       LPAREN expr COMMA expr RPAREN    # powFunction

    // ───────── teoría de números ─────────
    | MATH_LIB DOT_FACTORIAL LPAREN expr RPAREN               # factorialFunction
    | MATH_LIB DOT_COMB      LPAREN expr COMMA expr RPAREN    # combFunction
    | MATH_LIB DOT_PERM      LPAREN expr COMMA expr RPAREN    # permFunction
    | MATH_LIB DOT_GCD       LPAREN expr (COMMA expr)+ RPAREN # gcdFunction
    | MATH_LIB DOT_LCM       LPAREN expr (COMMA expr)+ RPAREN # lcmFunction

    // ───────── aritmética simple ─────────
    | MATH_LIB DOT_ABS       LPAREN expr RPAREN               # absFunction
    | MATH_LIB DOT_FLOOR     LPAREN expr RPAREN               # floorFunction
    | MATH_LIB DOT_CEIL      LPAREN expr RPAREN               # ceilFunction
    | MATH_LIB DOT_ROUND     LPAREN expr (COMMA expr)? RPAREN # roundFunction
    | MATH_LIB DOT_TRUNC     LPAREN expr RPAREN               # truncFunction
    | MATH_LIB DOT_FMOD      LPAREN expr COMMA expr RPAREN    # fmodFunction
    | MATH_LIB DOT_REMAINDER LPAREN expr COMMA expr RPAREN    # remainderFunction

    // ───────── manipulación de flotantes ─────────
    | MATH_LIB DOT_COPYSIGN  LPAREN expr COMMA expr RPAREN    # copysignFunction
    | MATH_LIB DOT_ISCLOSE   LPAREN expr COMMA expr RPAREN    # iscloseFunction
    | MATH_LIB DOT_ISFINITE  LPAREN expr RPAREN               # isfiniteFunction
    | MATH_LIB DOT_ISINF     LPAREN expr RPAREN               # isinfFunction
    | MATH_LIB DOT_ISNAN     LPAREN expr RPAREN               # isnanFunction
    | MATH_LIB DOT_ULP       LPAREN expr RPAREN               # ulpFunction

    // ───────── sumatorias / productos ─────────
    | MATH_LIB DOT_SUM       LPAREN expr RPAREN               # sumFunction
    | MATH_LIB DOT_PROD      LPAREN expr RPAREN               # prodFunction
    | MATH_LIB DOT_SUM       LPAREN expr COMMA expr RPAREN    # sumRangeFunction
    | MATH_LIB DOT_PROD      LPAREN expr COMMA expr RPAREN    # prodRangeFunction
    | MATH_LIB DOT_DIST      LPAREN expr COMMA expr RPAREN    # distFunction
    | MATH_LIB DOT_FSUM      LPAREN expr RPAREN               # fsumFunction
    | MATH_LIB DOT_HYPOT     LPAREN expr (COMMA expr)+ RPAREN # hypotFunction
    | MATH_LIB DOT_SUMPROD   LPAREN expr COMMA expr RPAREN    # sumprodFunction

    // ───────── funciones especiales ─────────
    | MATH_LIB DOT_ERF       LPAREN expr RPAREN               # erfFunction
    | MATH_LIB DOT_ERFC      LPAREN expr RPAREN               # erfcFunction
    | MATH_LIB DOT_GAMMA     LPAREN expr RPAREN               # gammaFunction
    | MATH_LIB DOT_LGAMMA    LPAREN expr RPAREN               # lgammaFunction

    // ───────── conversión angular ─────────
    | MATH_LIB DOT_DEGREES   LPAREN expr RPAREN               # degreesFunction
    | MATH_LIB DOT_RADIANS   LPAREN expr RPAREN               # radiansFunction

    // ───────── constantes ─────────
    | MATH_LIB DOT_PI        (LPAREN RPAREN)?                 # piValue
    | MATH_LIB DOT_E         (LPAREN RPAREN)?                 # eValue
    | MATH_LIB DOT_TAU                                        # tauConstant
    | MATH_LIB DOT_INF                                        # infConstant
    | MATH_LIB DOT_NAN                                        # nanConstant
    ;
