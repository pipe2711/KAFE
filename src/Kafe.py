import sys
import os
import pathlib
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from Kafe_GrammarLexer import Kafe_GrammarLexer
from Kafe_GrammarParser import Kafe_GrammarParser
from EvalVisitorPrimitivo import EvalVisitorPrimitivo
from errores import raiseScientificNotationError

import globals

class KafeErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Error de string sin cerrar
        if "token recognition error" in msg:
            raise Exception(
                f"SyntaxError: unterminated string literal at line {line}:{column}"
            )

        # Detectamos si el error parece ser de notación científica
        symbol_text = offendingSymbol.text if offendingSymbol else ""
        if 'e' in symbol_text.lower() or 'exponent' in msg.lower():
            raiseScientificNotationError(line, column, msg)
        else:
            # Error genérico de sintaxis
            raise Exception(
                f"SyntaxError at line {line}:{column} -> {msg}"
            )
def main():
    if len(sys.argv) < 2:
        print("Uso: python Kafe.py <archivo.kf>")
        sys.exit(1)

    base = pathlib.Path(__file__).parent
    input_file = sys.argv[1]
    filepath = base / input_file
    if not filepath.is_file():
        print(f"Archivo '{filepath}' no encontrado")
        sys.exit(1)

    globals.ruta_programa = os.path.abspath(input_file)
    globals.current_dir = os.path.dirname(globals.ruta_programa)

    contenido = filepath.read_text(encoding='utf-8')

    visitor = EvalVisitorPrimitivo()

    visitor.current_dir = filepath.parent

    input_stream = InputStream(contenido)
    lexer = Kafe_GrammarLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(KafeErrorListener())

    tokens = CommonTokenStream(lexer)

    parser = Kafe_GrammarParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(KafeErrorListener())

    tree = parser.program()

    visitor.visit(tree)


if __name__ == "__main__":
    main()
