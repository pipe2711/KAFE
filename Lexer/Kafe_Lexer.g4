lexer grammar Kafe_Lexer;

//Estructura y definicion de TOKENS
    //Simbolos matematicos

    ID : [a-zA-Z]+;
    INT : [0-9]+;
    ADD : '+';
    SUB : '-';
    MUL : '*';
    DIV : '/';
    MOD : '%';
    SIN : 'sin';
    COS :  'cos';
    TAN : 'tan';
    RAI : '^';

    //Comparacion

    EQUALS : '=';
    NOEQUAL : '!=';
    MEQ : '<' ;
    MAQ : '>' ;
    MEQI : '<=';
    MAQI : '>=';


    //Operaciones Logicas

    OR : '|';
    AND : '&&' ;
    NOT : '!'   ;

    //PARENTESIS, LLAVES, CORCHETES

    IPAREN : '(' ;
    DPAREN : ')' ;
    ILLAVE : '[' ;
    DLLAVE : ']' ;
    ICOR : '{' ;
    DCOR : '}' ;


    //Espacios en blanco o espacios
    SEMICOLON   : ';';
    COMA    : ',';
    NEWLINE: ('\r' '\n'? | '\n');
    WS : [ \t]+ -> skip;

