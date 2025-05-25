from TypeUtils import nombre_tipos, obtener_tipo_dato, obtener_tipo_dentro_lista
from ..errores import (
    raiseConditionMustBeBoolean, raiseExceededIterationCount, raiseNonIterableVariable
)

from componentes_lenguaje.funciones.utils import ReturnValue, check_value_type


def whileLoop(self, ctx):
    cond = self.visit(ctx.expr())

    if not isinstance(cond, bool):
        raiseConditionMustBeBoolean("while", cond)
    max_iteraciones = 10000
    contador = 0
    while cond:
        try:
            self.visit(ctx.block())
        except ReturnValue as ret:
            raise ret
        contador += 1
        if contador > max_iteraciones:
            raiseExceededIterationCount()
        cond = self.visit(ctx.expr())
        if not isinstance(cond, bool):
            raiseConditionMustBeBoolean("while", cond)

    return None


def forLoop(self, ctx):
    var_name = ctx.ID().getText()
    iterable = self.visit(ctx.expr())

    tipo_iterable = obtener_tipo_dato(iterable)

    if type(iterable) == list:
        tipo_elemento = obtener_tipo_dentro_lista(iterable)
    elif tipo_iterable == nombre_tipos[str]:
        tipo_elemento = nombre_tipos[str]
    else:
        raiseNonIterableVariable(iterable)

    for item in iterable:
        self.variables[var_name] = (tipo_elemento, item)
        try:
            self.visit(ctx.block())
        except ReturnValue as ret:
            if var_name in self.variables:
                del self.variables[var_name]
            raise ret

    if var_name in self.variables:
        del self.variables[var_name]

    return None
