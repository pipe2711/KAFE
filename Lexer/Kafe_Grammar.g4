grammar Kafe_Grammar;
import Kafe_Lexer;

prog: stat+;

declaracion: tipo ID ASSIGN (expr | arrayValues);

stat: declaracion END_LINE
    | condicion END_LINE
    | functionDecl END_LINE
    | returnStmt END_LINE
    | pourStmt END_LINE
    | showStmt END_LINE
    | NEWLINE
    ;

expr: expr EQUALS expr //Igual a
    | expr NOEQUAL expr //Diferente a
    | expr MEQ expr //menor que
    | expr MAQ expr //mayor que
    | expr MEQI expr //menor o igual que
    | expr MAQI expr //mayor o igual que
    | expr OR expr //o
    | expr AND expr //Y
    | NOT expr //Negar
    | expr RAI expr
    | expr op=(MUL|DIV|MOD) expr
    | expr op=(ADD|SUB) expr
    | valor
    | pourStmt //pour
    ;

// Input/Output
pourStmt: POUR IPAREN (STRING_VALUE | ID) DPAREN;
showStmt: SHOW IPAREN expr DPAREN;

// Declaracion de funcion
functionDecl
    : DRIP ID IPAREN DPAREN COLON
    ;

// Sentencia return
returnStmt
    : RETURN IPAREN expr DPAREN
    ;

// Lista de valores separados por coma 
arrayValues
    : ILLAVE expr (COMA expr)* DLLAVE
    | STRING_VALUE
    ;

tipo: INT | FLOAT | BOOL | CHAR;

valor: INT_VALUE
     | FLOAT_VALUE
     | BOOLEAN
     | CHAR_VALUE
     | STRING_VALUE
     ;

condicion: IF IPAREN expr DPAREN ICOR stat* DCOR
         ( ELSE ICOR stat+ DCOR )?;
