grammar Kafe_Grammar;
import Kafe_Lexer;

prog: stat+;

stat: declaracion SEMICOLON
    | condicion
    | NEWLINE
    ;

declaracion: tipo ID '=' valor;

tipo: INT | FLOAT | BOOL | CHAR;

valor: INT_VALUE
     | FLOAT_VALUE
     | BOOLEAN
     | CHAR_VALUE
     ;

condicion: IF IPAREN expr DPAREN ICOR stat* DCOR
         ( ELSE ICOR stat* DCOR )?;

expr: valor;
