parser grammar Kafe_Grammar;
import Kafe_Lexer;

options { tokenVocab=NombreDelLexer; }

prog: (importStmt | stat)+;

importStmt: IMPORT STRING_VALUE NEWLINE;

declaracion: tipo ID ASSIGN (expr | arrayValues)
	| DRIP functionDeclaration
	;

stat: declaracion
    | condicion
    | returnStmt
    | pourStmt
    | showStmt
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
    | expr op=(ADD|SUB) expr
    | expr op=(MUL|DIV|MOD) expr
    | expr RAI expr
    | valor
    | pourStmt //pour
    ;

block
    : expr+ NEWLINE returnStmt
    ;

// Input/Output
pourStmt: POUR IPAREN (STRING_VALUE | ID) DPAREN;
showStmt: SHOW IPAREN expr DPAREN;

// Declaracion de funcion
functionDefinition
    : functionSignature (':' tipo) ASSIGN expr
    | functionSignature NEWLINE? ICOR block DCOR
    ;

functionDeclaration
    : functionSignature (':' tipo)
    ;

functionSignature
    : ID paramClauses
    ;

paramClauses
    : paramClause* (IPAREN params DPAREN)?
    ;

paramClause
    : IPAREN params? DPAREN
    ;

params
    : param (',' param)*
    ;

param
    : ID ':' paramType (ASSIGN expr)?
    ;

paramType
    : tipo
    | FLECHA_SUSHI tipo
    ;

// Sentencia return
returnStmt
    : RETURN IPAREN expr DPAREN
    ;

// Lista de valores separados por coma 
arrayValues
    : ILLAVE expr (',' expr)* DLLAVE
    | STRING_VALUE
    ;

tipo: INT | FLOAT | BOOL | CHAR;

valor: '-'? INT_VALUE
     | '-'? FLOAT_VALUE
     | BOOLEAN
     | CHAR_VALUE
     | STRING_VALUE
     | 'null'
     ;

condicion: IF IPAREN expr DPAREN ICOR stat* DCOR
         ( ELSE ICOR stat+ DCOR )?;
