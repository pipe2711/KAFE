# src/componentes_lenguaje/funciones/funciones.py

from TypeUtils import nombre_tipos
from ..errores import (
    raiseFunctionAlreadyDefined,
    raiseVoidAsParameterType,
    raiseWrongNumberOfArgs,
    raiseFunctionNotDefined
)
from Kafe_GrammarParser import Kafe_GrammarParser
from .utils import ReturnValue, check_value_type
from ..global_utils import asignar_variable

def functionDecl(self, ctx):
    name = ctx.ID().getText()

    # Verificación para evitar redefinición de funciones
    if name in self.variables:
        tipo_existente, _ = self.variables[name]
        if tipo_existente == nombre_tipos["func"]:
            raiseFunctionAlreadyDefined(name)

    # Extraer la única lista de parámetros
    if ctx.paramList():
        params = ctx.paramList().paramDecl()
    else:
        params = []

    retTyp = ctx.typeDecl().getText()
    for p in params:
        if (not isinstance(p, Kafe_GrammarParser.FunctionParamContext)
                and p.typeDecl().getText() == nombre_tipos["void"]):
            raiseVoidAsParameterType()

    body = ctx.block()
    outer = self

    class KafeFunction:
        def __init__(self, collected=None):
            self.collected = collected or []
            self.total = len(params)
            self.name = name  # Guardar el nombre para errores

        def __call__(self, *args):
            # 1) No exceder número de args
            if len(self.collected) + len(args) > self.total:
                raiseWrongNumberOfArgs(self.name, self.total, len(self.collected) + len(args))

            new_vals = self.collected + list(args)

            # 2) Currificación parcial: devolvemos otra función
            if len(new_vals) < self.total:
                return KafeFunction(new_vals)

            # 3) Validar tipos ahora que tenemos todos los args
            for decl, val in zip(params, new_vals):
                if not isinstance(decl, Kafe_GrammarParser.FunctionParamContext):
                    expected = decl.typeDecl().getText()
                    check_value_type(val, expected)

            # 4) Ejecutar cuerpo
            saved = dict(outer.variables)
            for decl, val in zip(params, new_vals):
                pid = decl.ID().getText()
                ptype = (
                    nombre_tipos["func"]
                    if isinstance(decl, Kafe_GrammarParser.FunctionParamContext)
                    else decl.typeDecl().getText()
                )
                asignar_variable(outer, pid, val, ptype)

            result = None
            try:
                outer.visit(body)
            except ReturnValue as rv:
                result = rv.value
            finally:
                outer.variables = saved

            # 5) Validar tipo de retorno
            check_value_type(result, retTyp)
            return result

    # Registrar la función
    self.variables[name] = (nombre_tipos["func"], KafeFunction())


def lambdaExpr(self, ctx):
    param = ctx.paramDecl()
    pid = param.ID().getText()
    ptype = param.typeDecl().getText()

    if ptype == nombre_tipos["func"]:
        raiseVoidAsParameterType()

    body = ctx.expr()
    captured = dict(self.variables)
    outer = self

    class LambdaFn:
        def __call__(self, val):
            # Verificar tipo del único parámetro
            check_value_type(val, ptype)

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

    children, i = list(ctx.getChildren()), 0
    while i < len(children):
        if children[i].getText() == '(':
            # llamada con argumentos
            if (i + 1 < len(children)
                    and isinstance(children[i + 1], Kafe_GrammarParser.ArgListContext)):
                args = [self.visit(a) for a in children[i + 1].arg()]
                func = func(*args)
                i += 3
            # llamada sin argumentos
            else:
                func = func()
                i += 2
        else:
            i += 1

    # — Se elimina la verificación de función parcial aquí
    return func


def returnStmt(self, ctx):
    raise ReturnValue(self.visit(ctx.expr()))
