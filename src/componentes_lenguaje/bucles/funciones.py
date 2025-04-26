from ..global_utils import obtener_tipo_lista

def whileLoop(self, ctx):
    cond = self.visit(ctx.expr())
    if not isinstance(cond, bool):
        raise TypeError(f"Condition in 'while' must be boolean, got {type(cond).__name__}")
    max_iteraciones = 10000 
    contador = 0
    while cond:
        try:
            self.visit(ctx.block())
        except Exception as e:
            raise RuntimeError(f"Error in 'while' block: {str(e)}")
        contador += 1
        if contador > max_iteraciones:
            raise RuntimeError("Maximum number of iterations exceeded in 'while' loop (possible infinite loop)")
        cond = self.visit(ctx.expr())

        if not isinstance(cond, bool):
            raise TypeError(f"Condition in 'while' must be boolean, got {type(cond).__name__} on iteration {contador}")

def forLoop(self, ctx):
    var_name = ctx.ID().getText()
    iterable = self.visit(ctx.expr())

    if isinstance(iterable, list):
        try:
            tipo_elemento = obtener_tipo_lista(iterable, self.nombre_tipos).replace("List[", "").replace("]", "")
        except Exception as e:
            raise RuntimeError(f"Error determining type of iterable: {str(e)}")
    elif isinstance(iterable, str):
        tipo_elemento = self.nombre_tipos[str]
    else:
        raise TypeError(f"Variable in 'for' must be iterable (list or string), got {type(iterable).__name__}")

    for item in iterable:
        try:
            self.variables[var_name] = (tipo_elemento, item)
            self.visit(ctx.block())
        except Exception as e:
            raise RuntimeError(f"Error in 'for' block: {str(e)}")

    if var_name in self.variables:
       del self.variables[var_name]
