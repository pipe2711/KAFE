lexer grammar Kafe_Lexer;

ID : [a-zA-Z_][a-zA-Z0-9_]*;
ASSIGN : '=';

// Operaciones Aritmeticas
ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
MOD : '%';
RAI : '^';

// Comparacion
EQUALS : '==';
NOEQUAL : '!=';
MEQ : '<' ;
MAQ : '>' ;
MEQI : '<=';
MAQI : '>=';

// Operaciones Logicas
OR : '||';
AND : '&&';
NOT : '!';

// PARENTESIS, LLAVES, CORCHETES
IPAREN : '(';
DPAREN : ')';
ILLAVE : '[';
DLLAVE : ']';
ICOR : '{';
DCOR : '}';

FLECHA_SUSHI : '=>';

// Espacios en blanco o espacios
END_LINE   : ';';
NEWLINE: ('\r' '\n'? | '\n');
WS : [ \t]+ -> skip;

// Relacionado con funciones
DRIP       : 'drip';
RETURN     : 'return';
POUR       : 'pour';
SHOW       : 'show';

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

// Otros Valores
STRING_VALUE : '"' (~["\\] | ESCAPED_VALUE)* '"';
ESCAPED_VALUE: '\\' [\\'"];

// PALABRAS RESERVADAS PARA CONDICIONALES
IF : 'if';
ELSE : 'else';

// COMENTARIOS
LINE_COMMENT : '--' (~[\r\n])* -> skip;
BLOCK_COMMENT : '->' .*? '<-' -> skip;
