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


    # Visit a parse tree produced by Kafe_GrammarParser#importNUMK.
    def visitImportNUMK(self, ctx:Kafe_GrammarParser.ImportNUMKContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#importPLOT.
    def visitImportPLOT(self, ctx:Kafe_GrammarParser.ImportPLOTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#importMATH.
    def visitImportMATH(self, ctx:Kafe_GrammarParser.ImportMATHContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#simpleImport.
    def visitSimpleImport(self, ctx:Kafe_GrammarParser.SimpleImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#stmt.
    def visitStmt(self, ctx:Kafe_GrammarParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#block.
    def visitBlock(self, ctx:Kafe_GrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#varDecl.
    def visitVarDecl(self, ctx:Kafe_GrammarParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#assignStmt.
    def visitAssignStmt(self, ctx:Kafe_GrammarParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#indexedAssignStmt.
    def visitIndexedAssignStmt(self, ctx:Kafe_GrammarParser.IndexedAssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#indexing.
    def visitIndexing(self, ctx:Kafe_GrammarParser.IndexingContext):
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


    # Visit a parse tree produced by Kafe_GrammarParser#elifBranch.
    def visitElifBranch(self, ctx:Kafe_GrammarParser.ElifBranchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#whileLoop.
    def visitWhileLoop(self, ctx:Kafe_GrammarParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#forLoop.
    def visitForLoop(self, ctx:Kafe_GrammarParser.ForLoopContext):
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


    # Visit a parse tree produced by Kafe_GrammarParser#filesLibraryExpr.
    def visitFilesLibraryExpr(self, ctx:Kafe_GrammarParser.FilesLibraryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#floatCastExpr.
    def visitFloatCastExpr(self, ctx:Kafe_GrammarParser.FloatCastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#mathLibraryExpr.
    def visitMathLibraryExpr(self, ctx:Kafe_GrammarParser.MathLibraryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#plotLibraryExpr.
    def visitPlotLibraryExpr(self, ctx:Kafe_GrammarParser.PlotLibraryExprContext):
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


    # Visit a parse tree produced by Kafe_GrammarParser#boolCastExpr.
    def visitBoolCastExpr(self, ctx:Kafe_GrammarParser.BoolCastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#numkLibraryExpr.
    def visitNumkLibraryExpr(self, ctx:Kafe_GrammarParser.NumkLibraryExprContext):
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


    # Visit a parse tree produced by Kafe_GrammarParser#idExpr.
    def visitIdExpr(self, ctx:Kafe_GrammarParser.IdExprContext):
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


    # Visit a parse tree produced by Kafe_GrammarParser#graph.
    def visitGraph(self, ctx:Kafe_GrammarParser.GraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#xlabel.
    def visitXlabel(self, ctx:Kafe_GrammarParser.XlabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#ylabel.
    def visitYlabel(self, ctx:Kafe_GrammarParser.YlabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#title.
    def visitTitle(self, ctx:Kafe_GrammarParser.TitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#grid.
    def visitGrid(self, ctx:Kafe_GrammarParser.GridContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#color.
    def visitColor(self, ctx:Kafe_GrammarParser.ColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#pointColor.
    def visitPointColor(self, ctx:Kafe_GrammarParser.PointColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#pointSize.
    def visitPointSize(self, ctx:Kafe_GrammarParser.PointSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#legend.
    def visitLegend(self, ctx:Kafe_GrammarParser.LegendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#bar.
    def visitBar(self, ctx:Kafe_GrammarParser.BarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#barValues.
    def visitBarValues(self, ctx:Kafe_GrammarParser.BarValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#pie.
    def visitPie(self, ctx:Kafe_GrammarParser.PieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#numkadd.
    def visitNumkadd(self, ctx:Kafe_GrammarParser.NumkaddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#numksub.
    def visitNumksub(self, ctx:Kafe_GrammarParser.NumksubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#numkmul.
    def visitNumkmul(self, ctx:Kafe_GrammarParser.NumkmulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#numkinv.
    def visitNumkinv(self, ctx:Kafe_GrammarParser.NumkinvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#numktranspose.
    def visitNumktranspose(self, ctx:Kafe_GrammarParser.NumktransposeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#open.
    def visitOpen(self, ctx:Kafe_GrammarParser.OpenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#sinFunction.
    def visitSinFunction(self, ctx:Kafe_GrammarParser.SinFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#cosFunction.
    def visitCosFunction(self, ctx:Kafe_GrammarParser.CosFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#tanFunction.
    def visitTanFunction(self, ctx:Kafe_GrammarParser.TanFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#asinFunction.
    def visitAsinFunction(self, ctx:Kafe_GrammarParser.AsinFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#acosFunction.
    def visitAcosFunction(self, ctx:Kafe_GrammarParser.AcosFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#atanFunction.
    def visitAtanFunction(self, ctx:Kafe_GrammarParser.AtanFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#sinhFunction.
    def visitSinhFunction(self, ctx:Kafe_GrammarParser.SinhFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#coshFunction.
    def visitCoshFunction(self, ctx:Kafe_GrammarParser.CoshFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#tanhFunction.
    def visitTanhFunction(self, ctx:Kafe_GrammarParser.TanhFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#expFunction.
    def visitExpFunction(self, ctx:Kafe_GrammarParser.ExpFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#expm1Function.
    def visitExpm1Function(self, ctx:Kafe_GrammarParser.Expm1FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#exp2Function.
    def visitExp2Function(self, ctx:Kafe_GrammarParser.Exp2FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#logFunction.
    def visitLogFunction(self, ctx:Kafe_GrammarParser.LogFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#log2Function.
    def visitLog2Function(self, ctx:Kafe_GrammarParser.Log2FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#log10Function.
    def visitLog10Function(self, ctx:Kafe_GrammarParser.Log10FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#cbrtFunction.
    def visitCbrtFunction(self, ctx:Kafe_GrammarParser.CbrtFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#sqrtFunction.
    def visitSqrtFunction(self, ctx:Kafe_GrammarParser.SqrtFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#powFunction.
    def visitPowFunction(self, ctx:Kafe_GrammarParser.PowFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#factorialFunction.
    def visitFactorialFunction(self, ctx:Kafe_GrammarParser.FactorialFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#combFunction.
    def visitCombFunction(self, ctx:Kafe_GrammarParser.CombFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#permFunction.
    def visitPermFunction(self, ctx:Kafe_GrammarParser.PermFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#gcdFunction.
    def visitGcdFunction(self, ctx:Kafe_GrammarParser.GcdFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#lcmFunction.
    def visitLcmFunction(self, ctx:Kafe_GrammarParser.LcmFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#absFunction.
    def visitAbsFunction(self, ctx:Kafe_GrammarParser.AbsFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#floorFunction.
    def visitFloorFunction(self, ctx:Kafe_GrammarParser.FloorFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#ceilFunction.
    def visitCeilFunction(self, ctx:Kafe_GrammarParser.CeilFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#roundFunction.
    def visitRoundFunction(self, ctx:Kafe_GrammarParser.RoundFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#truncFunction.
    def visitTruncFunction(self, ctx:Kafe_GrammarParser.TruncFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#fmodFunction.
    def visitFmodFunction(self, ctx:Kafe_GrammarParser.FmodFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#remainderFunction.
    def visitRemainderFunction(self, ctx:Kafe_GrammarParser.RemainderFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#copysignFunction.
    def visitCopysignFunction(self, ctx:Kafe_GrammarParser.CopysignFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#iscloseFunction.
    def visitIscloseFunction(self, ctx:Kafe_GrammarParser.IscloseFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#isfiniteFunction.
    def visitIsfiniteFunction(self, ctx:Kafe_GrammarParser.IsfiniteFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#isinfFunction.
    def visitIsinfFunction(self, ctx:Kafe_GrammarParser.IsinfFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#isnanFunction.
    def visitIsnanFunction(self, ctx:Kafe_GrammarParser.IsnanFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#ulpFunction.
    def visitUlpFunction(self, ctx:Kafe_GrammarParser.UlpFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#sumFunction.
    def visitSumFunction(self, ctx:Kafe_GrammarParser.SumFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#prodFunction.
    def visitProdFunction(self, ctx:Kafe_GrammarParser.ProdFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#sumRangeFunction.
    def visitSumRangeFunction(self, ctx:Kafe_GrammarParser.SumRangeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#prodRangeFunction.
    def visitProdRangeFunction(self, ctx:Kafe_GrammarParser.ProdRangeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#distFunction.
    def visitDistFunction(self, ctx:Kafe_GrammarParser.DistFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#fsumFunction.
    def visitFsumFunction(self, ctx:Kafe_GrammarParser.FsumFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#hypotFunction.
    def visitHypotFunction(self, ctx:Kafe_GrammarParser.HypotFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#sumprodFunction.
    def visitSumprodFunction(self, ctx:Kafe_GrammarParser.SumprodFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#erfFunction.
    def visitErfFunction(self, ctx:Kafe_GrammarParser.ErfFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#erfcFunction.
    def visitErfcFunction(self, ctx:Kafe_GrammarParser.ErfcFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#gammaFunction.
    def visitGammaFunction(self, ctx:Kafe_GrammarParser.GammaFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#lgammaFunction.
    def visitLgammaFunction(self, ctx:Kafe_GrammarParser.LgammaFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#degreesFunction.
    def visitDegreesFunction(self, ctx:Kafe_GrammarParser.DegreesFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#radiansFunction.
    def visitRadiansFunction(self, ctx:Kafe_GrammarParser.RadiansFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#piValue.
    def visitPiValue(self, ctx:Kafe_GrammarParser.PiValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#eValue.
    def visitEValue(self, ctx:Kafe_GrammarParser.EValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#tauConstant.
    def visitTauConstant(self, ctx:Kafe_GrammarParser.TauConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#infConstant.
    def visitInfConstant(self, ctx:Kafe_GrammarParser.InfConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Kafe_GrammarParser#nanConstant.
    def visitNanConstant(self, ctx:Kafe_GrammarParser.NanConstantContext):
        return self.visitChildren(ctx)



del Kafe_GrammarParser