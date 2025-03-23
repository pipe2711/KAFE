grammar Kafe_Grammar.g4
import Kafe_Lexer.g4

prog: stat+;

stat: expr NEWLINE 
    | ID '=' expr NEWLINE 
    | NEWLINE
    ;

expr: expr 'EQUALS' expr //Igual a 
    | expr 'NOEQUAL' expr //Diferente a
    | expr 'MEQ' expr //menor que
    | expr 'MAQ' expr //mayor que 
    | expr 'MEQI' expr //menor o igual que 
    | expr 'MAQI' expr //mayor o igual que 
    | expr 'OR' expr //o
    | expr 'AND' expr //Y 
    | 'NOT'expr'
    ;  