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

    def visitParamDecl(self, ctx:Kafe_GrammarParser.ParamDeclContext):
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

    def visitPattern(self, ctx:Kafe_GrammarParser.PatternContext):
        return self.visitChildren(ctx)

    def visitBlock(self, ctx:Kafe_GrammarParser.BlockContext):
        return self.visitChildren(ctx)

    def visitExpr(self, ctx:Kafe_GrammarParser.ExprContext):
        return self.visitChildren(ctx)

    def visitFunctionCall(self, ctx:Kafe_GrammarParser.FunctionCallContext):
        return self.visitChildren(ctx)

    def visitArgList(self, ctx:Kafe_GrammarParser.ArgListContext):
        return self.visitChildren(ctx)

    def visitArg(self, ctx:Kafe_GrammarParser.ArgContext):
        return self.visitChildren(ctx)

    def visitLambdaExpr(self, ctx:Kafe_GrammarParser.LambdaExprContext):
        return self.visitChildren(ctx)

    def visitLiteral(self, ctx:Kafe_GrammarParser.LiteralContext):
        return self.visitChildren(ctx)

    def visitTypeDecl(self, ctx:Kafe_GrammarParser.TypeDeclContext):
        return self.visitChildren(ctx)
