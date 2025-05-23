import sys

from ..errores import (
    raiseFunctionAlreadyDefined, raiseVoidAsParameterType, raiseWrongNumberOfArgs, raiseFunctionNotDefined
)
sys.path.append("../..")
from Kafe_GrammarParser import Kafe_GrammarParser
from componentes_lenguaje.funciones.utils import ReturnValue, check_value_type
from componentes_lenguaje.global_utils import asignar_variable

def functionDecl(self, ctx):
    name = ctx.ID().getText()

    # Verificación para evitar redefinición de funciones
    if name in self.variables:
        tipo_existente, _ = self.variables[name]
        if tipo_existente == "FUNC":
            raiseFunctionAlreadyDefined(name)

    retTyp = ctx.typeDecl().getText()
    params = [p for pl in ctx.paramList() for p in pl.paramDecl()]
    for p in params:
        if (not isinstance(p, Kafe_GrammarParser.FunctionParamContext)
                and p.typeDecl().getText() == "VOID"):
            raiseVoidAsParameterType()
    body = ctx.block()
    outer = self

    class KafeFunction:
        def __init__(self, collected=None):
            self.collected = collected or []
            self.total = len(params)

        def __call__(self, *args):
            if len(self.collected) + len(args) > self.total:
                raiseWrongNumberOfArgs(name, self.total, len(self.collected) + len(args))
            new_vals = self.collected + list(args)
            if len(new_vals) < self.total:
                return KafeFunction(new_vals)
            saved = dict(outer.variables)
            for decl, val in zip(params, new_vals):
                pid = decl.ID().getText()
                ptype = ("FUNC" if isinstance(decl, Kafe_GrammarParser.FunctionParamContext)
                         else decl.typeDecl().getText())
                asignar_variable(outer, pid, val, ptype)
            result = None
            try:
                outer.visit(body)
            except ReturnValue as rv:
                result = rv.value
            finally:
                outer.variables = saved
            check_value_type(outer, result, retTyp)
            return result

    # Si todo está bien, se guarda la función
    self.variables[name] = ("FUNC", KafeFunction())


def lambdaExpr(self, ctx):
    param = ctx.paramDecl()
    pid = param.ID().getText()
    ptype = param.typeDecl().getText()
    if ptype == "VOID":
        raiseVoidAsParameterType()
    body = ctx.expr()
    captured = dict(self.variables)
    outer = self

    class LambdaFn:
        def __call__(self, val):
            local = dict(captured)
            saved = outer.variables
            outer.variables = local
            asignar_variable(outer, pid, val, ptype)
            try:
                res = outer.visit(body)
            finally:
                outer.variables = saved
            return res

    return LambdaFn()


def functionCall(self, ctx):
    name = ctx.ID().getText()
    if name not in self.variables:
        raiseFunctionNotDefined(name)
    func = self.variables[name][1]
    ch, i = list(ctx.getChildren()), 0
    while i < len(ch):
        if ch[i].getText() == '(':
            if (i + 1 < len(ch) and isinstance(ch[i + 1], Kafe_GrammarParser.ArgListContext)):
                args = [self.visit(a) for a in ch[i + 1].arg()]
                func = func(*args)
                i += 3
            else:
                func = func()
                i += 2
        else:
            i += 1
    if hasattr(func, "total") and len(func.collected) < func.total:
        raiseWrongNumberOfArgs(name, func.total, len(func.collected))
    return func


def returnStmt(self, ctx):
    raise ReturnValue(self.visit(ctx.expr()))
