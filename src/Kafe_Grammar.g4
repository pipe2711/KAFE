grammar Kafe_Grammar;

// Importar gramáticas auxiliares, incluida la nueva librería Math
import Kafe_Lexer, KafePLOT, KafeNUMK, KafeFILES, KafeMATH;

program : (importStmt SEMI)* (stmt SEMI)*;

importStmt
    : IMPORT NUMK_LIB        # importNUMK
    | IMPORT PLOT_LIB        # importPLOT
    | IMPORT ID              # simpleImport
    ;

stmt
    : varDecl
    | assignStmt
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

block : (stmt SEMI)*;

// ======================  VARIABLES ======================
varDecl   : typeDecl ID ('=' expr)? ;
assignStmt: ID '=' expr ;

// ======================  FUNCIONES ======================
// Función currificada: drip id (params) (params)* ARROW typeDecl COLON block ;
functionDecl
    : DRIP ID '(' paramList? ')' ('(' paramList ')')* ARROW typeDecl COLON block
    ;
paramList : paramDecl (COMMA paramDecl)*;
paramDecl
    : ID COLON typeDecl                                      # simpleParam
    | ID COLON FUNC '(' paramList? ')' COLON typeDecl        # functionParam
    ;

// Llamadas currificables: f(args) (args)*
functionCall
    : ID '(' argList? ')' ('(' argList? ')')*
    ;
argList : arg (COMMA arg)*;
arg
    : expr        # exprArgument
    | lambdaExpr  # lambdaArgument
    ;

lambdaExpr : '(' paramDecl ')' ARROW expr;

returnStmt : RETURN expr;
showStmt   : SHOW '(' expr ')';
pourStmt   : POUR '(' expr ')';

// ======================  CONDICIONALES ======================
ifElseExpr: IF '(' expr ')' COLON block (elifBranch)* (ELSE COLON block)?;
elifBranch: ELIF '(' expr ')' COLON block;

// ======================  BUCLES ======================
whileLoop : 'while' '(' expr ')' COLON block;
forLoop   : 'for' '(' ID 'in' expr ')' COLON block;

// ======================  EXPRESIONES ======================
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

primaryExpr
    : primaryExpr LBRACK expr RBRACK          # indexingExpr
    | functionCall                            # functionCallExpr
    | numkLibrary                             # numkLibraryExpr
    | plotLibrary                             # plotLibraryExpr
    | filesLibrary                            # filesLibraryExpr
    | mathLibrary                             # mathLibraryExpr
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

// ======================  TIPOS ======================
literal
    : INT         # intLiteral
    | FLOAT       # floatLiteral
    | STRING      # stringLiteral
    | BOOL        # boolLiteral
    | listLiteral # listLiteralExpr
    ;

listLiteral : LBRACK (expr (COMMA expr)*)? RBRACK;

typeDecl
    : INT_TYPE
    | FLOAT_TYPE
    | BOOL_TYPE
    | VOID_TYPE
    | STRING_TYPE
    | LIST LBRACK typeDecl RBRACK
    | FUNC '(' paramList? ')' COLON typeDecl
    ;
