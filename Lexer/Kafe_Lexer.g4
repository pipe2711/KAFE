lexer grammar Kafe_Lexer;

//TIPOS DE DATOS PRIMITIVOS Y OPERADORES (SEMILLAS)

    ID : [a-zA-Z]+;
    INT : [0-9]+;
    ADD : '+';
    SUB : '-';
    MUL : '*';
    DIV : '/';
    MOD : '%';


    //Comparacion

    EQUALS : '==';
    NOEQUAL : '!=';
    MEQ : '<' ;
    MAQ : '>' ;
    MEQI : '<=';
    MAQI : '>=';


    //Operaciones Logicas

    OR : '||';
    AND : '&&' ;
    NOT : '!'   ;

    //PARENTESIS, LLAVES, CORCHETES

    IPAREN : '(' ;
    DPAREN : ')' ;
    ILLAVE : '[' ;
    DLLAVE : ']' ;
    ICOR : '{' ;
    DCOR : '}' ;


    SEMICOLON   : ';';
    COMA    : ',';
    NEWLINE: ('\r' '\n'? | '\n');
    WS : [ \t]+ -> skip;

