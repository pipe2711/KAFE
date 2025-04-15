from Kafe_GrammarVisitor import Kafe_GrammarVisitor
from Kafe_GrammarParser import Kafe_GrammarParser

class EvalVisitorPrimitivo(Kafe_GrammarVisitor):
    def visitProgram(self, ctx:Kafe_GrammarParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitImportStmt(self, ctx:Kafe_GrammarParser.ImportStmtContext):
        return self.visitChildren(ctx)

    def visitStmt(self, ctx:Kafe_GrammarParser.StmtContext):
        return self.visitChildren(ctx)

    def visitVarDecl(self, ctx:Kafe_GrammarParser.VarDeclContext):
        return self.visitChildren(ctx)

    def visitAssignStmt(self, ctx:Kafe_GrammarParser.AssignStmtContext):
        return self.visitChildren(ctx)

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
        return self.visitChildren(ctx)

    def visitIdExpr(self, ctx:Kafe_GrammarParser.IdExprContext):
        return self.visitChildren(ctx)

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
        return self.visitChildren(ctx)

    def visitFloatLiteral(self, ctx:Kafe_GrammarParser.FloatLiteralContext):
        return self.visitChildren(ctx)

    def visitCharLiteral(self, ctx:Kafe_GrammarParser.CharLiteralContext):
        return self.visitChildren(ctx)

    def visitStringLiteral(self, ctx:Kafe_GrammarParser.StringLiteralContext):
        return self.visitChildren(ctx)

    def visitBoolLiteral(self, ctx:Kafe_GrammarParser.BoolLiteralContext):
        return self.visitChildren(ctx)

    def visitListLiteralExpr(self, ctx:Kafe_GrammarParser.ListLiteralExprContext):
        return self.visitChildren(ctx)

    def visitListLiteral(self, ctx:Kafe_GrammarParser.ListLiteralContext):
        return self.visitChildren(ctx)

    def visitTypeDecl(self, ctx:Kafe_GrammarParser.TypeDeclContext):
        return self.visitChildren(ctx)
