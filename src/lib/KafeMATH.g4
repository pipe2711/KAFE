parser grammar KafeMATH;

import Kafe_Lexer;

mathLibrary
    // Función genérica: math.<name>( argumentos... ) con 0 o más args
    : MATH_LIB '.' ID LPAREN ( expr ( COMMA expr )* )? RPAREN    # mathFunctionCall
    // Constante simple: math.<name>
    | MATH_LIB '.' ID                                            # mathConstant
    ;
