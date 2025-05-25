grammar KafeFILES;

filesLibrary
    : 'file' '.' 'create' '(' STRING ')'                # FileCreate
    | 'file' '.' 'read' '(' STRING ')'                  # FileRead
    | 'file' '.' 'write' '(' STRING ',' STRING ')'      # FileWrite
    | 'file' '.' 'delete' '(' STRING ')'                # FileDelete
    ;
