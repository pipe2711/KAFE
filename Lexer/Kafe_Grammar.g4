grammar Kafe_Grammar;

import Kafe_Lexer;

program : importStmt* stmt* ;

importStmt : IMPORT ID SEMI ;

stmt
    : varDecl SEMI
    | assignStmt SEMI
    | functionDecl
    | ifElseExpr
    | whileLoop
    | forLoop
    | returnStmt SEMI
    | showStmt SEMI
    | pourStmt SEMI
    | matchExpr
    ;

varDecl : typeDecl ID ASSIGN expr ;
assignStmt : ID ASSIGN expr ;

functionDecl
    : DRIP ID '(' paramList? ')' ('(' paramList ')')* COLON block SEMI
    ;

paramList : paramDecl (COMMA paramDecl)* ;
paramDecl : ID COLON typeDecl | ID COLON FUNC '(' paramList? ')' COLON typeDecl ;

returnStmt : RETURN expr ;
showStmt : SHOW '(' expr ')' ;
pourStmt : POUR '(' expr ')' ;

ifElseExpr
    : IF '(' expr ')' COLON block (PIPE '(' expr ')' COLON block)* (ELSE COLON block)? SEMI
    ;

whileLoop : 'while' '(' expr ')' COLON block SEMI ;
forLoop : 'for' '(' ID 'in' expr ')' COLON block SEMI ;

matchExpr : MATCH expr COLON matchCase+ SEMI ;
matchCase : PIPE pattern ARROW expr ;
pattern : literal | UNDERSCORE | ID ;

block : stmt* ;

expr
    : expr POW expr
    | expr MUL expr
    | expr DIV expr
    | expr MOD expr
    | expr ADD expr
    | expr SUB expr
    | expr LT expr
    | expr GT expr
    | expr LE expr
    | expr GE expr
    | expr EQ expr
    | expr NEQ expr
    | expr AND expr
    | expr OR expr
    | lambdaExpr
    | '(' expr ')'
    | literal
    | ID
    | functionCall
    ;

functionCall : ID '(' argList? ')' ;
argList : arg (COMMA arg)* ;
arg : expr | lambdaExpr ;

lambdaExpr : '(' paramDecl ')' ARROW expr ;

literal
    : INT
    | FLOAT
    | CHAR
    | STRING
    | TRUE
    | FALSE
    ;

typeDecl
    : INT_TYPE
    | FLOAT_TYPE
    | CHAR_TYPE
    | BOOL_TYPE
    | VOID_TYPE
    ;

