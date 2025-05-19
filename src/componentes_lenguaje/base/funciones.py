from ..global_utils import verificarHomogeneidad, asignar_variable

def varDecl(self, ctx):
    tipo = ctx.typeDecl().getText()
    if tipo == "VOID":
        raise TypeError("VOID cannot be used as variable type")

    name = ctx.ID().getText()
    val = None

    if ctx.expr():
        val = self.visit(ctx.expr())

    if name in self.variables:
        raise NameError(f"Variable '{name}' already defined")

    if val is None:
        if tipo == "INT":
            val = 0
        elif tipo == "FLOAT":
            val = 0.0
        elif tipo == "STR":
            val = ""
        elif tipo == "BOOL":
            val = False
        elif tipo.startswith("List"):
            val = []
        else:
            raise TypeError(f"Type '{tipo}' not recognized or missing default value")

    asignar_variable(self, name, val, tipo)


def assignStmt(self, ctx):
    id_text = ctx.ID().getText()
    valor = self.visit(ctx.expr())

    if id_text not in self.variables:
        raise NameError(f"Variable '{id_text}' not defined")

    tipo = self.variables[id_text][0]

    asignar_variable(self, id_text, valor, tipo)


def showStmt(self, ctx):
    print(self.visit(ctx.expr()))

def pourStmt(self, ctx):
    return input(self.visit(ctx.expr()))

def expr(self, ctx):
    resultado = self.visitChildren(ctx)

    if (type(resultado) == list):
        if (verificarHomogeneidad(resultado) == False):
            raise TypeError(f"Expected homogeneous list")

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
        raise Exception(f"Index must be an integer, got {type(index).__name__}")

    if type(collection) == str or type(collection) == list:
        try:
            return collection[index]
        except IndexError:
            raise Exception(f"Index {index} out of bounds for collection of size {len(collection)}")

def idExpr(self, ctx):
    id_text = ctx.ID().getText()

    if id_text in self.variables:
        return self.variables[id_text][1]

    raise NameError(f"Variable '{id_text}' not defined")

def indexedAssignStmt(self, ctx):
    nombre_lista = ctx.ID().getText()
    indexes = self.visit(ctx.indexing())

    for index in indexes:
        if type(index) != int:
            raise Exception(f"Index must be an integer, got {type(index).__name__}")

    _, lista = self.variables[nombre_lista]

    if nombre_lista not in self.variables:
        raise Exception(f"Variable '{nombre_lista}' not defined")

    nuevo_valor = self.visit(ctx.expr())
    tipo_nuevo_valor = self.obtener_tipo_dato(nuevo_valor)

    listaIndexada = lista
    for i in range(len(indexes) - 1):
       try:
            listaIndexada = listaIndexada[indexes[i]]
       except IndexError:
            raise Exception(f"Index {indexes[i]} out of bounds for collection of size {len(listaIndexada)}")

    ultimo_indice = indexes[len(indexes) - 1]
    try:
        anterior_valor = listaIndexada[ultimo_indice]
        tipo_anterior_valor = self.obtener_tipo_dato(anterior_valor)

        if tipo_nuevo_valor != tipo_anterior_valor:
            raise TypeError(f"Could not assign value of type {tipo_nuevo_valor} to variable of type '{tipo_anterior_valor}'")

        listaIndexada[ultimo_indice] = nuevo_valor
    except IndexError:
        raise Exception(f"Index {indexes[len(indexes) - 1]} out of bounds for collection of size {len(listaIndexada)}")
