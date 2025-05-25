grammar Kafe_Grammar;

options { tokenVocab=Kafe_Lexer; }

import
    Kafe_Lexer,
    KafePLOT,
    KafeNUMK,
    KafeFILES,
    KafeMATH
  ;

program
    : (importStmt SEMI)* (stmt SEMI)*
    ;

importStmt
    : IMPORT NUMK_LIB        # importNUMK
    | IMPORT PLOT_LIB        # importPLOT
    | IMPORT MATH_LIB        # importMATH
    | IMPORT ID              # simpleImport
    ;

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
    | pourStmt
    | functionCall
    | expr
    ;

block
    : (stmt SEMI)*
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
    : primaryExpr LBRACK expr RBRACK          # indexingExpr
    | mathLibrary                              # mathLibraryExpr
    | functionCall                             # functionCallExpr
    | numkLibrary                              # numkLibraryExpr
    | plotLibrary                              # plotLibraryExpr
    | filesLibrary                             # filesLibraryExpr
    | pourStmt                                 # pourExpr
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
