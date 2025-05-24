import pathlib

from ..errores import raiseModuleNotFound
from antlr4 import FileStream, CommonTokenStream
from Kafe_GrammarLexer import Kafe_GrammarLexer
from Kafe_GrammarParser import Kafe_GrammarParser

def importStmt(self, ctx):
    module = ctx.ID().getText()
    if module in self.imported:
        return
    self.imported.add(module)

    # Construir lista de rutas a probar
    candidates = []
    if self.current_dir:
        candidates.append(pathlib.Path(self.current_dir) / f"{module}.kf")
    base = pathlib.Path(__file__).parent
    candidates.append(base / f"{module}.kf")
    candidates.append(base.parent / f"{module}.kf")

    filename = None
    for path in candidates:
        if path.is_file():
            filename = path
            break
    if filename is None:
        tried = ", ".join(str(p) for p in candidates)
        raiseModuleNotFound(module, tried)

    # Ajustar directorio para imports dentro del módulo
    prev_dir = self.current_dir
    self.current_dir = filename.parent

    # Parsear y ejecutar el módulo
    input_stream = FileStream(str(filename), encoding='utf-8')
    lexer        = Kafe_GrammarLexer(input_stream)
    tokens       = CommonTokenStream(lexer)
    parser       = Kafe_GrammarParser(tokens)
    tree         = parser.program()
    self.visit(tree)

    # Restaurar directorio anterior
    self.current_dir = prev_dir
    return

