from Kafe_GrammarVisitor import Kafe_GrammarVisitor
from Kafe_GrammarParser import Kafe_GrammarParser
from utils import obtener_tipo_lista, verificarHomogeneidad

class EvalVisitorPrimitivo(Kafe_GrammarVisitor):
    def __init__(self):
        self.intVariables = {}
        self.floatVariables = {}
        self.stringVariables = {}
        self.booleanoVariables = {}
        self.listaVariables = {}
        self.type_mapping = {
            "INT": (int, self.intVariables),
            "FLOAT": (float, self.floatVariables),
            "STR": (str, self.stringVariables),
            "BOOL": (bool, self.booleanoVariables)
        }

    def visitImportStmt(self, ctx:Kafe_GrammarParser.ImportStmtContext):
        return self.visitChildren(ctx)

    def visitVarDecl(self, ctx:Kafe_GrammarParser.VarDeclContext):
        tipo = ctx.typeDecl().getText()
        id_text = ctx.ID().getText()
        valor = self.visit(ctx.expr())

        if id_text in self.intVariables or id_text in self.floatVariables or id_text in self.stringVariables or id_text in self.booleanoVariables or id_text in self.listaVariables:
            raise NameError(f"Variable '{id_text}' already defined")

        if tipo == "VOID":
            raise TypeError("Cannot declare variable with type VOID")

        if tipo in self.type_mapping:
            expected_type, storage = self.type_mapping[tipo]
            if not isinstance(valor, expected_type):
                raise TypeError(f"Expected {tipo}, obtained {str.upper(type(valor).__name__)}")
            storage[id_text] = valor
            return

        if tipo.startswith("List") and any(t in tipo for t in ["INT", "FLOAT", "STR", "BOOL"]):
            tipo_valor = obtener_tipo_lista(valor)
            tipo_base = tipo.replace("INT", '').replace("FLOAT", '').replace("STR", '').replace("BOOL", '')

            if tipo != tipo_valor and tipo_base != tipo_valor and valor != []:
                raise TypeError(f"Expected {tipo}, obtained {tipo_valor}")
            self.listaVariables[id_text] = (tipo, valor)
            return

        raise TypeError(f"Type '{tipo}' not recognized")

    def visitAssignStmt(self, ctx:Kafe_GrammarParser.AssignStmtContext):
        id_text = ctx.ID().getText()
        valor = self.visit(ctx.expr())

        for tipo, (expected_type, storage) in self.type_mapping.items():
            if id_text in storage:
                if not isinstance(valor, expected_type):
                    raise TypeError(f"Expected {tipo}, obtained {str.upper(type(valor).__name__)}")
                storage[id_text] = valor
                return

        if id_text in self.listaVariables:
            tipo = self.listaVariables[id_text][0]
            tipo_valor = obtener_tipo_lista(valor)

            tipo_base = tipo.replace("INT", '').replace("FLOAT", '').replace("STR", '').replace("BOOL", '')
            if tipo != tipo_valor and tipo_base != tipo_valor and valor != []:
                raise TypeError(f"Expected {tipo}, obtained {tipo_valor}")
            self.listaVariables[id_text] = (tipo, valor)
            return

        raise NameError(f"Variable '{id_text}' not defined")


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
        return self.visitChildren(ctx)

    def visitPourStmt(self, ctx:Kafe_GrammarParser.PourStmtContext):
        return self.visitChildren(ctx)

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
        return self.visitChildren(ctx)

    def visitEqualityExpr(self, ctx:Kafe_GrammarParser.EqualityExprContext):
        return self.visitChildren(ctx)

    def visitRelationalExpr(self, ctx:Kafe_GrammarParser.RelationalExprContext):
        return self.visitChildren(ctx)

    def visitAdditiveExpr(self, ctx:Kafe_GrammarParser.AdditiveExprContext):
        return self.visitChildren(ctx)

    def visitMultiplicativeExpr(self, ctx:Kafe_GrammarParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)

    def visitPowerExpr(self, ctx:Kafe_GrammarParser.PowerExprContext):
        return self.visitChildren(ctx)

    def visitUnaryExpresion(self, ctx:Kafe_GrammarParser.UnaryExpresionContext):
        return self.visitChildren(ctx)

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

        for (_, storage) in self.type_mapping.values():
            if id_text in storage:
                return storage[id_text]

        if id_text in self.listaVariables:
            return self.listaVariables[id_text][1]

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

        if (verificarHomogeneidad(lista) == False):
            raise TypeError(f"Expected homogeneous list")

        return lista
