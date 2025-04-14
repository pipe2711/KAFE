#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Kafe_GrammarVisitor import Kafe_GrammarVisitor
from Kafe_GrammarParser import Kafe_GrammarParser
from antlr4 import FileStream, CommonTokenStream

# Excepción para manejo del "return"
class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class EvalVisitorPrimitivo(Kafe_GrammarVisitor):
    def __init__(self):
        # Ambiente global: variables (incluyendo arreglos) y funciones definidas
        self.memory = {}
        self.functions = {}
        # Diccionario para almacenar módulos importados
        self.modules = {}

    # --------------------------------------------------
    # Regla principal: program
    # program : importStmt* stmt* ;
    # Se procesan primero todos los import y luego las sentencias.
    # --------------------------------------------------
    def visitProgram(self, ctx: Kafe_GrammarParser.ProgramContext):
        for importStmt in ctx.importStmt():
            self.visit(importStmt)
        for stmt in ctx.stmt():
            self.visit(stmt)
        return None

    # --------------------------------------------------
    # Módulos
    # importStmt : IMPORT ID SEMI ;
    # Se asume que el módulo se encuentra en un archivo llamado "<moduleName>.kafe"
    # --------------------------------------------------
    def visitImportStmt(self, ctx: Kafe_GrammarParser.ImportStmtContext):
        module_name = ctx.ID().getText()
        module_file = module_name + ".kafe"
        try:
            input_stream = FileStream(module_file)
        except Exception as e:
            raise Exception(f"No se pudo abrir el módulo '{module_name}' en el archivo '{module_file}'. Error: {str(e)}")
        # Crear el lexer y parser para el módulo
        from Kafe_GrammarLexer import Kafe_GrammarLexer  # Asegúrate de que este archivo esté en tu PYTHONPATH
        lexer = Kafe_GrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = Kafe_GrammarParser(stream)
        tree = parser.program()
        # Se crea un nuevo visitor para evaluar el módulo
        module_visitor = EvalVisitorPrimitivo()
        # Opcional: compartir la misma tabla de módulos para evitar recargas dobles
        module_visitor.modules = self.modules
        module_visitor.visit(tree)
        # Fusionar las funciones y variables del módulo en el ambiente global.
        # (Cuidado con posibles colisiones; aquí se hace una fusión simple).
        self.memory.update(module_visitor.memory)
        self.functions.update(module_visitor.functions)
        self.modules[module_name] = module_visitor
        print(f"Módulo '{module_name}' importado desde '{module_file}'.")
        return None

    # --------------------------------------------------
    # Funciones y Lambdas
    # functionDecl : DRIP ID '(' paramList? ')' ('(' paramList ')')* COLON block SEMI ;
    # --------------------------------------------------
    def visitFunctionDecl(self, ctx: Kafe_GrammarParser.FunctionDeclContext):
        func_name = ctx.ID().getText()
        params = []
        if ctx.paramList():
            params = self.visit(ctx.paramList())
        block = ctx.block()

        def func(*args):
            if len(args) != len(params):
                raise Exception(f"La función '{func_name}' esperaba {len(params)} argumentos, pero recibió {len(args)}.")
            # Crear un nuevo ámbito (se copia el ambiente anterior)
            old_memory = self.memory.copy()
            for i, param in enumerate(params):
                self.memory[param] = args[i]
            try:
                self.visit(block)
            except ReturnException as ret:
                result = ret.value
            else:
                result = None
            # Restaurar el ambiente
            self.memory = old_memory
            return result

        self.functions[func_name] = func
        print(f"Función '{func_name}' declarada con parámetros: {params}")
        return None

    def visitLambdaExpr(self, ctx: Kafe_GrammarParser.LambdaExprContext):
        # lambdaExpr : '(' paramDecl ')' ARROW expr ;
        param = self.visit(ctx.paramDecl())
        body = ctx.expr()
        def lambda_func(arg):
            old_memory = self.memory.copy()
            self.memory[param] = arg
            result = self.visit(body)
            self.memory = old_memory
            return result
        return lambda_func

    def visitParamList(self, ctx: Kafe_GrammarParser.ParamListContext):
        # paramList : paramDecl (COMMA paramDecl)* ;
        params = []
        for param in ctx.paramDecl():
            params.append(self.visit(param))
        return params

    def visitParamDecl(self, ctx: Kafe_GrammarParser.ParamDeclContext):
        # paramDecl : ID COLON typeDecl | ID COLON FUNC '(' paramList? ')' COLON typeDecl ;
        return ctx.ID().getText()

    # --------------------------------------------------
    # Sentencia return
    # returnStmt : RETURN expr ;
    # --------------------------------------------------
    def visitReturnStmt(self, ctx: Kafe_GrammarParser.ReturnStmtContext):
        value = self.visit(ctx.expr())
        raise ReturnException(value)

    # --------------------------------------------------
    # Arreglos: variables (varDecl)
    # varDecl : typeDecl ID ASSIGN expr ;
    # Se asume que si el valor evaluado es un list, es un arreglo.
    # --------------------------------------------------
    def visitVarDecl(self, ctx: Kafe_GrammarParser.VarDeclContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        print(f"Variable '{var_name}' declarada con valor: {value}")
        return value

    # --------------------------------------------------
    # Implementaciones mínimas para apoyar la ejecución
    # --------------------------------------------------
    def visitBlock(self, ctx: Kafe_GrammarParser.BlockContext):
        result = None
        for stmt in ctx.stmt():
            result = self.visit(stmt)
        return result

    def visitFunctionCall(self, ctx: Kafe_GrammarParser.FunctionCallContext):
        func_name = ctx.ID().getText()
        args = []
        if ctx.argList():
            args = self.visit(ctx.argList())
        if func_name in self.functions:
            return self.functions[func_name](*args)
        else:
            raise Exception(f"Función '{func_name}' no definida.")

    def visitArgList(self, ctx: Kafe_GrammarParser.ArgListContext):
        args = []
        for arg in ctx.arg():
            args.append(self.visit(arg))
        return args

    def visitLiteral(self, ctx: Kafe_GrammarParser.LiteralContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.CHAR():
            return ctx.CHAR().getText()[1:-1]
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False

    def visitID(self, ctx: Kafe_GrammarParser.IDContext):
        var_name = ctx.getText()
        if var_name in self.memory:
            return self.memory[var_name]
        else:
            raise Exception(f"Variable '{var_name}' no definida.")

    def visitTypeDecl(self, ctx: Kafe_GrammarParser.TypeDeclContext):
        return ctx.getText()

    def visitChildren(self, node):
        result = None
        for child in node.getChildren():
            result = self.visit(child)
        return result
