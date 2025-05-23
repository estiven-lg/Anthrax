# Generated from antlr4_data/Antrax.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AntraxParser import AntraxParser
else:
    from AntraxParser import AntraxParser

# This class defines a complete generic visitor for a parse tree produced by AntraxParser.

class AntraxVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AntraxParser#root.
    def visitRoot(self, ctx:AntraxParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#stat.
    def visitStat(self, ctx:AntraxParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#ifStat.
    def visitIfStat(self, ctx:AntraxParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#tryStat.
    def visitTryStat(self, ctx:AntraxParser.TryStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#tryAction.
    def visitTryAction(self, ctx:AntraxParser.TryActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#catchAction.
    def visitCatchAction(self, ctx:AntraxParser.CatchActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#ifAction.
    def visitIfAction(self, ctx:AntraxParser.IfActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#elseAction.
    def visitElseAction(self, ctx:AntraxParser.ElseActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#whileStat.
    def visitWhileStat(self, ctx:AntraxParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#forStat.
    def visitForStat(self, ctx:AntraxParser.ForStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#printStat.
    def visitPrintStat(self, ctx:AntraxParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#varDecl.
    def visitVarDecl(self, ctx:AntraxParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#varAsg.
    def visitVarAsg(self, ctx:AntraxParser.VarAsgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#funcStat.
    def visitFuncStat(self, ctx:AntraxParser.FuncStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#params.
    def visitParams(self, ctx:AntraxParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#param.
    def visitParam(self, ctx:AntraxParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#retStat.
    def visitRetStat(self, ctx:AntraxParser.RetStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#funcCall.
    def visitFuncCall(self, ctx:AntraxParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#expr.
    def visitExpr(self, ctx:AntraxParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#exprBool.
    def visitExprBool(self, ctx:AntraxParser.ExprBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#exprAdd.
    def visitExprAdd(self, ctx:AntraxParser.ExprAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#exprMul.
    def visitExprMul(self, ctx:AntraxParser.ExprMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AntraxParser#exprAtom.
    def visitExprAtom(self, ctx:AntraxParser.ExprAtomContext):
        return self.visitChildren(ctx)



del AntraxParser