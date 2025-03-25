lexer grammar Kafe_Lexer;

// TIPOS DE DATOS PRIMITIVOS
INT   : 'INT';
FLOAT : 'FLOAT';
BOOL  : 'BOOL';
CHAR  : 'CHAR';

// Valores primitivos
BOOLEAN : 'True' | 'False';
FLOAT_VALUE : [0-9]+ '.' [0-9]+;
INT_VALUE : [0-9]+;
CHAR_VALUE : '\'' . '\'';


// PALABRAS RESERVADAS PARA CONDICIONALES
IF : 'if';
ELSE : 'else';

// COMENTARIOS
LINE_COMMENT : '--' ~[\r\n]* -> skip;
BLOCK_COMMENT : '->' .*? '<-' -> skip;
