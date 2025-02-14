lexer grammar Kafe_Lexer;

//Estructura y definicion de TOKENS

    ID : [a-zA-Z]+;
    INT : [0-9]+;
    ADD : '+';
    SUB : '-';
    MUL : '*';
    DIV : '/';
    //ws  : [\t\r\n]+ -> skip; 