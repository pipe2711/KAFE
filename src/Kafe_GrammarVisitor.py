# Generated from Kafe_Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Kafe_GrammarParser import Kafe_GrammarParser
else:
    from Kafe_GrammarParser import Kafe_GrammarParser

# This class defines a complete generic visitor for a parse tree produced by Kafe_GrammarParser.

class Kafe_GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Kafe_GrammarParser#program.
    def visitProgram(self, ctx:Kafe_GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#importStmt.
    def visitImportStmt(self, ctx:Kafe_GrammarParser.ImportStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#stmt.
    def visitStmt(self, ctx:Kafe_GrammarParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#varDecl.
    def visitVarDecl(self, ctx:Kafe_GrammarParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#assignStmt.
    def visitAssignStmt(self, ctx:Kafe_GrammarParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#functionDecl.
    def visitFunctionDecl(self, ctx:Kafe_GrammarParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#paramList.
    def visitParamList(self, ctx:Kafe_GrammarParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#simpleParam.
    def visitSimpleParam(self, ctx:Kafe_GrammarParser.SimpleParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#functionParam.
    def visitFunctionParam(self, ctx:Kafe_GrammarParser.FunctionParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#returnStmt.
    def visitReturnStmt(self, ctx:Kafe_GrammarParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#showStmt.
    def visitShowStmt(self, ctx:Kafe_GrammarParser.ShowStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#pourStmt.
    def visitPourStmt(self, ctx:Kafe_GrammarParser.PourStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#ifElseExpr.
    def visitIfElseExpr(self, ctx:Kafe_GrammarParser.IfElseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#whileLoop.
    def visitWhileLoop(self, ctx:Kafe_GrammarParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#forLoop.
    def visitForLoop(self, ctx:Kafe_GrammarParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#matchExpr.
    def visitMatchExpr(self, ctx:Kafe_GrammarParser.MatchExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#matchCase.
    def visitMatchCase(self, ctx:Kafe_GrammarParser.MatchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#literalPattern.
    def visitLiteralPattern(self, ctx:Kafe_GrammarParser.LiteralPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#wildcardPattern.
    def visitWildcardPattern(self, ctx:Kafe_GrammarParser.WildcardPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#idPattern.
    def visitIdPattern(self, ctx:Kafe_GrammarParser.IdPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#block.
    def visitBlock(self, ctx:Kafe_GrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#expr.
    def visitExpr(self, ctx:Kafe_GrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#logicExpr.
    def visitLogicExpr(self, ctx:Kafe_GrammarParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#equalityExpr.
    def visitEqualityExpr(self, ctx:Kafe_GrammarParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#relationalExpr.
    def visitRelationalExpr(self, ctx:Kafe_GrammarParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:Kafe_GrammarParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:Kafe_GrammarParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#powerExpr.
    def visitPowerExpr(self, ctx:Kafe_GrammarParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#unaryExpresion.
    def visitUnaryExpresion(self, ctx:Kafe_GrammarParser.UnaryExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#primaryExpresion.
    def visitPrimaryExpresion(self, ctx:Kafe_GrammarParser.PrimaryExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#boolCastExpr.
    def visitBoolCastExpr(self, ctx:Kafe_GrammarParser.BoolCastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#floatCastExpr.
    def visitFloatCastExpr(self, ctx:Kafe_GrammarParser.FloatCastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#pourExpr.
    def visitPourExpr(self, ctx:Kafe_GrammarParser.PourExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#literalExpr.
    def visitLiteralExpr(self, ctx:Kafe_GrammarParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#functionCallExpr.
    def visitFunctionCallExpr(self, ctx:Kafe_GrammarParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#intCastExpr.
    def visitIntCastExpr(self, ctx:Kafe_GrammarParser.IntCastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#lambdaExpresion.
    def visitLambdaExpresion(self, ctx:Kafe_GrammarParser.LambdaExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#indexingExpr.
    def visitIndexingExpr(self, ctx:Kafe_GrammarParser.IndexingExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#strCastExpr.
    def visitStrCastExpr(self, ctx:Kafe_GrammarParser.StrCastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#parenExpr.
    def visitParenExpr(self, ctx:Kafe_GrammarParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#idExpr.
    def visitIdExpr(self, ctx:Kafe_GrammarParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#functionCall.
    def visitFunctionCall(self, ctx:Kafe_GrammarParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#argList.
    def visitArgList(self, ctx:Kafe_GrammarParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#exprArgument.
    def visitExprArgument(self, ctx:Kafe_GrammarParser.ExprArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#lambdaArgument.
    def visitLambdaArgument(self, ctx:Kafe_GrammarParser.LambdaArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#lambdaExpr.
    def visitLambdaExpr(self, ctx:Kafe_GrammarParser.LambdaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#intLiteral.
    def visitIntLiteral(self, ctx:Kafe_GrammarParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#floatLiteral.
    def visitFloatLiteral(self, ctx:Kafe_GrammarParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#stringLiteral.
    def visitStringLiteral(self, ctx:Kafe_GrammarParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#boolLiteral.
    def visitBoolLiteral(self, ctx:Kafe_GrammarParser.BoolLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#listLiteralExpr.
    def visitListLiteralExpr(self, ctx:Kafe_GrammarParser.ListLiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#listLiteral.
    def visitListLiteral(self, ctx:Kafe_GrammarParser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#typeDecl.
    def visitTypeDecl(self, ctx:Kafe_GrammarParser.TypeDeclContext):
        return self.visitChildren(ctx)



del Kafe_GrammarParser