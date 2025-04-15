from Kafe_GrammarVisitor import Kafe_GrammarVisitor
from Kafe_GrammarParser import Kafe_GrammarParser
from utils import obtener_tipo_lista, verificarHomogeneidad

# --- Clases de ayuda para funciones y return ---

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class UserFunction:
    """
    Clase que representa una función definida por el usuario.
    Se almacena la lista de parámetros (se asume para este ejemplo una única lista de parámetros),
    el bloque (ctx) a ejecutar y el entorno (closure) del momento de su declaración.
    
    Se ha modificado el método __call__ para admitir currificación:
    - Si se suministran menos argumentos que los requeridos, se retorna una función parcial que
      espera los argumentos faltantes.
    """
    def __init__(self, param_lists, block, closure, visitor):
        self.param_lists = param_lists      # lista de listas de parámetros (cada parámetro es una tupla (nombre, tipo))
        self.block = block                  # bloque de código (ctx) a ejecutar
        self.closure = closure.copy()       # entorno (closure) al momento de la declaración
        self.visitor = visitor              # referencia al evaluador

    def __call__(self, *args):
        # Soporta únicamente una lista de parámetros.
        if len(self.param_lists) != 1:
            raise NotImplementedError("Soporta únicamente una lista de parámetros.")
        params = self.param_lists[0]
        required = len(params)
        provided = len(args)

        if provided > required:
            raise TypeError(f"Expected at most {required} arguments, got {provided}")
        
        # Currificación: si no se han suministrado todos los argumentos, retorna una función que acumula más.
        if provided < required:
            return lambda *more_args: self(*(args + more_args))
        
        # Si se suministraron todos los argumentos, ejecutar la función.
        old_env = self.visitor.variables.copy()
        # Se crea un entorno basado en el closure de la función.
        self.visitor.variables = self.closure.copy()

        # Asignación de cada parámetro en el entorno de la función.
        for (param_name, param_type), arg in zip(params, args):
            if param_type in self.visitor.type_mapping:
                expected_type = self.visitor.type_mapping[param_type]
                if type(arg) != expected_type:
                    raise TypeError(f"Expected type {param_type} for parameter '{param_name}', got {str.upper(type(arg).__name__)}")
            self.visitor.variables[param_name] = (param_type, arg)
        try:
            self.visitor.visit(self.block)
        except ReturnValue as rv:
            result = rv.value
            self.visitor.variables = old_env  # restaurar entorno original
            return result
        self.visitor.variables = old_env
        return None

# --- Fin de clases de ayuda ---

class EvalVisitorPrimitivo(Kafe_GrammarVisitor):
    def __init__(self):
        self.variables = {}
        self.type_mapping = {
            "INT": int,
            "FLOAT": float,
            "STR": str,
            "BOOL": bool
        }

    def asignar_variable(self, id_text, valor, tipo):
        variable_asignada = True
        if tipo in self.type_mapping:
            expected_type = self.type_mapping[tipo]
            if type(valor) != expected_type:
                raise TypeError(f"Expected {tipo}, obtained {str.upper(type(valor).__name__)}")
            self.variables[id_text] = (tipo, valor)
        elif tipo.startswith("List") and any(t in tipo for t in ["INT", "FLOAT", "STR", "BOOL"]):
            tipo_valor = obtener_tipo_lista(valor)
            tipo_base = tipo.replace("INT", '').replace("FLOAT", '').replace("STR", '').replace("BOOL", '')
            if not verificarHomogeneidad(valor):
                raise TypeError("Expected homogeneous list")
            if tipo != tipo_valor and tipo_base != tipo_valor and valor != []:
                raise TypeError(f"Expected {tipo}, obtained {tipo_valor}")
            self.variables[id_text] = (tipo, valor)
        else:
            variable_asignada = False
        return variable_asignada

    # ----------------------------------------------------------------------
    #   MODIFICACIONES: funciones, lambdas, return, import y llamadas a función
    # ----------------------------------------------------------------------
    
    def visitImportStmt(self, ctx:Kafe_GrammarParser.ImportStmtContext):
        module_name = ctx.ID().getText()
        filename = f"{module_name}.kf"
        try:
            with open(filename, "r") as f:
                code = f.read()
        except FileNotFoundError:
            raise Exception(f"Module '{filename}' not found.")
        from antlr4 import InputStream, CommonTokenStream
        from Kafe_GrammarLexer import Kafe_GrammarLexer
        from Kafe_GrammarParser import Kafe_GrammarParser
        input_stream = InputStream(code)
        lexer = Kafe_GrammarLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = Kafe_GrammarParser(tokens)
        tree = parser.program()
        self.visit(tree)

    def visitFunctionDecl(self, ctx:Kafe_GrammarParser.FunctionDeclContext):
        func_name = ctx.ID().getText()
        if func_name in self.variables:
            raise NameError(f"Function '{func_name}' already defined")
        param_lists = []
        # Procesar el primer grupo de parámetros (si existe)
        if ctx.paramList():
            for param_ctx in ctx.paramList():
                params = []
                for param in param_ctx.paramDecl():
                    param_name = param.ID().getText()
                    param_type = param.typeDecl().getText()
                    params.append((param_name, param_type))
                param_lists.append(params)
        else:
            param_lists.append([])
        block = ctx.block()
        func_obj = UserFunction(param_lists, block, self.variables, self)
        self.variables[func_name] = ("FUNC", func_obj)

    def visitReturnStmt(self, ctx:Kafe_GrammarParser.ReturnStmtContext):
        value = self.visit(ctx.expr())
        raise ReturnValue(value)

    def _create_lambda(self, ctx):
        # Se asume que la regla lambdaExpr es: '(' paramDecl ')' ARROW expr
        param_decl = ctx.paramDecl()
        param_name = param_decl.ID().getText()
        param_type = param_decl.typeDecl().getText()
        expr_ctx = ctx.expr()
        def lambda_func(arg):
            if param_type in self.type_mapping:
                expected_type = self.type_mapping[param_type]
                if type(arg) != expected_type:
                    raise TypeError(f"Expected type {param_type} for parameter '{param_name}', got {str.upper(type(arg).__name__)}")
            old = self.variables.get(param_name)
            self.variables[param_name] = (param_type, arg)
            try:
                return self.visit(expr_ctx)
            finally:
                if old is None:
                    del self.variables[param_name]
                else:
                    self.variables[param_name] = old
        return lambda_func

    def visitLambdaExpr(self, ctx:Kafe_GrammarParser.LambdaExprContext):
        return self._create_lambda(ctx)
    
    def visitLambdaExpresion(self, ctx:Kafe_GrammarParser.LambdaExpresionContext):
        return self._create_lambda(ctx)
    
    # --- Actualización en llamadas a función y lista de argumentos ---

    def visitArgList(self, ctx:Kafe_GrammarParser.ArgListContext):
        # Evaluar cada argumento definido en la lista.
        return [ self.visit(arg_ctx) for arg_ctx in ctx.arg() ]
    
    def visitFunctionCall(self, ctx:Kafe_GrammarParser.FunctionCallContext):
        func_name = ctx.ID().getText()
        if func_name not in self.variables:
            raise NameError(f"Function '{func_name}' not defined")
        tipo, func_obj = self.variables[func_name]
        if tipo != "FUNC":
            raise TypeError(f"Variable '{func_name}' is not callable")
        # Evaluar argumentos (si existen)
        args = self.visit(ctx.argList()) if ctx.argList() else []
        return func_obj(*args)
    # ----------------------------------------------------------------------
    # Fin de modificaciones sobre funciones, lambdas, return, import y llamadas.
    # ----------------------------------------------------------------------
    
    def visitVarDecl(self, ctx:Kafe_GrammarParser.VarDeclContext):
        tipo = ctx.typeDecl().getText()
        id_text = ctx.ID().getText()
        valor = self.visit(ctx.expr())
        if id_text in self.variables:
            raise NameError(f"Variable '{id_text}' already defined")
        if tipo == "VOID":
            raise TypeError("Cannot declare variable with type VOID")
        variable_asignada = self.asignar_variable(id_text, valor, tipo)
        if not variable_asignada:
            raise TypeError(f"Type '{tipo}' not recognized")

    def visitAssignStmt(self, ctx:Kafe_GrammarParser.AssignStmtContext):
        id_text = ctx.ID().getText()
        valor = self.visit(ctx.expr())
        if id_text not in self.variables:
            raise NameError(f"Variable '{id_text}' not defined")
        tipo = self.variables[id_text][0]
        variable_asignada = self.asignar_variable(id_text, valor, tipo)
        if not variable_asignada:
            raise TypeError(f"Cannot assign value to variable '{id_text}' of type '{tipo}'")

    def visitFunctionParam(self, ctx:Kafe_GrammarParser.FunctionParamContext):
        return self.visitChildren(ctx)

    def visitParamList(self, ctx:Kafe_GrammarParser.ParamListContext):
        return self.visitChildren(ctx)

    def visitSimpleParam(self, ctx:Kafe_GrammarParser.SimpleParamContext):
        return self.visitChildren(ctx)

    def visitShowStmt(self, ctx:Kafe_GrammarParser.ShowStmtContext):
        print(self.visit(ctx.expr()))

    def visitPourStmt(self, ctx:Kafe_GrammarParser.PourStmtContext):
        return input(self.visit(ctx.expr()))

    def visitIfElseExpr(self, ctx:Kafe_GrammarParser.IfElseExprContext):
        return self.visitChildren(ctx)

    def visitWhileLoop(self, ctx:Kafe_GrammarParser.WhileLoopContext):
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

    def visitForLoop(self, ctx:Kafe_GrammarParser.ForLoopContext):
        var_name = ctx.ID().getText()
        iterable = self.visit(ctx.expr())
        if isinstance(iterable, list):
            try:
                tipo_elemento = obtener_tipo_lista(iterable).replace("List[", "").replace("]", "")
            except Exception as e:
                raise RuntimeError(f"Error determining type of iterable: {str(e)}")
        elif isinstance(iterable, str):
            tipo_elemento = "STR"
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

    def visitMatchExpr(self, ctx:Kafe_GrammarParser.MatchExprContext):
        return self.visitChildren(ctx)

    def visitMatchCase(self, ctx:Kafe_GrammarParser.MatchCaseContext):
        return self.visitChildren(ctx)

    def visitLiteralPattern(self, ctx:Kafe_GrammarParser.LiteralPatternContext):
        return self.visitChildren(ctx)

    def visitWildcardPattern(self, ctx:Kafe_GrammarParser.WildcardPatternContext):
        return self.visitChildren(ctx)

    def visitIdPattern(self, ctx:Kafe_GrammarParser.IdPatternContext):
        return self.visitChildren(ctx)

    def visitBlock(self, ctx:Kafe_GrammarParser.BlockContext):
        return self.visitChildren(ctx)

    def visitExpr(self, ctx:Kafe_GrammarParser.ExprContext):
        return self.visitChildren(ctx)

    def visitLogicExpr(self, ctx:Kafe_GrammarParser.LogicExprContext):
        result = self.visit(ctx.equalityExpr(0))
        for i in range(1, len(ctx.equalityExpr())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.equalityExpr(i))
            if op == '&&':
                result = result and right
            elif op == '||':
                result = result or right
        return result

    def visitEqualityExpr(self, ctx:Kafe_GrammarParser.EqualityExprContext):
        result = self.visit(ctx.relationalExpr(0))
        for i in range(1, len(ctx.relationalExpr())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.relationalExpr(i))
            if op == '==':
                result = result == right
            elif op == '!=':
                result = result != right
        return result

    def visitRelationalExpr(self, ctx:Kafe_GrammarParser.RelationalExprContext):
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

    def visitAdditiveExpr(self, ctx:Kafe_GrammarParser.AdditiveExprContext):
        result = self.visit(ctx.multiplicativeExpr(0))
        for i in range(1, len(ctx.multiplicativeExpr())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.multiplicativeExpr(i))
            if op == '+':
                result += right
            elif op == '-':
                result -= right
        return result

    def visitMultiplicativeExpr(self, ctx:Kafe_GrammarParser.MultiplicativeExprContext):
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

    def visitPowerExpr(self, ctx:Kafe_GrammarParser.PowerExprContext):
        base = self.visit(ctx.unaryExpr(0))
        for i in range(1, len(ctx.unaryExpr())):
            exponent = self.visit(ctx.unaryExpr(i))
            base = base ** exponent
        return base

    def visitUnaryExpresion(self, ctx:Kafe_GrammarParser.UnaryExpresionContext):
        op = ctx.getChild(0).getText()
        value = self.visit(ctx.unaryExpr())
        if op == '-':
            return -value
        elif op == '!':
            return not value

    def visitPrimaryExpresion(self, ctx:Kafe_GrammarParser.PrimaryExpresionContext):
        return self.visitChildren(ctx)

    def visitLiteralExpr(self, ctx:Kafe_GrammarParser.LiteralExprContext):
        return self.visitChildren(ctx)

    def visitIndexingExpr(self, ctx:Kafe_GrammarParser.IndexingExprContext):
        collection = self.visit(ctx.primaryExpr())
        index = self.visit(ctx.expr())
        if type(index) != int:
            raise Exception(f"Index must be an integer, got {type(index).__name__}")
        if type(collection) == str or type(collection) == list:
            try:
                return collection[index]
            except IndexError:
                raise Exception(f"Index {index} out of bounds for collection of size {len(collection)}")
        else:
            raise Exception(f"Type {type(collection).__name__} is not indexable")

    def visitParenExpr(self, ctx:Kafe_GrammarParser.ParenExprContext):
        return self.visitChildren(ctx.expr())

    def visitIdExpr(self, ctx:Kafe_GrammarParser.IdExprContext):
        id_text = ctx.ID().getText()
        if id_text in self.variables:
            return self.variables[id_text][1]
        raise NameError(f"Variable '{id_text}' not defined")
    
    def visitIntLiteral(self, ctx:Kafe_GrammarParser.IntLiteralContext):
        return int(ctx.getText())

    def visitFloatLiteral(self, ctx:Kafe_GrammarParser.FloatLiteralContext):
        return float(ctx.getText())

    def visitStringLiteral(self, ctx:Kafe_GrammarParser.StringLiteralContext):
        return ctx.getText()[1:-1]

    def visitBoolLiteral(self, ctx:Kafe_GrammarParser.BoolLiteralContext):
        return False if ctx.getText() == "False" else True

    def visitListLiteral(self, ctx:Kafe_GrammarParser.ListLiteralContext):
        lista = []
        for expr in ctx.expr():
            valor = self.visit(expr)
            lista.append(valor)
        return lista

    def visitStrCastExpr(self, ctx:Kafe_GrammarParser.StrCastExprContext):
        return str(self.visit(ctx.expr()))

    def visitBoolCastExpr(self, ctx:Kafe_GrammarParser.BoolCastExprContext):
        return bool(self.visit(ctx.expr()))

    def visitFloatCastExpr(self, ctx:Kafe_GrammarParser.FloatCastExprContext):
        return float(self.visit(ctx.expr()))

    def visitIntCastExpr(self, ctx:Kafe_GrammarParser.IntCastExprContext):
        return int(self.visit(ctx.expr()))
