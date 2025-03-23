grammar Kafe_Grammar.g4
import Kafe_Lexer.g4

program
    : (functionDecl | returnStmt | arrayDecl)+ EOF
    ;

// Declaracion de funcion
functionDecl
    : DRIP IDENT LPAREN RPAREN COLON END_LINE
    ;

// Sentencia return
returnStmt
    : RETURN LPAREN expr RPAREN END_LINE
    ;

// Declaracion arreglo
arrayDecl
    : type IDENT ASSIGN arrayValues END_LINE
    ;

// Lista de valores separados por coma 
arrayValues
    : expr (COMMA expr)*
    ;

// Expresion simple
expr
    : NUMBER
    | IDENT
    ;

// tipos 
type
    : INT_TYPE
    | FLOAT_TYPE
    | CHAR_TYPE
    | BOOL_TYPE
    ;
