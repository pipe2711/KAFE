grammar Kafe_Grammar;

import Kafe_Lexer;

program : importStmt* stmt* ;

importStmt : IMPORT ID SEMI;

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

varDecl : typeDecl ID ASSIGN expr;
assignStmt : ID ASSIGN expr;

functionDecl: DRIP ID '(' paramList? ')' ('(' paramList ')')* COLON block SEMI;

paramList : paramDecl (COMMA paramDecl)*;
paramDecl
    : ID COLON typeDecl                                      # simpleParam
    | ID COLON FUNC '(' paramList? ')' COLON typeDecl        # functionParam;

returnStmt : RETURN expr;
showStmt : SHOW '(' expr ')';
pourStmt : POUR '(' expr ')';

ifElseExpr: IF '(' expr ')' COLON block (PIPE '(' expr ')' COLON block)* (ELSE COLON block)? SEMI;

whileLoop : 'while' '(' expr ')' COLON block SEMI;
forLoop : 'for' '(' ID 'in' expr ')' COLON block SEMI;

matchExpr : MATCH expr COLON matchCase+ SEMI;
matchCase : PIPE pattern ARROW expr;
pattern
    : literal                                                # literalPattern
    | UNDERSCORE                                             # wildcardPattern
    | ID                                                     # idPattern ;

block : stmt*;

expr : logicExpr;

logicExpr: equalityExpr ((OR | AND) equalityExpr)*;

equalityExpr: relationalExpr ((EQ | NEQ) relationalExpr)*;

relationalExpr: additiveExpr ((LT | LE | GT | GE) additiveExpr)*;

additiveExpr: multiplicativeExpr ((ADD | SUB) multiplicativeExpr)*;

multiplicativeExpr: powerExpr ((MUL | DIV | MOD) powerExpr)*;

powerExpr: unaryExpr (POW unaryExpr)*;

unaryExpr
    : (SUB | NOT) unaryExpr # unaryExpresion
    | primaryExpr # primaryExpresion
    ;

primaryExpr
    : primaryExpr LBRACK expr RBRACK          # indexingExpr
    | functionCall                            # functionCallExpr
    | lambdaExpr                              # lambdaExpresion
    | literal                                 # literalExpr
    | ID                                      # idExpr
    | '(' expr ')'                            # parenExpr
    ;

functionCall : ID '(' argList? ')';
argList : arg (COMMA arg)*;
arg
    : expr                                                   # exprArgument
    | lambdaExpr                                             # lambdaArgument ;

lambdaExpr : '(' paramDecl ')' ARROW expr;

literal
    : INT                                                    # intLiteral
    | FLOAT                                                  # floatLiteral
    | CHAR                                                   # charLiteral
    | STRING                                                 # stringLiteral
    | BOOL                                                   # boolLiteral
    | listLiteral                                            # listLiteralExpr
    ;

listLiteral : LBRACK (expr (COMMA expr)*)? RBRACK;

typeDecl
    : INT_TYPE
    | FLOAT_TYPE
    | CHAR_TYPE
    | BOOL_TYPE
    | VOID_TYPE
    | STRING_TYPE
    | LIST LBRACK typeDecl RBRACK
    ;
