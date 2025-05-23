# Generated from antlr4_data/Antrax.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AntraxParser import AntraxParser
else:
    from AntraxParser import AntraxParser

# This class defines a complete listener for a parse tree produced by AntraxParser.
class AntraxListener(ParseTreeListener):

    # Enter a parse tree produced by AntraxParser#root.
    def enterRoot(self, ctx:AntraxParser.RootContext):
        pass

    # Exit a parse tree produced by AntraxParser#root.
    def exitRoot(self, ctx:AntraxParser.RootContext):
        pass


    # Enter a parse tree produced by AntraxParser#stat.
    def enterStat(self, ctx:AntraxParser.StatContext):
        pass

    # Exit a parse tree produced by AntraxParser#stat.
    def exitStat(self, ctx:AntraxParser.StatContext):
        pass


    # Enter a parse tree produced by AntraxParser#ifStat.
    def enterIfStat(self, ctx:AntraxParser.IfStatContext):
        pass

    # Exit a parse tree produced by AntraxParser#ifStat.
    def exitIfStat(self, ctx:AntraxParser.IfStatContext):
        pass


    # Enter a parse tree produced by AntraxParser#tryStat.
    def enterTryStat(self, ctx:AntraxParser.TryStatContext):
        pass

    # Exit a parse tree produced by AntraxParser#tryStat.
    def exitTryStat(self, ctx:AntraxParser.TryStatContext):
        pass


    # Enter a parse tree produced by AntraxParser#tryAction.
    def enterTryAction(self, ctx:AntraxParser.TryActionContext):
        pass

    # Exit a parse tree produced by AntraxParser#tryAction.
    def exitTryAction(self, ctx:AntraxParser.TryActionContext):
        pass


    # Enter a parse tree produced by AntraxParser#catchAction.
    def enterCatchAction(self, ctx:AntraxParser.CatchActionContext):
        pass

    # Exit a parse tree produced by AntraxParser#catchAction.
    def exitCatchAction(self, ctx:AntraxParser.CatchActionContext):
        pass


    # Enter a parse tree produced by AntraxParser#ifAction.
    def enterIfAction(self, ctx:AntraxParser.IfActionContext):
        pass

    # Exit a parse tree produced by AntraxParser#ifAction.
    def exitIfAction(self, ctx:AntraxParser.IfActionContext):
        pass


    # Enter a parse tree produced by AntraxParser#elseAction.
    def enterElseAction(self, ctx:AntraxParser.ElseActionContext):
        pass

    # Exit a parse tree produced by AntraxParser#elseAction.
    def exitElseAction(self, ctx:AntraxParser.ElseActionContext):
        pass


    # Enter a parse tree produced by AntraxParser#whileStat.
    def enterWhileStat(self, ctx:AntraxParser.WhileStatContext):
        pass

    # Exit a parse tree produced by AntraxParser#whileStat.
    def exitWhileStat(self, ctx:AntraxParser.WhileStatContext):
        pass


    # Enter a parse tree produced by AntraxParser#forStat.
    def enterForStat(self, ctx:AntraxParser.ForStatContext):
        pass

    # Exit a parse tree produced by AntraxParser#forStat.
    def exitForStat(self, ctx:AntraxParser.ForStatContext):
        pass


    # Enter a parse tree produced by AntraxParser#printStat.
    def enterPrintStat(self, ctx:AntraxParser.PrintStatContext):
        pass

    # Exit a parse tree produced by AntraxParser#printStat.
    def exitPrintStat(self, ctx:AntraxParser.PrintStatContext):
        pass


    # Enter a parse tree produced by AntraxParser#varDecl.
    def enterVarDecl(self, ctx:AntraxParser.VarDeclContext):
        pass

    # Exit a parse tree produced by AntraxParser#varDecl.
    def exitVarDecl(self, ctx:AntraxParser.VarDeclContext):
        pass


    # Enter a parse tree produced by AntraxParser#varAsg.
    def enterVarAsg(self, ctx:AntraxParser.VarAsgContext):
        pass

    # Exit a parse tree produced by AntraxParser#varAsg.
    def exitVarAsg(self, ctx:AntraxParser.VarAsgContext):
        pass


    # Enter a parse tree produced by AntraxParser#funcStat.
    def enterFuncStat(self, ctx:AntraxParser.FuncStatContext):
        pass

    # Exit a parse tree produced by AntraxParser#funcStat.
    def exitFuncStat(self, ctx:AntraxParser.FuncStatContext):
        pass


    # Enter a parse tree produced by AntraxParser#params.
    def enterParams(self, ctx:AntraxParser.ParamsContext):
        pass

    # Exit a parse tree produced by AntraxParser#params.
    def exitParams(self, ctx:AntraxParser.ParamsContext):
        pass


    # Enter a parse tree produced by AntraxParser#param.
    def enterParam(self, ctx:AntraxParser.ParamContext):
        pass

    # Exit a parse tree produced by AntraxParser#param.
    def exitParam(self, ctx:AntraxParser.ParamContext):
        pass


    # Enter a parse tree produced by AntraxParser#retStat.
    def enterRetStat(self, ctx:AntraxParser.RetStatContext):
        pass

    # Exit a parse tree produced by AntraxParser#retStat.
    def exitRetStat(self, ctx:AntraxParser.RetStatContext):
        pass


    # Enter a parse tree produced by AntraxParser#funcCall.
    def enterFuncCall(self, ctx:AntraxParser.FuncCallContext):
        pass

    # Exit a parse tree produced by AntraxParser#funcCall.
    def exitFuncCall(self, ctx:AntraxParser.FuncCallContext):
        pass


    # Enter a parse tree produced by AntraxParser#expr.
    def enterExpr(self, ctx:AntraxParser.ExprContext):
        pass

    # Exit a parse tree produced by AntraxParser#expr.
    def exitExpr(self, ctx:AntraxParser.ExprContext):
        pass


    # Enter a parse tree produced by AntraxParser#exprBool.
    def enterExprBool(self, ctx:AntraxParser.ExprBoolContext):
        pass

    # Exit a parse tree produced by AntraxParser#exprBool.
    def exitExprBool(self, ctx:AntraxParser.ExprBoolContext):
        pass


    # Enter a parse tree produced by AntraxParser#exprAdd.
    def enterExprAdd(self, ctx:AntraxParser.ExprAddContext):
        pass

    # Exit a parse tree produced by AntraxParser#exprAdd.
    def exitExprAdd(self, ctx:AntraxParser.ExprAddContext):
        pass


    # Enter a parse tree produced by AntraxParser#exprMul.
    def enterExprMul(self, ctx:AntraxParser.ExprMulContext):
        pass

    # Exit a parse tree produced by AntraxParser#exprMul.
    def exitExprMul(self, ctx:AntraxParser.ExprMulContext):
        pass


    # Enter a parse tree produced by AntraxParser#exprAtom.
    def enterExprAtom(self, ctx:AntraxParser.ExprAtomContext):
        pass

    # Exit a parse tree produced by AntraxParser#exprAtom.
    def exitExprAtom(self, ctx:AntraxParser.ExprAtomContext):
        pass


