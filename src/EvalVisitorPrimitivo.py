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
    def visitSimpleImport(self, ctx):
        importStmt(self, ctx)

    # ===== NUMK LIBRARY =====
    def visitImportNUMK(self, ctx):
        self.numk = Numk()

    # ===== PLOT LIBRARY =====
    def visitImportPLOT(self, ctx):
        self.plot = Plot()

    # ===== MATH LIBRARY =====
    def visitImportMATH(self, ctx):
        from lib.KafeMATH.funciones import (
            pi, e,
            exp, exp2, expm1, log, log2, log10,
            pow_, cbrt, sqrt,
            degrees, radians,
            sin, cos, tan,
            asin, acos, atan,
            sinh, cosh, tanh,
            factorial, comb, perm, gcd, lcm,
            trunc, fmod, remainder,
            math_abs, floor, ceil, math_round,
            copysign, isclose, isfinite, isinf, isnan, ulp,
            sum_range, prod_range, dist, fsum, hypot, prod, sumprod,
            erf, erfc, gamma, lgamma,
            tau, inf, nan
        )
        # Populate math functions
        self.math_funcs = {
            'pi': pi, 'e': e,
            'exp': exp, 'exp2': exp2, 'expm1': expm1,
            'log': log, 'log2': log2, 'log10': log10,
            'pow': pow_, 'cbrt': cbrt, 'sqrt': sqrt,
            'degrees': degrees, 'radians': radians,
            'sin': sin, 'cos': cos, 'tan': tan,
            'asin': asin, 'acos': acos, 'atan': atan,
            'sinh': sinh, 'cosh': cosh, 'tanh': tanh,
            'factorial': factorial, 'comb': comb, 'perm': perm,
            'gcd': gcd, 'lcm': lcm,
            'trunc': trunc, 'fmod': fmod, 'remainder': remainder,
            'abs': math_abs, 'floor': floor, 'ceil': ceil, 'round': math_round,
            'copysign': copysign, 'isclose': isclose, 'isfinite': isfinite,
            'isinf': isinf, 'isnan': isnan, 'ulp': ulp,
            'sum': sum_range, 'prod': prod_range,
            'dist': dist, 'fsum': fsum, 'hypot': hypot, 'prod_list': prod, 'sumprod': sumprod,
            'erf': erf, 'erfc': erfc, 'gamma': gamma, 'lgamma': lgamma
        }
        # Constants for idExpr
        self.variables['tau'] = (self.nombre_tipos[type(tau)], tau)
        self.variables['inf'] = (self.nombre_tipos[type(inf)], inf)
        self.variables['nan'] = (self.nombre_tipos[type(nan)], nan)
        # Wrapper for unified prod()
        def prod_wrapper(*p_args):
            if len(p_args) == 1 and isinstance(p_args[0], list):
                return prod(p_args[0])
            if len(p_args) == 2 and all(isinstance(x, (int, float)) for x in p_args):
                return prod_range(p_args[0], p_args[1])
            raise TypeError(f"prod() expects 1 iterable or 2 numeric args, got {len(p_args)}")
        self.math_funcs['prod'] = prod_wrapper

    # ===== VARIABLES =====
    def visitVarDecl(self, ctx): return varDecl(self, ctx)
    def visitAssignStmt(self, ctx): return assignStmt(self, ctx)

    # ===== FUNCTIONS =====
    def visitFunctionDecl(self, ctx): return functionDecl(self, ctx)
    def visitFunctionCall(self, ctx):
        name = ctx.ID().getText()
        if name in self.math_funcs:
            args = []
            for al in ctx.argList() or []:
                for argu in al.arg():
                    if argu.expr(): args.append(self.visit(argu.expr()))
                    else: args.append(self.visit(argu.lambdaExpr()))
            return self.math_funcs[name](*args)
        return functionCall(self, ctx)

    def visitLambdaExpr(self, ctx): return lambdaExpr(self, ctx)
    def visitLambdaExpresion(self, ctx): return self.visit(ctx.lambdaExpr())
    def visitReturnStmt(self, ctx): return returnStmt(self, ctx)
    def visitShowStmt(self, ctx): showStmt(self, ctx)
    def visitPourStmt(self, ctx): return pourStmt(self, ctx)

    # ===== CONTROL FLOW =====
    def visitIfElseExpr(self, ctx): return ifElseExpr(self, ctx)
    def visitWhileLoop(self, ctx): whileLoop(self, ctx)
    def visitForLoop(self, ctx): forLoop(self, ctx)

    # ===== EXPRESSIONS =====
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

    # ===== NUMK OPERATIONS =====
    def visitNumkadd(self, ctx): return numkadd(self, ctx, self.numk) if self.numk else (_ for _ in ()).throw(Exception('numk library not imported'))
    def visitNumksub(self, ctx): return numksub(self, ctx, self.numk) if self.numk else (_ for _ in ()).throw(Exception('numk library not imported'))
    def visitNumkmul(self, ctx): return numkmul(self, ctx, self.numk) if self.numk else (_ for _ in ()).throw(Exception('numk library not imported'))
    def visitNumkinv(self, ctx): return numkinv(self, ctx, self.numk) if self.numk else (_ for _ in ()).throw(Exception('numk library not imported'))
    def visitNumktranspose(self, ctx): return numktranspose(self, ctx, self.numk) if self.numk else (_ for _ in ()).throw(Exception('numk library not imported'))

    # ===== PLOT LIBRARY =====
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

    # ===== INTERNAL MATH =====
    def _visit_math(self, ctx):
        exprs = ctx.getTypedRuleContexts(Kafe_GrammarParser.ExprContext)
        args = [self.visit(c) for c in exprs]
        name = ctx.getChild(0).getText()
        if name not in self.math_funcs:
            raise Exception(f"Math function '{name}' not imported")
        return self.math_funcs[name](*args)

# Monkey-patch for mathLibrary rules
for _attr in dir(Kafe_GrammarVisitor):
    if _attr.startswith('visit') and (_attr.endswith('Function') or _attr.endswith('Constant')):
        setattr(EvalVisitorPrimitivo, _attr, EvalVisitorPrimitivo._visit_math)
