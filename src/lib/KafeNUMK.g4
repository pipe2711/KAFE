grammar KafeNUMK;

numkLibrary : 'numk.add' '(' expr ',' expr ')'    # numkadd
    | 'numk.sub' '(' expr ',' expr ')'            # numksub
    | 'numk.mul' '(' expr ',' expr ')'            # numkmul
    | 'numk.inv' '(' expr ')'                     # numkinv
    | 'numk.transpose' '(' expr ')'               # numktranspose
    ;
