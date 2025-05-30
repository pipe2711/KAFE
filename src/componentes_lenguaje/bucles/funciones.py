from TypeUtils import obtener_tipo_dato, obtener_tipo_dentro_lista, cadena_t
from errores import (
    raiseConditionMustBeBoolean, raiseExceededIterationCount, raiseNonIterableVariable
)
from componentes_lenguaje.funciones.utils import ReturnValue


def whileLoop(self, ctx):
    cond = self.visit(ctx.expr())

    if not isinstance(cond, bool):
        raiseConditionMustBeBoolean("while", cond)
    max_iteraciones = 10000
    contador = 0
    while cond:
        try:
            self.dentro_bloque = True
            self.visit(ctx.block())
        except ReturnValue as ret:
            self.dentro_bloque = False
            raise ret
        contador += 1
        if contador > max_iteraciones:
            raiseExceededIterationCount()
        cond = self.visit(ctx.expr())
        if not isinstance(cond, bool):
            raiseConditionMustBeBoolean("while", cond)

    self.dentro_bloque = False


def forLoop(self, ctx):
    var_name = ctx.ID().getText()
    iterable = self.visit(ctx.expr())

    tipo_iterable = obtener_tipo_dato(iterable)

    if type(iterable) == list:
        tipo_elemento = obtener_tipo_dentro_lista(iterable)
    elif tipo_iterable == cadena_t:
        tipo_elemento = cadena_t
    else:
        raiseNonIterableVariable(iterable)

    for item in iterable:
        self.variables[var_name] = (tipo_elemento, item)
        try:
            self.dentro_bloque = True
            self.visit(ctx.block())
        except ReturnValue as ret:
            self.dentro_bloque = False
            if var_name in self.variables:
                del self.variables[var_name]
            raise ret

    if var_name in self.variables:
        del self.variables[var_name]

    self.dentro_bloque = False
