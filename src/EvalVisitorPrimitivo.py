from Kafe_GrammarVisitor import Kafe_GrammarVisitor

from componentes_lenguaje.librerias.funciones import libraryFunctionCall, libraryConstant
from componentes_lenguaje.base.funciones import additiveExpr, assignStmt, equalityExpr, expr, idExpr, indexedAssignStmt, indexingExpr, logicExpr, multiplicativeExpr, powerExpr, relationalExpr, unaryExpresion, varDecl
from componentes_lenguaje.bucles.funciones import forLoop, whileLoop
from componentes_lenguaje.condicionales.funciones import ifElseExpr
from componentes_lenguaje.funciones.funciones import  functionDecl, lambdaExpr, returnStmt, visitAppendCall,functionCall,visitRemoveCall,visitLenCall, rangeExpr, pourStmt, showStmt
from componentes_lenguaje.importar.funciones import importStmt
from componentes_lenguaje.method_calling.funciones import objectConstant, objectFunctionCall

from errores import raiseVariableNotDefined

import lib.KafeNUMK.funciones as numk_funcs_module
import lib.KafeMATH.funciones as math_funcs_module
import lib.KafeFILES.funciones as files_funcs_module
import lib.KafePLOT.funciones as plot_funcs_module
import lib.KafeGESHA.funciones as gesha_funcs_module
import lib.KafePARDOS.funciones as pardos_funcs_module

class EvalVisitorPrimitivo(Kafe_GrammarVisitor):
    def __init__(self):
        self.variables = {}
        self.dentro_bloque = False
        self.libraries = {
            "numk": [numk_funcs_module, False],
            "math": [math_funcs_module, False],
            "files": [files_funcs_module, False],
            "plot": [plot_funcs_module, False],
            "geshaDeep": [gesha_funcs_module, False],
            "pardos": [pardos_funcs_module, False]
        }
        self.imported = set()


    def visitSimpleImport(self, ctx): importStmt(self, ctx)

    def visitVarDecl(self, ctx): varDecl(self, ctx)

    def visitAssignStmt(self, ctx): assignStmt(self, ctx)

    def visitIndexedAssignStmt(self, ctx): indexedAssignStmt(self, ctx)

    def visitIndexing(self, ctx):
        indexes = [self.visit(expr) for expr in ctx.expr()]
        return indexes

    def visitFunctionDecl(self, ctx): return functionDecl(self, ctx)

    def visitFunctionCall(self, ctx): return functionCall(self,ctx)

    def visitAppendCall(self, ctx):
        lista = self.visit(ctx.expr(0))
        elem = self.visit(ctx.expr(1))
        return visitAppendCall(lista, elem)

    def visitRemoveCall(self, ctx):
        lista = self.visit(ctx.expr(0))
        elem = self.visit(ctx.expr(1))
        return visitRemoveCall(lista, elem)

    def visitLenCall(self, ctx):
        lista = self.visit(ctx.expr())
        return visitLenCall(lista)

    def visitLambdaExpr(self, ctx): return lambdaExpr(self, ctx)

    def visitLambdaExpresion(self, ctx): return self.visit(ctx.lambdaExpr())

    def visitReturnStmt(self, ctx): return returnStmt(self, ctx)

    def visitShowStmt(self, ctx): showStmt(self, ctx)

    def visitPourStmt(self, ctx): return pourStmt(self, ctx)

    def visitRangeExpr(self, ctx):
        rango = [self.visit(expr) for expr in ctx.expr()]
        return rangeExpr(*rango)


    def visitIfElseExpr(self, ctx): return ifElseExpr(self, ctx)


    def visitWhileLoop(self, ctx): whileLoop(self, ctx)

    def visitForLoop(self, ctx): forLoop(self, ctx)


    def visitExpr(self, ctx): return expr(self, ctx)

    def visitIndexingExpr(self, ctx): return indexingExpr(self, ctx)

    def visitLogicExpr(self, ctx): return logicExpr(self, ctx)

    def visitEqualityExpr(self, ctx): return equalityExpr(self, ctx)

    def visitRelationalExpr(self, ctx): return relationalExpr(self, ctx)

    def visitAdditiveExpr(self, ctx): return additiveExpr(self, ctx)

    def visitMultiplicativeExpr(self, ctx): return multiplicativeExpr(self, ctx)

    def visitPowerExpr(self, ctx): return powerExpr(self, ctx)

    def visitUnaryExpresion(self, ctx): return unaryExpresion(self, ctx)

    def visitParenExpr(self, ctx): return self.visitChildren(ctx.expr())

    def visitIdExpr(self, ctx): return idExpr(self, ctx)


    def visitIntLiteral(self, ctx): return int(ctx.getText())

    def visitFloatLiteral(self, ctx): return float(ctx.getText())

    def visitStringLiteral(self, ctx): return ctx.getText()[1:-1]

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

    def visitStrCastExpr(self, ctx): return str(self.visit(ctx.expr()))

    def visitBoolCastExpr(self, ctx): return bool(self.visit(ctx.expr()))

    def visitFloatCastExpr(self, ctx): return float(self.visit(ctx.expr()))

    def visitIntCastExpr(self, ctx): return int(self.visit(ctx.expr()))


    def visitObjectFunctionCall(self, ctx):
        object_name = ctx.ID(0).getText()
        function_name = ctx.ID(1).getText()
        args = [self.visit(e) for e in ctx.expr()]

        esLibreria = self.libraries.get(object_name) != None
        esVariable = self.variables.get(object_name) != None
        try:
            if esLibreria:
                return libraryFunctionCall(self.libraries.get(object_name), function_name, args)
            elif esVariable:
                return objectFunctionCall(self.variables[object_name][1], function_name, args)
            else:
                raiseVariableNotDefined(object_name)
        except Exception as e:
            raise Exception(f"{object_name}: {str(e)}")

    def visitObjectConstant(self, ctx):
        object_name = ctx.ID(0).getText()
        constant_name = ctx.ID(1).getText()

        esLibreria = self.libraries.get(object_name) != None
        esVariable = self.variables.get(object_name) != None
        if esLibreria:
            return libraryConstant(self.libraries.get(object_name), constant_name)
        elif esVariable:
            return objectConstant(self.variables[object_name][1], constant_name)
        else:
            raiseVariableNotDefined(object_name)
