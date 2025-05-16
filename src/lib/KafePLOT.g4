grammar KafePLOT;

plotLibrary
    : PLOT_LIB '.graph' '(' expr (',' expr)* ')' # graph
    | PLOT_LIB '.xlabel' '(' expr ')'            # xlabel
    | PLOT_LIB '.ylabel' '(' expr ')'            # ylabel
    | PLOT_LIB '.title'  '(' expr ')'            # title
    | PLOT_LIB '.grid' '(' expr ')'              # grid
    | PLOT_LIB '.color' '(' expr ')'             # color
    | PLOT_LIB '.pointColor' '(' expr ')'        # pointColor
    | PLOT_LIB '.pointSize' '(' expr ')'         # pointSize
    | PLOT_LIB '.legend' '(' expr ')'            # legend
    | PLOT_LIB '.bar' '(' expr ',' expr ')'      # bar
    | PLOT_LIB '.barValues' '(' expr ')'         # barValues
    | PLOT_LIB '.pie' '(' expr ',' expr ')'      # pie
    | PLOT_LIB '.legend' '(' expr ')'            # legend
    ;
