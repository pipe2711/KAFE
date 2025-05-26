import pathlib
from antlr4 import FileStream, CommonTokenStream
from Kafe_GrammarLexer import Kafe_GrammarLexer
from Kafe_GrammarParser import Kafe_GrammarParser

from errores import raiseModuleNotFound
import globals

def importStmt(self, ctx):
    module = ctx.ID().getText()

    esLibreria = self.libraries.get(module) != None
    if esLibreria:
        self.libraries[module][1] = True
        return

    if module in self.imported:
        return
    self.imported.add(module)

    # Construir lista de rutas a probar
    candidates = []
    if globals.current_dir:
        candidates.append(pathlib.Path(globals.current_dir) / f"{module}.kf")
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
    prev_dir = globals.current_dir
    globals.current_dir = filename.parent

    # Parsear y ejecutar el módulo
    input_stream = FileStream(str(filename), encoding='utf-8')
    lexer        = Kafe_GrammarLexer(input_stream)
    tokens       = CommonTokenStream(lexer)
    parser       = Kafe_GrammarParser(tokens)
    tree         = parser.program()
    self.visit(tree)

    # Restaurar directorio anterior
    globals.current_dir = prev_dir
    return
