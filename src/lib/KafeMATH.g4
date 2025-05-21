// KafeMATH.g4  – parser grammar for all math.<name> usages
parser grammar KafeMATH;

import Kafe_Lexer;

mathLibrary
    // Función genérica: math.<name>( argumentos... ) con 0 o más args
    : MATH_LIB DOT ID LPAREN ( expr ( COMMA expr )* )? RPAREN    # mathFunctionCall
    // Constante simple: math.<name>
    | MATH_LIB DOT ID                                           # mathConstant
    ;
