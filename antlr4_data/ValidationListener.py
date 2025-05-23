from antlr4 import *
from .AntraxParser import AntraxParser
from .AntraxListener import AntraxListener

class ValidationListener(AntraxListener):
    def __init__(self):
        self.declared_variables = set()
        self.declared_functions = set()

    def enterVarDecl(self, ctx: AntraxParser.VarDeclContext):
        var_name = ctx.ID().getText()
        if var_name in self.declared_variables:
            raise Exception(f"❌ Error: La variable '{var_name}' ya ha sido declarada.")
        self.declared_variables.add(var_name)

    def enterVarAsg(self, ctx: AntraxParser.VarAsgContext):
        var_name = ctx.ID().getText()
        if var_name not in self.declared_variables:
            raise Exception(f"❌ Error: La variable '{var_name}' no ha sido declarada antes de su uso.")

    def enterFuncStat(self, ctx: AntraxParser.FuncStatContext):
        func_name = ctx.FID().getText()
        if func_name in self.declared_functions:
            raise Exception(f"❌ Error: La función '{func_name}' ya ha sido declarada.")
        self.declared_functions.add(func_name)

    def enterFuncCall(self, ctx: AntraxParser.FuncCallContext):
        func_name = ctx.FID().getText()
        if func_name not in self.declared_functions:
            raise Exception(f"❌ Error: La función '{func_name}' no ha sido declarada antes de su uso.")

    def enterExpr(self, ctx: AntraxParser.ExprContext):
        # Aquí se implementa la lógica de validación de tipos
        if ctx.getChildCount() == 3:  # Operación binaria
            left_type = self.get_expr_type(ctx.getChild(0))
            right_type = self.get_expr_type(ctx.getChild(2))
            operator = ctx.getChild(1).getText()

            if operator in ['+', '-', '*', '/'] and left_type != right_type:
                raise Exception(f"❌ Error: Operación entre tipos incompatibles: {left_type} {operator} {right_type}")

    def get_expr_type(self, expr_node):
        # Si el nodo es un ID, extraemos el tipo de la variable
        if isinstance(expr_node, TerminalNode):  # Verifica si es un nodo terminal (token)
            token = expr_node.getSymbol()  # Obtenemos el símbolo del token
            token_text = token.text
            
            # Verificamos si es un identificador
            if expr_node.symbol.type == AntraxParser.ID:  # Verifica si el tipo es 'ID'
                if token_text in self.declared_variables:
                    return 'int'  # Aquí deberías obtener el tipo real de la variable si lo tienes en la tabla de símbolos
            # Verificamos si es un número
            elif expr_node.symbol.type == AntraxParser.NUM:  
                return 'int'
            # Verificamos si es una cadena
            elif expr_node.symbol.type == AntraxParser.STRING:
                return 'string'

        return 'unknown'
    
    