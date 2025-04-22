// Kafe_Grammar.g4
grammar Kafe_Grammar;

import Kafe_Lexer;

// ─────────────────────────── Programa ───────────────────────────
program : importStmt* stmt* ;

// ─────────────────────────── Instrucciones ───────────────────────
importStmt : IMPORT ID SEMI;

stmt
    : varDecl    SEMI
    | assignStmt SEMI
    | functionDecl
    | ifElseExpr
    | whileLoop
    | forLoop
    | returnStmt SEMI
    | showStmt   SEMI
    | pourStmt   SEMI
    | functionCall SEMI          // ← llamada de función como sentencia
    | matchExpr
    ;

// ─────────────────────────── Declaraciones ───────────────────────
varDecl   : typeDecl ID ASSIGN expr;
assignStmt: ID ASSIGN expr;

// Función currificada:       drip id (params) (params)* : block ;
functionDecl
    : DRIP ID '(' paramList? ')' ('(' paramList ')')* ARROW typeDecl COLON block SEMI
    ;

paramList : paramDecl (COMMA paramDecl)*;
paramDecl
    : ID COLON typeDecl                                      # simpleParam
    | ID COLON FUNC '(' paramList? ')' COLON typeDecl        # functionParam
    ;

// ─────────────────────────── Sentencias básicas ─────────────────
returnStmt : RETURN expr;
showStmt   : SHOW '(' expr ')';
pourStmt   : POUR '(' expr ')';

// ─────────────────────────── Control de flujo ───────────────────
ifElseExpr
    : IF '(' expr ')' COLON block
      (PIPE '(' expr ')' COLON block)*
      (ELSE COLON block)?
      SEMI
    ;

whileLoop : 'while' '(' expr ')' COLON block SEMI;
forLoop   : 'for' '(' ID 'in' expr ')' COLON block SEMI;

// ─────────────────────────── Match / Pattern Matching ───────────
matchExpr : MATCH expr COLON matchCase+ SEMI;
matchCase : PIPE pattern ARROW expr;
pattern
    : literal        # literalPattern
    | UNDERSCORE     # wildcardPattern
    | ID             # idPattern
    ;

// ─────────────────────────── Bloques ────────────────────────────
block : stmt*;

// ─────────────────────────── Expresiones ────────────────────────
expr : logicExpr;

logicExpr        : equalityExpr ((OR   | AND) equalityExpr)*;
equalityExpr     : relationalExpr ((EQ | NEQ) relationalExpr)*;
relationalExpr   : additiveExpr ((LT | LE | GT | GE) additiveExpr)*;
additiveExpr     : multiplicativeExpr ((ADD | SUB) multiplicativeExpr)*;
multiplicativeExpr: powerExpr ((MUL | DIV | MOD) powerExpr)*;
powerExpr        : unaryExpr (POW unaryExpr)*;

unaryExpr
    : (SUB | NOT) unaryExpr  # unaryExpresion
    | primaryExpr            # primaryExpresion
    ;

// ─────────────────────────── Primarias ──────────────────────────
primaryExpr
    : primaryExpr LBRACK expr RBRACK          # indexingExpr
    | functionCall                            # functionCallExpr
    | pourStmt                                # pourExpr
    | INT_CAST   '(' expr ')'                 # intCastExpr
    | FLOAT_CAST '(' expr ')'                 # floatCastExpr
    | STR_CAST   '(' expr ')'                 # strCastExpr
    | BOOL_CAST  '(' expr ')'                 # boolCastExpr
    | lambdaExpr                              # lambdaExpresion
    | literal                                 # literalExpr
    | ID                                      # idExpr
    | '(' expr ')'                            # parenExpr
    ;

// Llamadas currificables:   f(args) (args)*
functionCall
    : ID '(' argList? ')' ('(' argList? ')')*
    ;
argList : arg (COMMA arg)*;
arg
    : expr        # exprArgument
    | lambdaExpr  # lambdaArgument
    ;

// Lambda:  (param) => expr
lambdaExpr : '(' paramDecl ')' ARROW expr;

// ─────────────────────────── Literales ──────────────────────────
literal
    : INT         # intLiteral
    | FLOAT       # floatLiteral
    | STRING      # stringLiteral
    | BOOL        # boolLiteral
    | listLiteral # listLiteralExpr
    ;

listLiteral : LBRACK (expr (COMMA expr)*)? RBRACK;

// ─────────────────────────── Tipado ─────────────────────────────
typeDecl
    : INT_TYPE
    | FLOAT_TYPE
    | BOOL_TYPE
    | VOID_TYPE
    | STRING_TYPE
    | LIST LBRACK typeDecl RBRACK
    | FUNC '(' paramList? ')' COLON typeDecl   // ← función como tipo
    ;