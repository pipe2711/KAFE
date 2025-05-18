import sys
import os

from Kafe_GrammarVisitor import Kafe_GrammarVisitor
from Kafe_GrammarParser import Kafe_GrammarParser

from componentes_lenguaje.base.funciones import (
    additiveExpr, assignStmt, equalityExpr, expr, idExpr, indexingExpr,
    logicExpr, multiplicativeExpr, powerExpr, relationalExpr,
    showStmt, unaryExpresion, varDecl, pourStmt
)
from componentes_lenguaje.bucles.funciones import forLoop, whileLoop
from componentes_lenguaje.condicionales.funciones import ifElseExpr
from componentes_lenguaje.funciones.funciones import (
    functionCall, functionDecl, lambdaExpr, returnStmt
)
from componentes_lenguaje.importar.funciones import importStmt

from lib.KafeNUMK.funciones import (
    numkadd, numksub, numkmul, numkinv, numktranspose, Numk
)
from lib.KafePLOT.funciones import (
    plotgraph, set_xlabel, set_ylabel, set_title, set_grid,
    set_color, set_point_color, set_point_size,
    plot_bar, set_bar_values, plot_pie, set_legend
)
from lib.KafePLOT.Plot import Plot

class EvalVisitorPrimitivo(Kafe_GrammarVisitor):
    def __init__(self, input_file):
        self.ruta_programa = os.path.abspath(input_file)
        self.plot = None
        self.numk = None
        self.math_funcs = {}
        self.variables = {}
        self.type_mapping = {"INT": int, "FLOAT": float, "STR": str, "BOOL": bool}
        self.nombre_tipos = {int: "INT", float: "FLOAT", str: "STR", bool: "BOOL"}
        self.imported = set()
        self.current_dir = None

    # ===== IMPORT =====
    def visitSimpleImport(self, ctx): importStmt(self, ctx)
    def visitImportNUMK(self, ctx): self.numk = Numk()
    def visitImportPLOT(self, ctx): self.plot = Plot()

    # ===== MATH IMPORT =====
    def visitImportMATH(self, ctx):
        from lib.KafeMATH.funciones import (
            pi, e, exp, log, pow_, sqrt,
            degrees, radians,
            sin, cos, tan, asin, acos, atan,
            sinh, cosh, tanh,
            factorial, gcd, lcm,
            math_abs, floor, ceil, math_round,
            sum_range, prod_range
        )
        self.math_funcs = {
            'pi': pi, 'e': e,
            'exp': exp, 'log': log, 'pow': pow_, 'sqrt': sqrt,
            'degrees': degrees, 'radians': radians,
            'sin': sin, 'cos': cos, 'tan': tan,
            'asin': asin, 'acos': acos, 'atan': atan,
            'sinh': sinh, 'cosh': cosh, 'tanh': tanh,
            'factorial': factorial, 'gcd': gcd, 'lcm': lcm,
            'abs': math_abs, 'floor': floor, 'ceil': ceil, 'round': math_round,
            'sum': sum_range, 'prod': prod_range
        }

    # ===== VARIABLES =====
    def visitVarDecl(self, ctx): return varDecl(self, ctx)
    def visitAssignStmt(self, ctx): return assignStmt(self, ctx)

    # ===== FUNCIONES =====
    def visitFunctionDecl(self, ctx): return functionDecl(self, ctx)
    def visitFunctionCall(self, ctx):
        name = ctx.ID().getText()
        if name in self.math_funcs and ctx.argList():
            args = [self.visit(arg.expr()) for arg in ctx.argList().arg()]
            return self.math_funcs[name](*args)
        elif name in self.math_funcs:
            return self.math_funcs[name]()
        return functionCall(self, ctx)

    def visitLambdaExpr(self, ctx): return lambdaExpr(self, ctx)
    def visitLambdaExpresion(self, ctx): return self.visit(ctx.lambdaExpr())
    def visitReturnStmt(self, ctx): return returnStmt(self, ctx)
    def visitShowStmt(self, ctx): showStmt(self, ctx)
    def visitPourStmt(self, ctx): return pourStmt(self, ctx)

    # ===== CONDICIONALES =====
    def visitIfElseExpr(self, ctx): return ifElseExpr(self, ctx)

    # ===== BUCLES =====
    def visitWhileLoop(self, ctx): whileLoop(self, ctx)
    def visitForLoop(self, ctx): forLoop(self, ctx)

    # ===== EXPRESIONES =====
    def visitExpr(self, ctx): return expr(self, ctx)
    def visitIndexingExpr(self, ctx): return indexingExpr(self, ctx)
    def visitLogicExpr(self, ctx): return logicExpr(self, ctx)
    def visitEqualityExpr(self, ctx): return equalityExpr(self, ctx)
    def visitRelationalExpr(self, ctx): return relationalExpr(self, ctx)
    def visitAdditiveExpr(self, ctx): return additiveExpr(self, ctx)
    def visitMultiplicativeExpr(self, ctx): return multiplicativeExpr(self, ctx)
    def visitPowerExpr(self, ctx): return powerExpr(self, ctx)
    def visitUnaryExpresion(self, ctx): return unaryExpresion(self, ctx)
    def visitParenExpr(self, ctx): return self.visit(ctx.expr())
    def visitIdExpr(self, ctx): return idExpr(self, ctx)

    # ===== LITERALS =====
    def visitIntLiteral(self, ctx): return int(ctx.getText())
    def visitFloatLiteral(self, ctx): return float(ctx.getText())
    def visitStringLiteral(self, ctx): return ctx.getText()[1:-1]
    def visitBoolLiteral(self, ctx): return ctx.getText() == 'True'
    def visitListLiteral(self, ctx): return [self.visit(e) for e in ctx.expr()]
    def visitStrCastExpr(self, ctx): return str(self.visit(ctx.expr()))
    def visitBoolCastExpr(self, ctx): return bool(self.visit(ctx.expr()))
    def visitFloatCastExpr(self, ctx): return float(self.visit(ctx.expr()))
    def visitIntCastExpr(self, ctx): return int(self.visit(ctx.expr()))

    # ===== NUMK =====
    def visitNumkadd(self, ctx): return numkadd(self, ctx, self.numk) if self.numk else (_ for _ in ()).throw(Exception('numk library not imported'))
    def visitNumksub(self, ctx): return numksub(self, ctx, self.numk) if self.numk else (_ for _ in ()).throw(Exception('numk library not imported'))
    def visitNumkmul(self, ctx): return numkmul(self, ctx, self.numk) if self.numk else (_ for _ in ()).throw(Exception('numk library not imported'))
    def visitNumkinv(self, ctx): return numkinv(self, ctx, self.numk) if self.numk else (_ for _ in ()).throw(Exception('numk library not imported'))
    def visitNumktranspose(self, ctx): return numktranspose(self, ctx, self.numk) if self.numk else (_ for _ in ()).throw(Exception('numk library not imported'))

    # ===== PLOT =====
    def visitGraph(self, ctx): return plotgraph(self, ctx, self.plot, self.ruta_programa)
    def visitXlabel(self, ctx): return set_xlabel(self, ctx, self.plot)
    def visitYlabel(self, ctx): return set_ylabel(self, ctx, self.plot)
    def visitTitle(self, ctx): return set_title(self, ctx, self.plot)
    def visitGrid(self, ctx): return set_grid(self, ctx, self.plot)
    def visitColor(self, ctx): return set_color(self, ctx, self.plot)
    def visitPointColor(self, ctx): return set_point_color(self, ctx, self.plot)
    def visitPointSize(self, ctx): return set_point_size(self, ctx, self.plot)
    def visitBar(self, ctx): return plot_bar(self, ctx, self.plot, self.ruta_programa)
    def visitBarValues(self, ctx): return set_bar_values(self, ctx, self.plot)
    def visitPie(self, ctx): return plot_pie(self, ctx, self.plot, self.ruta_programa)
    def visitLegend(self, ctx): return set_legend(self, ctx, self.plot)

    # ===== MATH INTERNAL =====
    def _visit_math(self, ctx):
        # Obtener todos los subcontextos de tipo ExprContext
        exprs = ctx.getTypedRuleContexts(Kafe_GrammarParser.ExprContext)
        args = [self.visit(c) for c in exprs]
        name = ctx.getChild(0).getText()
        if name not in self.math_funcs:
            raise Exception(f"Math function '{name}' not imported")
        return self.math_funcs[name](*args)

for _attr in dir(Kafe_GrammarVisitor):
    if _attr.startswith('visit') and (_attr.endswith('Function') or _attr.endswith('Constant')):
        setattr(EvalVisitorPrimitivo, _attr, EvalVisitorPrimitivo._visit_math)
