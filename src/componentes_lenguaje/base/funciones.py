from ..errores import (
    raiseFunctionIncorrectArgumentType, raiseVariableAlreadyDefined, raiseVariableNotDefined, raiseVoidAsVariableType,
    raiseExpectedHomogeneousList, raiseNonIntegerIndex, raiseIndexOutOfBounds, raiseTypeMismatch,raiseWrongNumberOfArgs
)
from TypeUtils import nombre_tipos, obtener_tipo_dato
from ..global_utils import esTipoCorrecto, verificarHomogeneidad, asignar_variable

def varDecl(self, ctx):
    tipo = ctx.typeDecl().getText()
    if tipo == nombre_tipos["void"]:
        raiseVoidAsVariableType()

    name = ctx.ID().getText()
    val = None

    if ctx.expr():
        val = self.visit(ctx.expr())

    if name in self.variables:
        raiseVariableAlreadyDefined(name)

    if val is None:
        if tipo == nombre_tipos[int]:
            val = 0
        elif tipo == nombre_tipos[float]:
            val = 0.0
        elif tipo == nombre_tipos[str]:
            val = ""
        elif tipo == nombre_tipos[bool]:
            val = False
        elif tipo.startswith(nombre_tipos[list]):
            val = []

    asignar_variable(self, name, val, tipo)


def assignStmt(self, ctx):
    id_text = ctx.ID().getText()
    valor = self.visit(ctx.expr())

    if id_text not in self.variables:
        raiseVariableNotDefined(id_text)

    tipo = self.variables[id_text][0]

    asignar_variable(self, id_text, valor, tipo)


def showStmt(self, ctx):
    val = self.visit(ctx.expr())
    if hasattr(val, 'total') and hasattr(val, 'collected') and len(val.collected) < val.total:
        raiseWrongNumberOfArgs(val.name, val.total, len(val.collected))
    print(val)

def pourStmt(self, ctx):
    return input(self.visit(ctx.expr()))

def expr(self, ctx):
    resultado = self.visitChildren(ctx)

    if (type(resultado) == list):
        if (verificarHomogeneidad(resultado) == False):
            raiseExpectedHomogeneousList()

    return resultado

def logicExpr(self, ctx):
    result = self.visit(ctx.equalityExpr(0))
    for i in range(1, len(ctx.equalityExpr())):
        op = ctx.getChild(2 * i - 1).getText()
        right = self.visit(ctx.equalityExpr(i))
        if op == '&&':
            result = result and right
        elif op == '||':
                result = result or right
    return result

def equalityExpr(self, ctx):
    result = self.visit(ctx.relationalExpr(0))
    for i in range(1, len(ctx.relationalExpr())):
        op = ctx.getChild(2 * i - 1).getText()
        right = self.visit(ctx.relationalExpr(i))
        if op == '==':
            result = result == right
        elif op == '!=':
            result = result != right
    return result

def relationalExpr(self, ctx):
    result = self.visit(ctx.additiveExpr(0))
    for i in range(1, len(ctx.additiveExpr())):
        op = ctx.getChild(2 * i - 1).getText()
        right = self.visit(ctx.additiveExpr(i))
        if op == '<':
            result = result < right
        elif op == '<=':
            result = result <= right
        elif op == '>':
            result = result > right
        elif op == '>=':
            result = result >= right
    return result

def additiveExpr(self, ctx):
    result = self.visit(ctx.multiplicativeExpr(0))
    for i in range(1, len(ctx.multiplicativeExpr())):
        op = ctx.getChild(2 * i - 1).getText()
        right = self.visit(ctx.multiplicativeExpr(i))
        if op == '+':
            result += right
        elif op == '-':
            result -= right
    return result

def multiplicativeExpr(self, ctx):
    result = self.visit(ctx.powerExpr(0))
    for i in range(1, len(ctx.powerExpr())):
        op = ctx.getChild(2 * i - 1).getText()
        right = self.visit(ctx.powerExpr(i))
        if op == '*':
            result *= right
        elif op == '/':
            result /= right
        elif op == '%':
            result %= right
    return result

def powerExpr(self, ctx):
   base = self.visit(ctx.unaryExpr(0))
   for i in range(1,len(ctx.unaryExpr())):
       base **= self.visit(ctx.unaryExpr(i))
   return base

def unaryExpresion(self, ctx):
   op = ctx.getChild(0).getText()
   value = self.visit(ctx.unaryExpr())
   if op == '-':
      return -value
   elif op == '!':
      return not value

def indexingExpr(self, ctx):
    collection = self.visit(ctx.primaryExpr())
    index = self.visit(ctx.expr())

    if type(index) != int:
        raiseNonIntegerIndex(index)

    if type(collection) == str or type(collection) == list:
        try:
            return collection[index]
        except IndexError:
            raiseIndexOutOfBounds(index, len(collection))

def idExpr(self, ctx):
    id_text = ctx.ID().getText()

    if id_text in self.variables:
        return self.variables[id_text][1]

    raiseVariableNotDefined(id_text)

def indexedAssignStmt(self, ctx):
    nombre_lista = ctx.ID().getText()
    indexes = self.visit(ctx.indexing())

    for index in indexes:
        if type(index) != int:
            raiseNonIntegerIndex(index)

    if nombre_lista not in self.variables:
        raiseVariableNotDefined(nombre_lista)

    _, lista = self.variables[nombre_lista]

    nuevo_valor = self.visit(ctx.expr())

    listaIndexada = lista
    for i in range(len(indexes) - 1):
        try:
            listaIndexada = listaIndexada[indexes[i]]
        except IndexError:
            raiseIndexOutOfBounds(indexes[i], len(listaIndexada))

    ultimo_indice = indexes[len(indexes) - 1]
    try:
        anterior_valor = listaIndexada[ultimo_indice]
        tipo_anterior_valor = obtener_tipo_dato(anterior_valor)

        if not esTipoCorrecto(nuevo_valor, tipo_anterior_valor):
            raiseTypeMismatch(nuevo_valor, tipo_anterior_valor)

        listaIndexada[ultimo_indice] = nuevo_valor
    except IndexError:
        raiseIndexOutOfBounds(ultimo_indice, len(listaIndexada))

def rangeExpr(self, ctx):
    start = None
    stop = None
    step = None

    stop = self.visit(ctx.expr(0))
    if type(stop) != int:
        raiseFunctionIncorrectArgumentType("range", stop, nombre_tipos[int])

    if ctx.expr(1) is not None:
        start = self.visit(ctx.expr(0))
        stop = self.visit(ctx.expr(1))

        if type(stop) != int:
            raiseFunctionIncorrectArgumentType("range", stop, nombre_tipos[int])

    if ctx.expr(2) is not None:
        step = self.visit(ctx.expr(2))
        if type(step) != int:
            raiseFunctionIncorrectArgumentType("range", step, nombre_tipos[int])

    if ctx.expr(1) is None:
        return list(range(stop))
    elif ctx.expr(2) is None:
        return list(range(start, stop))
    else:
        return list(range(start, stop, step))
