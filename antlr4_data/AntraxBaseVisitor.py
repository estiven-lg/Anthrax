# Generated from Antrax.g4 by ANTLR 4.7.2
import re
from antlr4 import *

type_map = {
    "int": int,
    "float": float,
    "boolean": bool,
    "string": str,
    "void": type(None),
}


if __name__ is not None and "." in __name__:
    from .AntraxParser import AntraxParser
else:
    from AntraxParser import AntraxParser


class AntraxBaseVisitor(ParseTreeVisitor):
    __data = None
    __funtions = None
    __returnValue = None

    def __init__(self):
        self.__data = [{}]
        self.__funtions = {}

    def __enter_scope(self):
        """Ingresa a un nuevo ámbito (nuevo diccionario en la pila)."""
        self.__data.append({})

    def __exit_scope(self):
        """Sale del ámbito actual (elimina el último diccionario de la pila)."""
        self.__data.pop()

    def __data_add(self, id, type_var, value):
        """Declara una nueva variable en el ámbito actual."""

        var_type = type_map.get(type_var, None)
        if not isinstance(value, var_type):
            raise Exception(f"Error de tipo en la asignación de la variable {id}")

        if id in self.__data[-1]:
            raise Exception(f"Variable {id} ya declarada en este ámbito")
        self.__data[-1][id] = {"type": type_var, "value": value}

    def __data_set(self, id, type_var, value):
        """Asigna un valor a una variable en cualquier ámbito visible."""

        var_type = type_map.get(type_var, None)
        if not isinstance(value, var_type):
            raise Exception(f"Error de tipo en la asignación de la variable {id}")

        for scope in reversed(self.__data):  # Buscar en todos los ámbitos
            if id in scope:
                scope[id]["value"] = value
                return
        raise Exception(f"Variable {id} no declarada")

    def __data_get(self, id):
        """Obtiene el valor de una variable en cualquier ámbito visible."""
        for scope in reversed(self.__data):
            if id in scope:
                return scope[id]
        raise Exception(f"Variable {id} no declarada")

    def visitRoot(self, ctx: AntraxParser.RootContext):
        """
        Visita el nodo raíz
        """
        # print("visitRoot")
        return self.visitChildren(ctx)

    def visitStat(self, ctx: AntraxParser.StatContext):
        """
        Visita el nodo stat
        """
        # print("visitStat")
        if ctx.retStat():
            self.returnValue = self.visitRetStat(ctx.retStat())
        return self.visitChildren(ctx)

    def visitVarDecl(self, ctx: AntraxParser.VarDeclContext):
        """
        Visita el nodo varDecl, se ejecuta cuando se declara una variable.guarda el valor de la variable en el diccionario data.
        """
        # print("visitVarDecl")
        id = ctx.ID().getText()
        type_var = ctx.TYPE().getText()
        value = None

        if type_var == "int":
            value = int(self.visitExpr(ctx.expr()))
        elif type_var == "float":
            value = float(self.visitExpr(ctx.expr()))
        elif type_var == "boolean":
            value = bool(self.visitExpr(ctx.expr()))
        elif type_var == "string":
            value = str(self.visitExpr(ctx.expr()))
        else:
            value = self.visitExpr(ctx.expr())

        self.__data_add(id, type_var, value)

    def visitVarAsg(self, ctx: AntraxParser.VarAsgContext):
        """
        Visita el nodo varAsg, se ejecuta cuando se re-asigna un valor a una variable.
        """
        # print("visitVarAsg")
        var_data = self.__data_get(ctx.ID().getText())
        value = self.visitExpr(ctx.expr())

        self.__data_set(ctx.ID().getText(), var_data.get("type"), value)


    def visitIfStat(self, ctx: AntraxParser.IfStatContext):
        """
        Visita el nodo ifStat, se ejecuta cuando se encuentra una estructura if.
        y si hay un
        # print("visitIfStat")a estructura else se ejecuta.
        """
        self.__enter_scope()
        if self.visitExpr(ctx.expr()):
            self.visitIfAction(ctx.ifAction())
        elif ctx.getChildCount() > 7:
            self.visitElseAction(ctx.elseAction())
        self.__exit_scope()

    def visitIfAction(self, ctx: AntraxParser.IfActionContext):
        """
        Visita el nodo ifAction, se ejecuta cuando se cumple la condición  if de una condición.
        """
        # print("visitIfAction")
        for stat in ctx.stat():
            self.visitStat(stat)

    def visitElseAction(self, ctx: AntraxParser.ElseActionContext):
        """
        Visita el nodo elseAction, se ejecuta cuando se cumple la condición else de una condición.
        """
        # print("visitElseAction")
        for stat in ctx.stat():
            self.visitStat(stat)

    def visitTryStat(self, ctx: AntraxParser.TryStatContext):
        """
        Visita el nodo tryStat, se ejecuta cuando se encuentra una estructura try.
        """
        # print("visitTryStat")

        self.__enter_scope()
        try:
            self.visitTryAction(ctx.tryAction())
        except Exception as e:
            id = ctx.ID().getText()
            self.__data_add(id, "string", str(e))
            self.visitCatchAction(ctx.catchAction())
        
        self.__exit_scope()

    def visitTryAction(self, ctx: AntraxParser.TryActionContext):
        """
        Visita el nodo tryAction, se ejecuta cuando se no se encuentra una excepción.
        """
        # print("visitTryAction")
        for stat in ctx.stat():
            self.visitStat(stat)

    def visitCatchAction(self, ctx: AntraxParser.CatchActionContext):
        """
        Visita el nodo catchAction, se ejecuta cuando se encuentra una excepción.
        """
        # print("visitCatchAction")
        for stat in ctx.stat():
            self.visitStat(stat)

    def visitWhileStat(self, ctx: AntraxParser.WhileStatContext):
        """
        Visita el nodo whileStat, se ejecuta cuando se encuentra una estructura while.
        """
        # print("visitWhileStat")
        self.__enter_scope()
        while self.visitExpr(ctx.expr()):
            for stat in ctx.stat():
                self.visitStat(stat)
        self.__exit_scope()

    def visitForStat(self, ctx: AntraxParser.ForStatContext):
        """
        Visita el nodo forStat, se ejecuta cuando se encuentra una estructura for.
        """
        print("visitForStat")
        print(ctx.varDecl())
        self.visitVarDecl(ctx.varDecl())


        while self.visitExpr(ctx.expr()):
            for stat in ctx.stat():
                self.visitStat(stat)
                self.visitVarAsg(ctx.varAsg())

    def visitPrintStat(self, ctx: AntraxParser.PrintStatContext):
        """
        Visita el nodo printStat, se ejecuta cuando se encuentra una estructura print.
        """
        # print("visitPrintStat")
        if ctx.STRING():
            print(ctx.STRING().getText())
        if ctx.expr():
            print(self.visitExpr(ctx.expr()))

    # Visit a parse tree produced by AntraxParser#funcStat.
    def visitFuncStat(self, ctx: AntraxParser.FuncStatContext):
        """
        visita el nodo funcStat, se ejecuta cuando se encuentra una función. guarda el valor de la función en el diccionario de funciones.
        """
        # print("visitFuncStat")
        id = ctx.FID().getText()
        params = ctx.params()
        body = ctx.stat()

        self.__funtions[id] = {"params": params, "body": body}
        # return self.visitChildren(ctx)



    def visitFuncCall(self, ctx: AntraxParser.FuncCallContext):
        """
        Visita el nodo funcCall, se ejecuta cuando se encuentra una llamada a una función.
        """
        # print("visitFuncCall")
        id = ctx.FID().getText()

        if id not in self.__funtions:
            raise Exception(f"Función {id} no declarada")

        # Obtener la información de la función
        params = [self.visitExpr(expr) for expr in ctx.expr()]
        func_data = self.__funtions[id]
        body = func_data["body"]
        func_params = func_data["params"]

        self.__enter_scope()
        # Obtener los valores de los argumentos pasados
        for param, value in zip(func_params.param(), params):
            self.__data_add(param.ID().getText(), param.TYPE().getText(), value)

        self.returnValue = None

        # Ejecutar el cuerpo de la función
        for stat in body:
            self.visitStat(stat)
            if self.returnValue is not None:
                break

        self.__exit_scope

        return self.returnValue

    # Visit a parse tree produced by AntraxParser#retStat.
    def visitRetStat(self, ctx: AntraxParser.RetStatContext):
        """
        Visita el nodo retStat, se ejecuta cuando se encuentra una instrucción de retorno.
        """
        # print("visitRetStat")
        return self.visitExpr(ctx.expr())

    def visitExpr(self, ctx: AntraxParser.ExprContext):
        """
        Visita el nodo expr, se ejecuta cuando se encuentra una expresión.
        """
        # print("visitExpr")

        if ctx.funcCall():
            return self.visitFuncCall(ctx.funcCall())
        if ctx.STRING():
            return str(ctx.STRING().getText())
        if ctx.ID():
            return self.__data_get(ctx.ID().getText()).get("value")
        if ctx.NUM():
            return int(ctx.NUM().getText())
        if ctx.PLUS():
            return self.visitExpr(ctx.expr(0)) + self.visitExpr(ctx.expr(1))
        if ctx.getChildCount() == 3:

            # las expresiones están entre paréntesis
            if ctx.getChild(0).getText() == "(":
                return self.visitExpr(ctx.expr(0))

            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            sing = ctx.getChild(1).getText()

            # las operaciones estan a nivel atomico
            if sing == "+":
                return left + right
            if sing == "-":
                return left - right
            if sing == "*":
                return left * right
            if sing == "/":
                return left / right
            if sing == "<":
                return left < right
            if sing == ">":
                return left > right
            if sing == "<=":
                return left <= right
            if sing == ">=":
                return left >= right
            if sing == "==":
                return left == right
            if sing == "!=":
                return left != right
        return 0
