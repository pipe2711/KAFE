grammar KafeNUMK;

numkLibrary : NUMK_LIB '.add' '(' expr ',' expr ')'    # numkadd
    | NUMK_LIB '.sub' '(' expr ',' expr ')'            # numksub
    | NUMK_LIB '.mul' '(' expr ',' expr ')'            # numkmul
    | NUMK_LIB '.inv' '(' expr ')'                     # numkinv
    | NUMK_LIB '.transpose' '(' expr ')'               # numktranspose
    ;
