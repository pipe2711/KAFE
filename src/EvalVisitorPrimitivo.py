import sys
import os

from Kafe_GrammarVisitor import Kafe_GrammarVisitor
from Kafe_GrammarParser import Kafe_GrammarParser
from componentes_lenguaje.base.funciones import additiveExpr, assignStmt, equalityExpr, expr, idExpr, indexingExpr, logicExpr, multiplicativeExpr, powerExpr, relationalExpr, showStmt, unaryExpresion, varDecl, pourStmt
from componentes_lenguaje.bucles.funciones import forLoop, whileLoop
from componentes_lenguaje.condicionales.funciones import ifElseExpr
from componentes_lenguaje.funciones.funciones import functionCall, functionDecl, lambdaExpr, returnStmt
from componentes_lenguaje.importar.funciones import importStmt
from lib.KafeNUMK.funciones import numkadd, numksub, numkmul, numkinv, numktranspose, Numk
from lib.KafePLOT.funciones import plotgraph, set_xlabel, set_ylabel, set_title, set_grid, set_color, set_point_color, set_point_size, plot_bar, set_bar_values, plot_pie, set_legend
from lib.KafePLOT.Plot import Plot

class EvalVisitorPrimitivo(Kafe_GrammarVisitor):
    def __init__(self, input_file):
        self.ruta_programa = os.path.abspath(input_file)
        self.plot = None
        self.numk = None
        self.variables    = {}
        self.type_mapping = {"INT": int, "FLOAT": float, "STR": str, "BOOL": bool}
        self.nombre_tipos = { int:"INT", float:"FLOAT", str:"STR", bool:"BOOL" }
        self.imported     = set()
        # Directorio actual de .kf para imports relativos
        self.current_dir  = None

    def visitSimpleImport(self, ctx):
        importStmt(self, ctx)

    def visitVarDecl(self, ctx):
        return varDecl(self, ctx)

    def visitAssignStmt(self, ctx):
        return assignStmt(self, ctx)


    # ======================  FUNCIONES ======================


    def visitFunctionDecl(self, ctx):
        return functionDecl(self, ctx)

    def visitFunctionCall(self, ctx):
        return functionCall(self, ctx)

    def visitLambdaExpr(self, ctx):
        return lambdaExpr(self, ctx)

    def visitLambdaExpresion(self, ctx):
        return self.visit(ctx.lambdaExpr())

    def visitReturnStmt(self, ctx):
        return returnStmt(self, ctx)

    def visitShowStmt(self, ctx):
        showStmt(self, ctx)

    def visitPourStmt(self, ctx):
        return pourStmt(self, ctx)


    # ======================  CONDICIONALES ======================


    def visitIfElseExpr(self, ctx):
        return ifElseExpr(self, ctx)


    # ======================  BUCLES ======================


    def visitWhileLoop(self, ctx):
        whileLoop(self, ctx)

    def visitForLoop(self, ctx):
        forLoop(self, ctx)


    # ======================  EXPRESIONES ======================

    def visitExpr(self, ctx):
        return expr(self, ctx)

    def visitIndexingExpr(self, ctx):
        return indexingExpr(self, ctx)

    def visitLogicExpr(self, ctx):
        return logicExpr(self, ctx)

    def visitEqualityExpr(self, ctx):
        return equalityExpr(self, ctx)

    def visitRelationalExpr(self, ctx):
        return relationalExpr(self, ctx)

    def visitAdditiveExpr(self, ctx):
        return additiveExpr(self, ctx)

    def visitMultiplicativeExpr(self, ctx):
        return multiplicativeExpr(self, ctx)

    def visitPowerExpr(self, ctx):
        return powerExpr(self, ctx)

    def visitUnaryExpresion(self, ctx):
        return unaryExpresion(self, ctx)

    def visitParenExpr(self, ctx:Kafe_GrammarParser.ParenExprContext):
        return self.visitChildren(ctx.expr())

    def visitIdExpr(self, ctx):
        return idExpr(self, ctx)


    # ======================  TIPOS ======================

    def visitIntLiteral(self, ctx):
        return int(ctx.getText())

    def visitFloatLiteral(self, ctx):
        return float(ctx.getText())

    def visitStringLiteral(self, ctx):
        return ctx.getText()[1:-1]

    def visitBoolLiteral(self, ctx):
        if ctx.getText() == "False":
            return False
        else:
            return True

    def visitListLiteral(self, ctx):
        lista = []

        for expr in ctx.expr():
            valor = self.visit(expr)
            lista.append(valor)

        return lista

    def visitStrCastExpr(self, ctx):
        return str(self.visit(ctx.expr()))

    def visitBoolCastExpr(self, ctx):
        return bool(self.visit(ctx.expr()))

    def visitFloatCastExpr(self, ctx):
        return float(self.visit(ctx.expr()))

    def visitIntCastExpr(self, ctx):
        return int(self.visit(ctx.expr()))


    # ======================  NUMK Library ======================

    def visitImportNUMK(self, ctx):
        self.numk = Numk()

    def visitNumkadd(self, ctx):
        if self.numk == None:
            raise Exception("numk library not imported")

        return numkadd(self, ctx, self.numk)

    def visitNumksub(self, ctx):
        if self.numk == None:
            raise Exception("numk library not imported")

        return numksub(self, ctx, self.numk)

    def visitNumkmul(self, ctx):
        if self.numk == None:
            raise Exception("numk library not imported")

        return numkmul(self, ctx, self.numk)

    def visitNumkinv(self, ctx):
        if self.numk == None:
            raise Exception("numk library not imported")

        return numkinv(self, ctx, self.numk)

    def visitNumktranspose(self, ctx):
        if self.numk == None:
            raise Exception("numk library not imported")

        return numktranspose(self, ctx, self.numk)


    # ======================  FILES Library ======================


    # ======================  MATH Library ======================


    # ======================  PLOT Library ======================
    def visitImportPLOT(self, ctx):
        self.plot = Plot()

    def visitGraph(self, ctx):
        if self.plot == None:
            raise Exception("plot library not imported")

        return plotgraph(self, ctx, self.plot, self.ruta_programa)

    def visitXlabel(self, ctx):
        if self.plot == None:
            raise Exception("plot library not imported")

        return set_xlabel(self, ctx, self.plot)

    def visitYlabel(self, ctx):
        if self.plot == None:
            raise Exception("plot library not imported")

        return set_ylabel(self, ctx, self.plot)

    def visitTitle(self, ctx):
        if self.plot == None:
            raise Exception("plot library not imported")

        return set_title(self, ctx, self.plot)

    def visitGrid(self, ctx):
        if self.plot == None:
            raise Exception("plot library not imported")

        return set_grid(self, ctx, self.plot)

    def visitColor(self, ctx):
        if self.plot == None:
            raise Exception("plot library not imported")

        return set_color(self, ctx, self.plot)

    def visitPointColor(self, ctx):
        if self.plot == None:
            raise Exception("plot library not imported")

        return set_point_color(self, ctx, self.plot)

    def visitPointSize(self, ctx):
        if self.plot == None:
            raise Exception("plot library not imported")

        return set_point_size(self, ctx, self.plot)

    def visitBar(self, ctx):
        if self.plot == None:
            raise Exception("plot library not imported")

        return plot_bar(self, ctx, self.plot, self.ruta_programa)

    def visitBarValues(self, ctx):
        if self.plot == None:
            raise Exception("plot library not imported")

        return set_bar_values(self, ctx, self.plot)

    def visitPie(self, ctx):
        if self.plot == None:
            raise Exception("plot library not imported")

        return plot_pie(self, ctx, self.plot, self.ruta_programa)

    def visitLegend(self, ctx):
        if self.plot == None:
            raise Exception("plot library not imported")

        return set_legend(self, ctx, self.plot)
