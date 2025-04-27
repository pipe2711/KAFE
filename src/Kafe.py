import sys
import pathlib
import io
from antlr4 import InputStream, CommonTokenStream
from Kafe_GrammarLexer import Kafe_GrammarLexer
from Kafe_GrammarParser import Kafe_GrammarParser
from EvalVisitorPrimitivo import EvalVisitorPrimitivo


def main():
    # Verificar argumento del archivo .kf
    if len(sys.argv) < 2:
        print("Uso: python Kafe.py <archivo.kf>")
        sys.exit(1)

    base = pathlib.Path(__file__).parent
    input_file = sys.argv[1]
    filepath = base / input_file
    if not filepath.is_file():
        print(f"Archivo '{filepath}' no encontrado")
        sys.exit(1)

    contenido = filepath.read_text(encoding='utf-8')

    # 🔥 Capturar stdout
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()

    visitor = EvalVisitorPrimitivo()
    visitor.current_dir = filepath.parent

    input_stream = InputStream(contenido)
    lexer = Kafe_GrammarLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = Kafe_GrammarParser(tokens)
    tree = parser.program()

    visitor.visit(tree)


    sys.stdout = old_stdout

    print(mystdout.getvalue())


if __name__ == "__main__":
    main()
