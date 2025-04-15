import sys
from antlr4 import *
from Kafe_GrammarLexer import Kafe_GrammarLexer
from Kafe_GrammarParser import Kafe_GrammarParser
from EvalVisitorPrimitivo import EvalVisitorPrimitivo

def main():
    if len(sys.argv) < 2:
        print("Uso: python Kafe.py <archivo>")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        archivo = file.read()

    visitor = EvalVisitorPrimitivo()
    input_stream = InputStream(archivo)
    lexer = Kafe_GrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Kafe_GrammarParser(token_stream)
    arbol = parser.program()

    visitor.visit(arbol)

if __name__ == "__main__":
    main()
