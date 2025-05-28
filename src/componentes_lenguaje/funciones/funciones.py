from Kafe_GrammarParser import Kafe_GrammarParser

from TypeUtils import funcion_t, void_t, entero_t, todos_t, lista_cualquiera_t
from errores import (
    raiseFunctionAlreadyDefined, raiseVoidAsParameterType, raiseWrongNumberOfArgs, raiseFunctionNotDefined
)
from .utils import ReturnValue, check_value_type
from global_utils import asignar_variable, check_sig
from componentes_lenguaje.funciones.utils import ReturnValue, check_value_type

def functionDecl(self, ctx):
    name = ctx.ID().getText()

    if name in self.variables:
        tipo_existente, _ = self.variables[name]
        if tipo_existente == funcion_t:
            raiseFunctionAlreadyDefined(name)

    retTypCtx = ctx.typeDecl()
    if retTypCtx is None:
        retTyp = void_t
    else:
        retTyp = retTypCtx.getText()

    params = [p for pl in ctx.paramList() for p in pl.paramDecl()]
    for p in params:
        if (not isinstance(p, Kafe_GrammarParser.FunctionParamContext)
                and p.typeDecl() is not None and p.typeDecl().getText() == void_t):
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
                ptype = (funcion_t if isinstance(decl, Kafe_GrammarParser.FunctionParamContext)
                         else decl.typeDecl().getText())
                asignar_variable(outer, pid, val, ptype)
            result = None
            try:
                outer.dentro_bloque = True
                outer.visit(body)
            except ReturnValue as rv:
                result = rv.value
            finally:
                outer.variables = saved
            check_value_type(result, retTyp)

            outer.dentro_bloque = False
            return result

    # Si todo está bien, se guarda la función
    self.variables[name] = (funcion_t, KafeFunction())

def lambdaExpr(self, ctx):
    param = ctx.paramDecl()
    pid = param.ID().getText()
    ptype = param.typeDecl().getText()
    if ptype == funcion_t:
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
                outer.dentro_bloque = True
                res = outer.visit(body)
            finally:
                outer.variables = saved

            outer.dentro_bloque = False
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

@check_sig([2], lista_cualquiera_t, todos_t, func_nombre="append")
def visitAppendCall(lista, elem):
    lista.append(elem)

@check_sig([2], lista_cualquiera_t, todos_t, func_nombre="remove")
def visitRemoveCall(lista, elem):
    lista.remove(elem)
    return None

@check_sig([1], lista_cualquiera_t, func_nombre="len")
def visitLenCall(lista):
    return len(lista)

@check_sig([1, 2, 3], [entero_t], [entero_t], [entero_t], func_nombre="range")
def rangeExpr(*args):
    start = None
    stop = None
    step = None

    stop = args[0]

    if len(args) >= 2:
        start = args[0]
        stop = args[1]

    if len(args) == 3:
        step = args[2]

    if len(args) == 1:
        return list(range(stop))
    elif len(args) == 2:
        return list(range(start, stop))
    else:
        return list(range(start, stop, step))

def showStmt(self, ctx):
    print(self.visit(ctx.expr()))

def pourStmt(self, ctx):
    return input(self.visit(ctx.expr()))
