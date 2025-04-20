# EvalVisitorPrimitivo.py
from Kafe_GrammarVisitor import Kafe_GrammarVisitor
from Kafe_GrammarParser import Kafe_GrammarParser
from utils import obtener_tipo_lista, verificarHomogeneidad

class ReturnValue(Exception):
    def __init__(self, value):
        super().__init__()
        self.value = value

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
            expected = self.type_mapping[tipo]
            if type(valor) is not expected:
                raise TypeError(f"Expected {tipo}, obtained {type(valor).__name__.upper()}")
            self.variables[id_text] = (tipo, valor)
        elif tipo.startswith("List") and any(t in tipo for t in ["INT","FLOAT","STR","BOOL"]):
            tipo_valor = obtener_tipo_lista(valor)
            tipo_base  = tipo.replace("INT","").replace("FLOAT","").replace("STR","").replace("BOOL","")
            if not verificarHomogeneidad(valor):
                raise TypeError("Expected homogeneous list")
            if tipo != tipo_valor and tipo_base != tipo_valor and valor != []:
                raise TypeError(f"Expected {tipo}, obtained {tipo_valor}")
            self.variables[id_text] = (tipo, valor)
        else:
            variable_asignada = False
        return variable_asignada

    def visitImportStmt(self, ctx): return self.visitChildren(ctx)
    def visitParamList(self, ctx): return self.visitChildren(ctx)
    def visitSimpleParam(self, ctx): return self.visitChildren(ctx)
    def visitFunctionParam(self, ctx): return self.visitChildren(ctx)
    def visitIfElseExpr(self, ctx): return self.visitChildren(ctx)
    def visitMatchExpr(self, ctx): return self.visitChildren(ctx)
    def visitMatchCase(self, ctx): return self.visitChildren(ctx)
    def visitLiteralPattern(self, ctx): return self.visitChildren(ctx)
    def visitWildcardPattern(self, ctx): return self.visitChildren(ctx)
    def visitIdPattern(self, ctx): return self.visitChildren(ctx)
    def visitBlock(self, ctx): return self.visitChildren(ctx)
    def visitExpr(self, ctx): return self.visitChildren(ctx)
    def visitFunctionCallExpr(self, ctx): return self.visitChildren(ctx)
    def visitLambdaExpresion(self, ctx): return self.visitChildren(ctx)
    def visitExprArgument(self, ctx): return self.visitChildren(ctx)
    def visitLambdaArgument(self, ctx): return self.visitChildren(ctx)

    def visitVarDecl(self, ctx:Kafe_GrammarParser.VarDeclContext):
        tipo  = ctx.typeDecl().getText()
        name  = ctx.ID().getText()
        value = self.visit(ctx.expr())
        if name in self.variables:
            raise NameError(f"Variable '{name}' already defined")
        if tipo == "VOID":
            raise TypeError("Cannot declare variable with type VOID")
        if not self.asignar_variable(name, value, tipo):
            raise TypeError(f"Type '{tipo}' not recognized")

    def visitAssignStmt(self, ctx:Kafe_GrammarParser.AssignStmtContext):
        name  = ctx.ID().getText()
        value = self.visit(ctx.expr())
        if name not in self.variables:
            raise NameError(f"Variable '{name}' not defined")
        tipo = self.variables[name][0]
        if not self.asignar_variable(name, value, tipo):
            raise TypeError(f"Cannot assign to '{name}' of type '{tipo}'")

    def visitReturnStmt(self, ctx:Kafe_GrammarParser.ReturnStmtContext):
        value = self.visit(ctx.expr())
        raise ReturnValue(value)

    def visitShowStmt(self, ctx:Kafe_GrammarParser.ShowStmtContext):
        print(self.visit(ctx.expr()))

    def visitPourStmt(self, ctx:Kafe_GrammarParser.PourStmtContext):
        return input(self.visit(ctx.expr()))

    def visitWhileLoop(self, ctx:Kafe_GrammarParser.WhileLoopContext):
        cond = self.visit(ctx.expr())
        if not isinstance(cond, bool):
            raise TypeError(f"'while' condition must be bool, got {type(cond).__name__}")
        count, max_it = 0, 10000
        while cond:
            self.visit(ctx.block())
            count += 1
            if count > max_it:
                raise RuntimeError("Possible infinite loop")
            cond = self.visit(ctx.expr())

    def visitForLoop(self, ctx:Kafe_GrammarParser.ForLoopContext):
        name     = ctx.ID().getText()
        iterable = self.visit(ctx.expr())
        if isinstance(iterable, list):
            elem_t = obtener_tipo_lista(iterable).replace("List[","").replace("]","")
        elif isinstance(iterable, str):
            elem_t = "STR"
        else:
            raise TypeError(f"'for' expects iterable, got {type(iterable).__name__}")
        for item in iterable:
            self.variables[name] = (elem_t, item)
            self.visit(ctx.block())
        self.variables.pop(name, None)

    def visitLogicExpr(self, ctx:Kafe_GrammarParser.LogicExprContext):
        res = self.visit(ctx.equalityExpr(0))
        for i in range(1, len(ctx.equalityExpr())):
            op, right = ctx.getChild(2*i-1).getText(), self.visit(ctx.equalityExpr(i))
            res = res and right if op=='&&' else res or right
        return res

    def visitEqualityExpr(self, ctx:Kafe_GrammarParser.EqualityExprContext):
        res = self.visit(ctx.relationalExpr(0))
        for i in range(1, len(ctx.relationalExpr())):
            op, right = ctx.getChild(2*i-1).getText(), self.visit(ctx.relationalExpr(i))
            res = (res == right) if op=='==' else (res != right)
        return res

    def visitRelationalExpr(self, ctx:Kafe_GrammarParser.RelationalExprContext):
        res = self.visit(ctx.additiveExpr(0))
        for i in range(1, len(ctx.additiveExpr())):
            op, right = ctx.getChild(2*i-1).getText(), self.visit(ctx.additiveExpr(i))
            if op=='<':  res = res < right
            elif op=='<=': res = res <= right
            elif op=='>':  res = res > right
            else:          res = res >= right
        return res

    def visitAdditiveExpr(self, ctx:Kafe_GrammarParser.AdditiveExprContext):
        res = self.visit(ctx.multiplicativeExpr(0))
        for i in range(1, len(ctx.multiplicativeExpr())):
            op, right = ctx.getChild(2*i-1).getText(), self.visit(ctx.multiplicativeExpr(i))
            res = res + right if op=='+' else res - right
        return res

    def visitMultiplicativeExpr(self, ctx:Kafe_GrammarParser.MultiplicativeExprContext):
        res = self.visit(ctx.powerExpr(0))
        for i in range(1, len(ctx.powerExpr())):
            op, right = ctx.getChild(2*i-1).getText(), self.visit(ctx.powerExpr(i))
            if op=='*': res *= right
            elif op=='/': res /= right
            else:        res %= right
        return res

    def visitPowerExpr(self, ctx:Kafe_GrammarParser.PowerExprContext):
        base = self.visit(ctx.unaryExpr(0))
        for i in range(1, len(ctx.unaryExpr())):
            base **= self.visit(ctx.unaryExpr(i))
        return base

    def visitUnaryExpresion(self, ctx:Kafe_GrammarParser.UnaryExpresionContext):
        op, val = ctx.getChild(0).getText(), self.visit(ctx.unaryExpr())
        return -val if op=='-' else not val

    def visitPrimaryExpresion(self, ctx:Kafe_GrammarParser.PrimaryExpresionContext):
        return self.visitChildren(ctx)

    def visitIndexingExpr(self, ctx:Kafe_GrammarParser.IndexingExprContext):
        col, idx = self.visit(ctx.primaryExpr()), self.visit(ctx.expr())
        if not isinstance(idx, int):
            raise TypeError(f"Index must be int, got {type(idx).__name__}")
        return col[idx]

    def visitParenExpr(self, ctx:Kafe_GrammarParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitIdExpr(self, ctx:Kafe_GrammarParser.IdExprContext):
        name = ctx.ID().getText()
        if name not in self.variables:
            raise NameError(f"Variable '{name}' not defined")
        return self.variables[name][1]

    def visitFunctionDecl(self, ctx:Kafe_GrammarParser.FunctionDeclContext):
        # (implementado arriba)

        return self.visitChildren(ctx)

    def visitFunctionCall(self, ctx:Kafe_GrammarParser.FunctionCallContext):
        name = ctx.ID().getText()
        if name not in self.variables:
            raise NameError(f"Function '{name}' not defined")
        func = self.variables[name][1]
        for argListCtx in ctx.argList():
            args = [self.visit(a) for a in argListCtx.arg()]
            func = func(*args)
        return func

    def visitArgList(self, ctx:Kafe_GrammarParser.ArgListContext):
        return self.visitChildren(ctx)

    # Casts
    def visitIntLiteral(self, ctx:Kafe_GrammarParser.IntLiteralContext):
        return int(ctx.getText())
    def visitFloatLiteral(self, ctx:Kafe_GrammarParser.FloatLiteralContext):
        return float(ctx.getText())
    def visitStringLiteral(self, ctx:Kafe_GrammarParser.StringLiteralContext):
        return ctx.getText()[1:-1]
    def visitBoolLiteral(self, ctx:Kafe_GrammarParser.BoolLiteralContext):
        return False if ctx.getText()=="False" else True
    def visitListLiteral(self, ctx:Kafe_GrammarParser.ListLiteralContext):
        return [self.visit(e) for e in ctx.expr()]
    def visitStrCastExpr(self, ctx:Kafe_GrammarParser.StrCastExprContext):
        return str(self.visit(ctx.expr()))
    def visitBoolCastExpr(self, ctx:Kafe_GrammarParser.BoolCastExprContext):
        return bool(self.visit(ctx.expr()))
    def visitFloatCastExpr(self, ctx:Kafe_GrammarParser.FloatCastExprContext):
        return float(self.visit(ctx.expr()))
    def visitIntCastExpr(self, ctx:Kafe_GrammarParser.IntCastExprContext):
        return int(self.visit(ctx.expr()))

    # --- Función completa definida aquí para claridad ---
    def visitFunctionDecl(self, ctx:Kafe_GrammarParser.FunctionDeclContext):
        name       = ctx.ID().getText()
        full_groups= [pl.paramDecl() for pl in ctx.paramList()]
        body       = ctx.block()

        class KafeFunction:
            def __init__(self, visitor, remaining, collected=None):
                self.visitor    = visitor
                self.full_groups= full_groups
                self.remaining  = remaining
                self.body       = body
                self.collected  = collected or []

            def __call__(self, *args):
                grp = self.remaining[0]
                if len(args) != len(grp):
                    raise TypeError(f"{name} expects {len(grp)} args, got {len(args)}")
                new_col = self.collected + [args]
                # si es el último grupo, asigno todos los grupos
                if len(self.remaining) == 1:
                    old = dict(self.visitor.variables)
                    for decls, vals in zip(self.full_groups, new_col):
                        for decl, val in zip(decls, vals):
                            pid   = decl.ID().getText()
                            ptype = decl.typeDecl().getText()
                            self.visitor.asignar_variable(pid, val, ptype)
                    try:
                        self.visitor.visit(body)
                    except ReturnValue as rv:
                        result = rv.value
                    else:
                        result = None
                    self.visitor.variables = old
                    return result
                # queda currificación pendiente
                return KafeFunction(self.visitor, self.remaining[1:], new_col)

        func_obj = KafeFunction(self, full_groups)
        self.variables[name] = ("FUNC", func_obj)
