// Generated from /home/estiven/Proyecto Final compiladores grupo 2/antlr4_data/Antrax.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link AntraxParser}.
 */
public interface AntraxListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link AntraxParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(AntraxParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(AntraxParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(AntraxParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(AntraxParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#statControl}.
	 * @param ctx the parse tree
	 */
	void enterStatControl(AntraxParser.StatControlContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#statControl}.
	 * @param ctx the parse tree
	 */
	void exitStatControl(AntraxParser.StatControlContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#statFunc}.
	 * @param ctx the parse tree
	 */
	void enterStatFunc(AntraxParser.StatFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#statFunc}.
	 * @param ctx the parse tree
	 */
	void exitStatFunc(AntraxParser.StatFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#statCycle}.
	 * @param ctx the parse tree
	 */
	void enterStatCycle(AntraxParser.StatCycleContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#statCycle}.
	 * @param ctx the parse tree
	 */
	void exitStatCycle(AntraxParser.StatCycleContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#statBasic}.
	 * @param ctx the parse tree
	 */
	void enterStatBasic(AntraxParser.StatBasicContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#statBasic}.
	 * @param ctx the parse tree
	 */
	void exitStatBasic(AntraxParser.StatBasicContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#ifStat}.
	 * @param ctx the parse tree
	 */
	void enterIfStat(AntraxParser.IfStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#ifStat}.
	 * @param ctx the parse tree
	 */
	void exitIfStat(AntraxParser.IfStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#tryStat}.
	 * @param ctx the parse tree
	 */
	void enterTryStat(AntraxParser.TryStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#tryStat}.
	 * @param ctx the parse tree
	 */
	void exitTryStat(AntraxParser.TryStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#tryAction}.
	 * @param ctx the parse tree
	 */
	void enterTryAction(AntraxParser.TryActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#tryAction}.
	 * @param ctx the parse tree
	 */
	void exitTryAction(AntraxParser.TryActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#catchAction}.
	 * @param ctx the parse tree
	 */
	void enterCatchAction(AntraxParser.CatchActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#catchAction}.
	 * @param ctx the parse tree
	 */
	void exitCatchAction(AntraxParser.CatchActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#ifAction}.
	 * @param ctx the parse tree
	 */
	void enterIfAction(AntraxParser.IfActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#ifAction}.
	 * @param ctx the parse tree
	 */
	void exitIfAction(AntraxParser.IfActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#elseAction}.
	 * @param ctx the parse tree
	 */
	void enterElseAction(AntraxParser.ElseActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#elseAction}.
	 * @param ctx the parse tree
	 */
	void exitElseAction(AntraxParser.ElseActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#whileStat}.
	 * @param ctx the parse tree
	 */
	void enterWhileStat(AntraxParser.WhileStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#whileStat}.
	 * @param ctx the parse tree
	 */
	void exitWhileStat(AntraxParser.WhileStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#forStat}.
	 * @param ctx the parse tree
	 */
	void enterForStat(AntraxParser.ForStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#forStat}.
	 * @param ctx the parse tree
	 */
	void exitForStat(AntraxParser.ForStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#printStat}.
	 * @param ctx the parse tree
	 */
	void enterPrintStat(AntraxParser.PrintStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#printStat}.
	 * @param ctx the parse tree
	 */
	void exitPrintStat(AntraxParser.PrintStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(AntraxParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(AntraxParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#varAsg}.
	 * @param ctx the parse tree
	 */
	void enterVarAsg(AntraxParser.VarAsgContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#varAsg}.
	 * @param ctx the parse tree
	 */
	void exitVarAsg(AntraxParser.VarAsgContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#funcStat}.
	 * @param ctx the parse tree
	 */
	void enterFuncStat(AntraxParser.FuncStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#funcStat}.
	 * @param ctx the parse tree
	 */
	void exitFuncStat(AntraxParser.FuncStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#params}.
	 * @param ctx the parse tree
	 */
	void enterParams(AntraxParser.ParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#params}.
	 * @param ctx the parse tree
	 */
	void exitParams(AntraxParser.ParamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(AntraxParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(AntraxParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#retStat}.
	 * @param ctx the parse tree
	 */
	void enterRetStat(AntraxParser.RetStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#retStat}.
	 * @param ctx the parse tree
	 */
	void exitRetStat(AntraxParser.RetStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#funcCall}.
	 * @param ctx the parse tree
	 */
	void enterFuncCall(AntraxParser.FuncCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#funcCall}.
	 * @param ctx the parse tree
	 */
	void exitFuncCall(AntraxParser.FuncCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(AntraxParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(AntraxParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#exprBool}.
	 * @param ctx the parse tree
	 */
	void enterExprBool(AntraxParser.ExprBoolContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#exprBool}.
	 * @param ctx the parse tree
	 */
	void exitExprBool(AntraxParser.ExprBoolContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#exprAdd}.
	 * @param ctx the parse tree
	 */
	void enterExprAdd(AntraxParser.ExprAddContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#exprAdd}.
	 * @param ctx the parse tree
	 */
	void exitExprAdd(AntraxParser.ExprAddContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#exprMul}.
	 * @param ctx the parse tree
	 */
	void enterExprMul(AntraxParser.ExprMulContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#exprMul}.
	 * @param ctx the parse tree
	 */
	void exitExprMul(AntraxParser.ExprMulContext ctx);
	/**
	 * Enter a parse tree produced by {@link AntraxParser#exprAtom}.
	 * @param ctx the parse tree
	 */
	void enterExprAtom(AntraxParser.ExprAtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link AntraxParser#exprAtom}.
	 * @param ctx the parse tree
	 */
	void exitExprAtom(AntraxParser.ExprAtomContext ctx);
}