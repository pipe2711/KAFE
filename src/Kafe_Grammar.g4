grammar Kafe_Grammar;

import Kafe_Lexer;

program
    : (simpleImport SEMI)* (stmt SEMI)*
    ;

simpleImport: IMPORT ID;

stmt
    : varDecl
    | assignStmt
    | indexedAssignStmt
    | functionDecl
    | ifElseExpr
    | whileLoop
    | forLoop
    | returnStmt
    | showStmt
    | expr
    ;

block
    : (stmt SEMI)*
    ;

// ======================  LIBRERÍAS ======================
library
    : ID '.' ID LPAREN ( expr ( COMMA expr )* )? RPAREN    # libraryFunctionCall
    | ID '.' ID                                            # libraryConstant
    ;

// ======================  VARIABLES ======================
varDecl
    : typeDecl ID (ASSIGN expr)?
    ;

assignStmt
    : ID ASSIGN expr
    ;

indexedAssignStmt
    : ID indexing ASSIGN expr
    ;

indexing
    : (LBRACK expr RBRACK)+
    ;

// ======================  FUNCIONES ======================
functionDecl
    : DRIP ID LPAREN paramList? RPAREN (LPAREN paramList RPAREN)* ARROW typeDecl COLON block
    ;

paramList
    : paramDecl (COMMA paramDecl)*
    ;
paramDecl : ID COLON typeDecl   # simpleParam;

functionParam: FUNC LPAREN paramList_typeDecl? RPAREN ARROW typeDecl;
paramList_typeDecl : typeDecl (COMMA typeDecl)*;

 // Llamadas currificables:   f(args) (args)*
functionCall
    : ID LPAREN argList? RPAREN (LPAREN argList? RPAREN)*
    ;

argList
    : arg (COMMA arg)*
    ;

arg
    : expr        # exprArgument
    | lambdaExpr  # lambdaArgument
    ;

lambdaExpr
    : LPAREN paramDecl RPAREN ARROW expr
    ;

returnStmt
    : RETURN expr
    ;

showStmt
    : SHOW LPAREN expr RPAREN
    ;
pourStmt
    : POUR LPAREN expr RPAREN
    ;
appendCall: APPEND '(' expr ',' expr ')' ;
removeCall: REMOVE '(' expr ',' expr ')' ;
lenCall: LEN '(' expr ')' ;


// ======================  CONDICIONALES ======================
ifElseExpr
    : IF LPAREN expr RPAREN COLON block (elifBranch)* (ELSE COLON block)?
    ;
elifBranch
    : ELIF LPAREN expr RPAREN COLON block
    ;

// ======================  BUCLES ======================
whileLoop
    : 'while' LPAREN expr RPAREN COLON block
    ;
forLoop
    : 'for' LPAREN ID 'in' expr RPAREN COLON block
    ;

// ======================  EXPRESIONES ======================
expr
    : logicExpr
    ;

logicExpr
    : equalityExpr ((OR | AND) equalityExpr)*
    ;
equalityExpr
    : relationalExpr ((EQ | NEQ) relationalExpr)*
    ;
relationalExpr
    : additiveExpr ((LT | LE | GT | GE) additiveExpr)*
    ;
additiveExpr
    : multiplicativeExpr ((ADD | SUB) multiplicativeExpr)*
    ;
multiplicativeExpr
    : powerExpr ((MUL | DIV | MOD) powerExpr)*
    ;
powerExpr
    : unaryExpr (POW unaryExpr)*
    ;
unaryExpr
    : (SUB | NOT) unaryExpr    # unaryExpresion
    | primaryExpr              # primaryExpresion
    ;

// ======================  PRIMARY EXPRESSIONS ======================
primaryExpr
    : primaryExpr LBRACK expr RBRACK           # indexingExpr
    | library                                  # libraryExpr
    | functionCall                             # functionCallExpr
    | pourStmt                                 # pourExpr
    | appendCall                               # appendCallExpr
    | removeCall                               # removeCallExpr
    | lenCall                                  # lenCallExpr
    | RANGE '(' expr (COMMA expr)? (COMMA expr)? ')' # rangeExpr
    | INT_CAST LPAREN expr RPAREN              # intCastExpr
    | FLOAT_CAST LPAREN expr RPAREN            # floatCastExpr
    | STR_CAST LPAREN expr RPAREN              # strCastExpr
    | BOOL_CAST LPAREN expr RPAREN             # boolCastExpr
    | lambdaExpr                               # lambdaExpresion
    | literal                                  # literalExpr
    | ID                                       # idExpr
    | LPAREN expr RPAREN                       # parenExpr
    ;

// ======================  LITERALES ======================
literal
    : INT         # intLiteral
    | FLOAT       # floatLiteral
    | STRING      # stringLiteral
    | BOOL        # boolLiteral
    | listLiteral # listLiteralExpr
    ;

listLiteral
    : LBRACK (expr (COMMA expr)*)? RBRACK
    ;

// ======================  TIPOS ======================
typeDecl
    : INT_TYPE
    | FLOAT_TYPE
    | BOOL_TYPE
    | VOID_TYPE
    | STRING_TYPE
    | LIST LBRACK typeDecl RBRACK
    | functionParam
    ;
