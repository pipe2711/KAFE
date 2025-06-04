from lib.KafeGESHA.Gesha import Gesha
from errores import (
     raiseVariableAlreadyDefined, raiseVariableNotDefined, raiseVoidAsVariableType,
     raiseExpectedHomogeneousList, raiseNonIntegerIndex, raiseIndexOutOfBounds, raiseTypeMismatch
)
from TypeUtils import  obtener_tipo_dato, entero_t, flotante_t, cadena_t, booleano_t, lista_t, void_t, gesha_t
from global_utils import esTipoCorrecto, verificarHomogeneidad, asignar_variable

def varDecl(self, ctx):
    tipo = ctx.typeDecl().getText()
    if tipo == void_t:
        raiseVoidAsVariableType()

    name = ctx.ID().getText()
    val = None

    if ctx.expr():
        val = self.visit(ctx.expr())

    if name in self.variables and not self.dentro_bloque:
        raiseVariableAlreadyDefined(name)

    if val is None:
        if tipo == entero_t:
            val = 0
        elif tipo == flotante_t:
            val = 0.0
        elif tipo == cadena_t:
            val = ""
        elif tipo == booleano_t:
            val = False
        elif tipo == gesha_t:
            val = Gesha()
        elif tipo.startswith(lista_t):
            val = []

    asignar_variable(self, name, val, tipo)


def assignStmt(self, ctx):
    id_text = ctx.ID().getText()
    valor = self.visit(ctx.expr())

    if id_text not in self.variables:
        raiseVariableNotDefined(id_text)

    tipo = self.variables[id_text][0]

    asignar_variable(self, id_text, valor, tipo)


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
