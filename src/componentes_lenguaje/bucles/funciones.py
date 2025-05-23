from ..errores import (
    raiseConditionMustBeBoolean, raiseExceededIterationCount, raiseNonIterableVariable
)

def whileLoop(self, ctx):
    cond = self.visit(ctx.expr())

    if not isinstance(cond, bool):
        raiseConditionMustBeBoolean("while", self.obtener_tipo_dato(cond))
    max_iteraciones = 10000
    contador = 0
    while cond:
        self.visit(ctx.block())
        contador += 1
        if contador > max_iteraciones:
            raiseExceededIterationCount()
        cond = self.visit(ctx.expr())

        if not isinstance(cond, bool):
            raiseConditionMustBeBoolean("while", self.obtener_tipo_dato(cond))

def forLoop(self, ctx):
    var_name = ctx.ID().getText()
    iterable = self.visit(ctx.expr())

    tipo_iterable = self.obtener_tipo_dato(iterable)

    if type(iterable) == list:
        tipo_elemento = self.obtener_tipo_dentro_lista(iterable)
    elif tipo_iterable == self.nombre_tipos[str]:
        tipo_elemento = self.nombre_tipos[str]
    else:
        raiseNonIterableVariable(tipo_iterable)

    for item in iterable:
        self.variables[var_name] = (tipo_elemento, item)
        self.visit(ctx.block())

    if var_name in self.variables:
        del self.variables[var_name]
