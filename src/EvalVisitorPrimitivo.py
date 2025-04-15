from Kafe_GrammarVisitor import Kafe_GrammarVisitor
from Kafe_GrammarParser import Kafe_GrammarParser
from utils import obtener_tipo_lista, verificarHomogeneidad

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

            if (verificarHomogeneidad(valor) == False):
                raise TypeError(f"Expected homogeneous list")

            if tipo != tipo_valor and tipo_base != tipo_valor and valor != []:
                raise TypeError(f"Expected {tipo}, obtained {tipo_valor}")
            self.variables[id_text] = (tipo, valor)
        else:
            variable_asignada = False

        return variable_asignada

    def visitImportStmt(self, ctx:Kafe_GrammarParser.ImportStmtContext):
        return self.visitChildren(ctx)

    def visitVarDecl(self, ctx:Kafe_GrammarParser.VarDeclContext):
        tipo = ctx.typeDecl().getText()
        id_text = ctx.ID().getText()
        valor = self.visit(ctx.expr())

        if id_text in self.variables:
            raise NameError(f"Variable '{id_text}' already defined")

        if tipo == "VOID":
            raise TypeError("Cannot declare variable with type VOID")

        variable_asignada = self.asignar_variable(id_text, valor, tipo)

        if (not variable_asignada):
            raise TypeError(f"Type '{tipo}' not recognized")

    def visitAssignStmt(self, ctx:Kafe_GrammarParser.AssignStmtContext):
        id_text = ctx.ID().getText()
        valor = self.visit(ctx.expr())

        if id_text not in self.variables:
            raise NameError(f"Variable '{id_text}' not defined")

        tipo = self.variables[id_text][0]

        variable_asignada = self.asignar_variable(id_text, valor, tipo)

        if (not variable_asignada):
            raise TypeError(f"Cannot assign value to variable '{id_text}' of type '{tipo}'")

    def visitFunctionDecl(self, ctx:Kafe_GrammarParser.FunctionDeclContext):
        return self.visitChildren(ctx)

    def visitParamList(self, ctx:Kafe_GrammarParser.ParamListContext):
        return self.visitChildren(ctx)

    def visitSimpleParam(self, ctx:Kafe_GrammarParser.SimpleParamContext):
        return self.visitChildren(ctx)

    def visitFunctionParam(self, ctx:Kafe_GrammarParser.FunctionParamContext):
        return self.visitChildren(ctx)

    def visitReturnStmt(self, ctx:Kafe_GrammarParser.ReturnStmtContext):
        return self.visitChildren(ctx)

    def visitShowStmt(self, ctx:Kafe_GrammarParser.ShowStmtContext):
        print(self.visit(ctx.expr()))

    def visitPourStmt(self, ctx:Kafe_GrammarParser.PourStmtContext):
        return input(self.visit(ctx.expr()))

    def visitIfElseExpr(self, ctx:Kafe_GrammarParser.IfElseExprContext):
        return self.visitChildren(ctx)

    def visitWhileLoop(self, ctx:Kafe_GrammarParser.WhileLoopContext):
        return self.visitChildren(ctx)

    def visitForLoop(self, ctx:Kafe_GrammarParser.ForLoopContext):
        return self.visitChildren(ctx)

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

    def visitFunctionCallExpr(self, ctx:Kafe_GrammarParser.FunctionCallExprContext):
        return self.visitChildren(ctx)

    def visitLambdaExpresion(self, ctx:Kafe_GrammarParser.LambdaExpresionContext):
        return self.visitChildren(ctx)

    def visitIndexingExpr(self, ctx:Kafe_GrammarParser.IndexingExprContext):
        return self.visitChildren(ctx)

    def visitParenExpr(self, ctx:Kafe_GrammarParser.ParenExprContext):
        return self.visitChildren(ctx.expr())

    def visitIdExpr(self, ctx:Kafe_GrammarParser.IdExprContext):
        id_text = ctx.ID().getText()

        if id_text in self.variables:
            return self.variables[id_text][1]

        raise NameError(f"Variable '{id_text}' not defined")

    def visitFunctionCall(self, ctx:Kafe_GrammarParser.FunctionCallContext):
        return self.visitChildren(ctx)

    def visitArgList(self, ctx:Kafe_GrammarParser.ArgListContext):
        return self.visitChildren(ctx)

    def visitExprArgument(self, ctx:Kafe_GrammarParser.ExprArgumentContext):
        return self.visitChildren(ctx)

    def visitLambdaArgument(self, ctx:Kafe_GrammarParser.LambdaArgumentContext):
        return self.visitChildren(ctx)

    def visitLambdaExpr(self, ctx:Kafe_GrammarParser.LambdaExprContext):
        return self.visitChildren(ctx)

    def visitIntLiteral(self, ctx:Kafe_GrammarParser.IntLiteralContext):
        return int(ctx.getText())

    def visitFloatLiteral(self, ctx:Kafe_GrammarParser.FloatLiteralContext):
        return float(ctx.getText())

    def visitStringLiteral(self, ctx:Kafe_GrammarParser.StringLiteralContext):
        return ctx.getText()[1:-1]

    def visitBoolLiteral(self, ctx:Kafe_GrammarParser.BoolLiteralContext):
        if ctx.getText() == "False":
            return False
        else:
            return True

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
