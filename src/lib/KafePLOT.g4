grammar KafePLOT;

plotLibrary
    : 'plot.graph' '(' expr (',' expr)* ')' # graph
    | 'plot.xlabel' '(' expr ')'            # xlabel
    | 'plot.ylabel' '(' expr ')'            # ylabel
    | 'plot.title'  '(' expr ')'            # title
    | 'plot.grid' '(' expr ')'              # grid
    | 'plot.color' '(' expr ')'             # color
    | 'plot.pointColor' '(' expr ')'        # pointColor
    | 'plot.pointSize' '(' expr ')'         # pointSize
    | 'plot.legend' '(' expr ')'            # legend
    | 'plot.bar' '(' expr ',' expr ')'      # bar
    | 'plot.barValues' '(' expr ')'         # barValues
    | 'plot.pie' '(' expr ',' expr ')'      # pie
    | 'plot.legend' '(' expr ')'         # legend


    ;
