import sys
import os

from Kafe_GrammarVisitor import Kafe_GrammarVisitor
from Kafe_GrammarParser import Kafe_GrammarParser
from componentes_lenguaje.base.funciones import (
    additiveExpr, assignStmt, equalityExpr, expr, idExpr,
    indexedAssignStmt, indexingExpr, logicExpr,
    multiplicativeExpr, powerExpr, relationalExpr,
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
import lib.KafeMATH.funciones as math_funcs_module


class EvalVisitorPrimitivo(Kafe_GrammarVisitor):
    def __init__(self, input_file):
        self.ruta_programa = os.path.abspath(input_file)
        self.plot = None
        self.numk = None
        self.variables = {}
        self.type_mapping = {"INT": int, "FLOAT": float, "STR": str, "BOOL": bool}
        self.nombre_tipos = {int: "INT", float: "FLOAT", str: "STR", bool: "BOOL"}
        self.imported = set()
        self.current_dir = None

    # ──────────────────── IMPORTS ────────────────────
    def visitSimpleImport(self, ctx):
        importStmt(self, ctx)

    def visitImportNUMK(self, ctx):
        self.numk = Numk()

    def visitImportPLOT(self, ctx):
        self.plot = Plot()

    def visitImportMATH(self, ctx):
        return None

    # ──────────────────── VARIABLES ────────────────────
    def visitVarDecl(self, ctx):
        varDecl(self, ctx)

    def visitAssignStmt(self, ctx):
        assignStmt(self, ctx)

    def visitIndexedAssignStmt(self, ctx):
        indexedAssignStmt(self, ctx)

    def visitIndexing(self, ctx):
        return [self.visit(e) for e in ctx.expr()]

    # ──────────────────── FUNCIONES ────────────────────
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

    # ──────────────────── CONDICIONALES ────────────────────
    def visitIfElseExpr(self, ctx):
        return ifElseExpr(self, ctx)

    # ──────────────────── BUCLES ────────────────────
    def visitWhileLoop(self, ctx):
        whileLoop(self, ctx)

    def visitForLoop(self, ctx):
        forLoop(self, ctx)

    # ──────────────────── EXPRESIONES ────────────────────
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

    def visitParenExpr(self, ctx: Kafe_GrammarParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitIdExpr(self, ctx):
        return idExpr(self, ctx)

    # ──────────────────── LITERALES ────────────────────
    def visitIntLiteral(self, ctx):
        return int(ctx.getText())

    def visitFloatLiteral(self, ctx):
        return float(ctx.getText())

    def visitStringLiteral(self, ctx):
        return ctx.getText()[1:-1]

    def visitBoolLiteral(self, ctx):
        return ctx.getText() == 'True'

    def visitListLiteral(self, ctx):
        return [self.visit(e) for e in ctx.expr()]

    def visitStrCastExpr(self, ctx):
        return str(self.visit(ctx.expr()))

    def visitBoolCastExpr(self, ctx):
        return bool(self.visit(ctx.expr()))

    def visitFloatCastExpr(self, ctx):
        return float(self.visit(ctx.expr()))

    def visitIntCastExpr(self, ctx):
        return int(self.visit(ctx.expr()))

    # ──────────────────── NUMK ────────────────────
    def visitNumkadd(self, ctx):
        if self.numk is None:
            raise Exception("numk library not imported")
        return numkadd(self, ctx, self.numk)

    def visitNumksub(self, ctx):
        if self.numk is None:
            raise Exception("numk library not imported")
        return numksub(self, ctx, self.numk)

    def visitNumkmul(self, ctx):
        if self.numk is None:
            raise Exception("numk library not imported")
        return numkmul(self, ctx, self.numk)

    def visitNumkinv(self, ctx):
        if self.numk is None:
            raise Exception("numk library not imported")
        return numkinv(self, ctx, self.numk)

    def visitNumktranspose(self, ctx):
        if self.numk is None:
            raise Exception("numk library not imported")
        return numktranspose(self, ctx, self.numk)

        # ────────── MATH──────────

    def visitMathFunctionCall(self, ctx):
        name = ctx.ID().getText()
        args = [self.visit(e) for e in ctx.expr()]
        func = getattr(math_funcs_module, name, None)
        if func is None:
            raise Exception(f"Unknown math function: {name}")
        return func(*args)

    def visitMathConstant(self, ctx):
        name = ctx.ID().getText()
        const = getattr(math_funcs_module, name, None)
        if const is None:
            raise Exception(f"Unknown math constant: {name}")
        return const
        
    def visitSinFunction(self, ctx):
        return math_funcs_module.sin(self.visit(ctx.expr()))

    def visitCosFunction(self, ctx):
        return math_funcs_module.cos(self.visit(ctx.expr()))

    def visitTanFunction(self, ctx):
        return math_funcs_module.tan(self.visit(ctx.expr()))

    def visitAsinFunction(self, ctx):
        return math_funcs_module.asin(self.visit(ctx.expr()))

    def visitAcosFunction(self, ctx):
        return math_funcs_module.acos(self.visit(ctx.expr()))

    def visitAtanFunction(self, ctx):
        return math_funcs_module.atan(self.visit(ctx.expr()))

    def visitSinhFunction(self, ctx):
        return math_funcs_module.sinh(self.visit(ctx.expr()))

    def visitCoshFunction(self, ctx):
        return math_funcs_module.cosh(self.visit(ctx.expr()))

    def visitTanhFunction(self, ctx):
        return math_funcs_module.tanh(self.visit(ctx.expr()))

    def visitExpFunction(self, ctx):
        return math_funcs_module.exp(self.visit(ctx.expr()))

    def visitLogFunction(self, ctx):
        args = [self.visit(e) for e in ctx.expr()]
        if len(args) == 1:
            return math_funcs_module.log(args[0])
        return math_funcs_module.log(args[0], args[1])

    def visitSqrtFunction(self, ctx):
        return math_funcs_module.sqrt(self.visit(ctx.expr()))

    def visitPowFunction(self, ctx):
        return math_funcs_module.pow_( self.visit(ctx.expr(0)),
                                       self.visit(ctx.expr(1)) )

    def visitFactorialFunction(self, ctx):
        return math_funcs_module.factorial(self.visit(ctx.expr()))

    def visitGcdFunction(self, ctx):
        return math_funcs_module.gcd(*[self.visit(e) for e in ctx.expr()])

    def visitLcmFunction(self, ctx):
        return math_funcs_module.lcm(*[self.visit(e) for e in ctx.expr()])

    def visitCombFunction(self, ctx):
        return math_funcs_module.comb(self.visit(ctx.expr(0)),
                                      self.visit(ctx.expr(1)))

    def visitPermFunction(self, ctx):
        return math_funcs_module.perm(self.visit(ctx.expr(0)),
                                      self.visit(ctx.expr(1)))

    def visitDegreesFunction(self, ctx):
        return math_funcs_module.degrees(self.visit(ctx.expr()))

    def visitRadiansFunction(self, ctx):
        return math_funcs_module.radians(self.visit(ctx.expr()))

    def visitTruncFunction(self, ctx):
        return math_funcs_module.trunc(self.visit(ctx.expr()))

    def visitFmodFunction(self, ctx):
        return math_funcs_module.fmod(self.visit(ctx.expr(0)),
                                      self.visit(ctx.expr(1)))

    def visitRemainderFunction(self, ctx):
        return math_funcs_module.remainder(self.visit(ctx.expr(0)),
                                           self.visit(ctx.expr(1)))

    def visitAbsFunction(self, ctx):
        return math_funcs_module.math_abs(self.visit(ctx.expr()))

    def visitFloorFunction(self, ctx):
        return math_funcs_module.floor(self.visit(ctx.expr()))

    def visitCeilFunction(self, ctx):
        return math_funcs_module.ceil(self.visit(ctx.expr()))

    def visitRoundFunction(self, ctx):
        args = [self.visit(e) for e in ctx.expr()]
        return math_funcs_module.math_round(*args)

    # ……… Floating-point manipulation ………
    def visitCopysignFunction(self, ctx):
        return math_funcs_module.copysign(self.visit(ctx.expr(0)),
                                          self.visit(ctx.expr(1)))

    def visitIscloseFunction(self, ctx):
        return math_funcs_module.isclose(self.visit(ctx.expr(0)),
                                         self.visit(ctx.expr(1)))

    def visitIsfiniteFunction(self, ctx):
        return math_funcs_module.isfinite(self.visit(ctx.expr()))

    def visitIsinfFunction(self, ctx):
        return math_funcs_module.isinf(self.visit(ctx.expr()))

    def visitIsnanFunction(self, ctx):
        return math_funcs_module.isnan(self.visit(ctx.expr()))

    def visitUlpFunction(self, ctx):
        return math_funcs_module.ulp(self.visit(ctx.expr()))

    # ……… Power / exponential / logarithmic ………
    def visitExp2Function(self, ctx):
        return math_funcs_module.exp2(self.visit(ctx.expr()))

    def visitCbrtFunction(self, ctx):
        return math_funcs_module.cbrt(self.visit(ctx.expr()))

    def visitExpm1Function(self, ctx):
        return math_funcs_module.expm1(self.visit(ctx.expr()))

    def visitLog2Function(self, ctx):
        return math_funcs_module.log2(self.visit(ctx.expr()))

    def visitLog10Function(self, ctx):
        return math_funcs_module.log10(self.visit(ctx.expr()))

    # ……… Summation & products ………
    def visitDistFunction(self, ctx):
        return math_funcs_module.dist(self.visit(ctx.expr(0)),
                                      self.visit(ctx.expr(1)))

    def visitFsumFunction(self, ctx):
        return math_funcs_module.fsum(self.visit(ctx.expr()))

    def visitHypotFunction(self, ctx):
        return math_funcs_module.hypot(*[self.visit(e) for e in ctx.expr()])

    def visitProdFunction(self, ctx):
        return math_funcs_module.prod(self.visit(ctx.expr()))

    def visitSumFunction(self, ctx):
        return sum(self.visit(ctx.expr())) 

    def visitSumRangeFunction(self, ctx):
        return math_funcs_module.sum_range(self.visit(ctx.expr(0)),
                                           self.visit(ctx.expr(1)))

    def visitProdRangeFunction(self, ctx):
        return math_funcs_module.prod_range(self.visit(ctx.expr(0)),
                                            self.visit(ctx.expr(1)))

    def visitSumprodFunction(self, ctx):
        return math_funcs_module.sumprod(self.visit(ctx.expr(0)),
                                         self.visit(ctx.expr(1)))

    # ……… Special functions ………
    def visitErfFunction(self, ctx):
        return math_funcs_module.erf(self.visit(ctx.expr()))

    def visitErfcFunction(self, ctx):
        return math_funcs_module.erfc(self.visit(ctx.expr()))

    def visitGammaFunction(self, ctx):
        return math_funcs_module.gamma(self.visit(ctx.expr()))

    def visitLgammaFunction(self, ctx):
        return math_funcs_module.lgamma(self.visit(ctx.expr()))

    # ……… Constantes ………
    def visitPiValue(self, ctx):
        return math_funcs_module.pi()

    def visitEValue(self, ctx):
        return math_funcs_module.e()

    def visitTauConstant(self, ctx):
        return math_funcs_module.tau

    def visitInfConstant(self, ctx):
        return math_funcs_module.inf

    def visitNanConstant(self, ctx):
        return math_funcs_module.nan

    # ──────────────────── PLOT ────────────────────
    def visitGraph(self, ctx):
        return plotgraph(self, ctx, self.plot, self.ruta_programa)

    def visitXlabel(self, ctx):
        return set_xlabel(self, ctx, self.plot)

    def visitYlabel(self, ctx):
        return set_ylabel(self, ctx, self.plot)

    def visitTitle(self, ctx):
        return set_title(self, ctx, self.plot)

    def visitGrid(self, ctx):
        return set_grid(self, ctx, self.plot)

    def visitColor(self, ctx):
        return set_color(self, ctx, self.plot)

    def visitPointColor(self, ctx):
        return set_point_color(self, ctx, self.plot)

    def visitPointSize(self, ctx):
        return set_point_size(self, ctx, self.plot)

    def visitBar(self, ctx):
        return plot_bar(self, ctx, self.plot, self.ruta_programa)

    def visitBarValues(self, ctx):
        return set_bar_values(self, ctx, self.plot)

    def visitPie(self, ctx):
        return plot_pie(self, ctx, self.plot, self.ruta_programa)

    def visitLegend(self, ctx):
        return set_legend(self, ctx, self.plot)
