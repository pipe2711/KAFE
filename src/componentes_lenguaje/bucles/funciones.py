from TypeUtils import nombre_tipos, obtener_tipo_dato, obtener_tipo_dentro_lista
from ..errores import (
    raiseConditionMustBeBoolean, raiseExceededIterationCount, raiseNonIterableVariable
)

def whileLoop(self, ctx):
    cond = self.visit(ctx.expr())

    if not isinstance(cond, bool):
        raiseConditionMustBeBoolean("while", cond)
    max_iteraciones = 10000
    contador = 0
    while cond:
        self.visit(ctx.block())
        contador += 1
        if contador > max_iteraciones:
            raiseExceededIterationCount()
        cond = self.visit(ctx.expr())

        if not isinstance(cond, bool):
            raiseConditionMustBeBoolean("while", cond)

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
        self.visit(ctx.block())

    if var_name in self.variables:
        del self.variables[var_name]
