from antlr4 import ParseTreeVisitor
from llvmlite import ir


if __name__ is not None and "." in __name__:
    from .AntraxParser import AntraxParser
else:
    from AntraxParser import AntraxParser


class AntraxIRVisitor(ParseTreeVisitor):
    def __init__(self):
        self.__module = ir.Module(name="AntraxModule")
        self.__module.triple = "x86_64-pc-linux-gnu"
        self.__builder = None
        self.__scope = {}
        self.__functions = {}
        self.__variables = {}
        self.printf = None

        # funcion main
        func_type = ir.FunctionType(ir.IntType(32), [])
        main_func = ir.Function(self.__module, func_type, name="main")
        block = main_func.append_basic_block(name="entry")
   
        self.__add_scope("main", ir.IRBuilder(block))
        self.__change_scope("main")
        
        # Declarar printf
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.__module, printf_ty, name="printf")

        # Declarar formato para imprimir enteros
        formato = "%d\n\0"
        formato_const = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(formato)), bytearray(formato.encode("utf8"))
        )
        format_num = ir.GlobalVariable(self.__module, formato_const.type, name="fmt")
        format_num.linkage = "internal"
        format_num.global_constant = True
        format_num.initializer = formato_const
        self.formato_ptr = format_num

        # Declarar formato para imprimir enteros texto
        format_str = "%s\n\0"
        format_str_const = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(format_str)),
            bytearray(format_str.encode("utf8")),
        )
        format_str_var = ir.GlobalVariable(
            self.__module, format_str_const.type, name="fmt_str"
        )
        format_str_var.linkage = "internal"
        format_str_var.global_constant = True
        format_str_var.initializer = format_str_const
        self.formato_str_ptr = format_str_var



    # visitors

    def visitRoot(self, ctx: AntraxParser.RootContext):
        """
        Visita el nodo raíz del árbol de análisis
        """
        for statement in ctx.stat():
            self.visit(statement)
        self.__builder.ret(ir.Constant(ir.IntType(32), 0))
        return self.__module

    def visitStat(self, ctx: AntraxParser.StatContext):
        """
        Visita el nodo stat
        """
        return self.visitChildren(ctx)

    def visitVarDecl(self, ctx: AntraxParser.VarDeclContext):
        """
        Visita el nodo varDecl, se ejecuta cuando se encuentra una declaración de variable.
        """
        var_name = ctx.ID().getText()
        var_type = self.__getType (ctx.TYPE().getText())
        ptr = self.__builder.alloca(var_type, name=var_name)
        self.__variables[var_name] = ptr

        # Asignar valor inicial
        expr_value = self.visit(ctx.expr())
        self.__builder.store(expr_value, ptr)

        return ptr

    def visitVarAsg(self, ctx: AntraxParser.VarAsgContext):
        """
        Visita el nodo varAsg, se ejecuta cuando se encuentra una asignación de variable.
        """
        var_name = ctx.ID().getText()
        expr_value = self.visit(ctx.expr())
        self.__builder.store(expr_value, self.__variables[var_name])

    def visitIfStat(self, ctx: AntraxParser.IfStatContext):
        """
        visita el nodo ifStat, se ejecuta cuando se encuentra una estructura if.
        """

        # condición
        cond_value = self.visit(ctx.expr())

        # Crear bloques básicos
        then_block = self.__builder.append_basic_block(name="then")
        else_block = self.__builder.append_basic_block(name="else") if ctx.elseAction() else None
        merge_block = self.__builder.append_basic_block(name="ifcont") if not self.__has_return(ctx) else None

        # Salto condicional
        if else_block:
            self.__builder.cbranch(cond_value, then_block, else_block)
        else:
            self.__builder.cbranch(cond_value, then_block, merge_block if merge_block else None)

        # Bloque THEN
        self.__builder.position_at_start(then_block)
        self.visit(ctx.ifAction())
        # si hay un return en el bloque THEN, no saltar al bloque de merge
        if merge_block and not self.__block_ends_with_return(ctx.ifAction()):
            self.__builder.branch(merge_block)

        # Bloque ELSE (si existe)
        if else_block:
            self.__builder.position_at_start(else_block)
            self.visit(ctx.elseAction())
            # si hay un return en el bloque ELSE, no saltar al bloque de merge
            if merge_block and not self.__block_ends_with_return(ctx.elseAction()):
                self.__builder.branch(merge_block)

        # Solo posicionar en merge_block si es necesario
        if merge_block:
            self.__builder.position_at_start(merge_block)


    def visitIfAction(self, ctx: AntraxParser.IfActionContext):
        """
        Visita el nodo ifAction, se ejecuta cuando se encuentra una acción dentro de un if.
        """
        for stat in ctx.stat():
            self.visit(stat)

    def visitElseAction(self, ctx: AntraxParser.ElseActionContext):
        """
        Visita el nodo elseAction, se ejecuta cuando se encuentra una acción dentro de un else.
        """
        for stat in ctx.stat():
            self.visit(stat)

    def visitPrintStat(self, ctx: AntraxParser.PrintStatContext):
        """
        Visita el nodo printStat, se ejecuta cuando se encuentra una estructura print.
        """

        content = ctx.getChild(2).getText()

        # Verifica si es una cadena o una expresión
        if content.startswith('"') and content.endswith('"'):

            content = content[1:-1]
            str_name = f".str.{abs(hash(content)) % 1000}"

            str_const = ir.Constant(
                ir.ArrayType(ir.IntType(8), len(content) + 1),
                bytearray(content.encode("utf8") + b"\0"),
            )

            # Crear variable global para la cadena
            str_var = ir.GlobalVariable(self.__module, str_const.type, name=str_name)
            str_var.linkage = "internal"
            str_var.global_constant = True
            str_var.initializer = str_const

            # Obtener puntero al inicio de la cadena
            str_ptr = self.__builder.gep(
                str_var,
                [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0)],
                name="str_ptr",
            )

            # Obtener puntero al formato de string
            fmt_ptr = self.__builder.bitcast(
                self.formato_str_ptr, ir.IntType(8).as_pointer()
            )

            # Llamar a printf con el formato y el string
            self.__builder.call(self.printf, [fmt_ptr, str_ptr])
        elif ctx.expr():
            expr_value = self.visit(ctx.expr())

            formato_ptr = self.__builder.bitcast(
                self.formato_ptr, ir.IntType(8).as_pointer()
            )
            self.__builder.call(self.printf, [formato_ptr, expr_value])

    def visitWhileStat(self, ctx: AntraxParser.WhileStatContext):
        """
        Genera código IR para un ciclo while.
        """
        # Crear bloques básicos
        cond_block = self.__builder.append_basic_block(name="while.cond")
        body_block = self.__builder.append_basic_block(name="while.body")
        end_block = self.__builder.append_basic_block(name="while.end")

        # Saltar al bloque de condición
        self.__builder.branch(cond_block)
        # Bloque de condición
        self.__builder.position_at_start(cond_block)
        cond_value = self.visit(ctx.expr())  # Evaluar la condición
        self.__builder.cbranch(
            cond_value, body_block, end_block
        )  # Saltar según condición

        # Bloque del cuerpo
        self.__builder.position_at_start(body_block)
        for stat in ctx.stat():  # Visitar todas las declaraciones del cuerpo
            self.visit(stat)
        self.__builder.branch(cond_block)  # Volver a evaluar la condición

        # Bloque de salida
        self.__builder.position_at_start(end_block)

    def visitForStat(self, ctx: AntraxParser.ForStatContext):
        """
        visita el nodo forStat, se ejecuta cuando se encuentra una estructura for.
        """
        # 1. Bloque de inicialización
        self.visit(ctx.varDecl())  # Inicialización (ej: int $i = 0)

        # Crear bloques básicos
        cond_block = self.__builder.append_basic_block(name="for.cond")
        body_block = self.__builder.append_basic_block(name="for.body")
        inc_block = self.__builder.append_basic_block(name="for.inc")
        end_block = self.__builder.append_basic_block(name="for.end")

        # Saltar al bloque de condición
        self.__builder.branch(cond_block)

        # 2. Bloque de condición
        self.__builder.position_at_start(cond_block)
        cond_value = self.visit(ctx.expr())  # Evaluar condición
        self.__builder.cbranch(cond_value, body_block, end_block)

        # 3. Bloque del cuerpo
        self.__builder.position_at_start(body_block)
        for stat in ctx.stat():  # Ejecutar cuerpo del for
            self.visit(stat)
        self.__builder.branch(inc_block)  # Saltar a incremento

        # 4. Bloque de incremento
        self.__builder.position_at_start(inc_block)
        self.visit(ctx.varAsg())  # Ejecutar incremento (ej: $i = $i + 1)
        self.__builder.branch(cond_block)  # Volver a evaluar condición

        # 5. Bloque de salida
        self.__builder.position_at_start(end_block)

    def visitExpr(self, ctx:AntraxParser.ExprContext):
        return self.visitChildren(ctx)


    def visitExprBool(self, ctx:AntraxParser.ExprBoolContext):
        left = self.visit(ctx.exprAdd(0))
        for i in range(1, len(ctx.exprAdd())):
            right = self.visit(ctx.exprAdd(i))
            op = ctx.getChild(2 * i - 1).getText()

            if op == "<":
                left = self.__builder.icmp_signed("<", left, right, name="cmplttmp")
            elif op == ">":
                left = self.__builder.icmp_signed(">", left, right, name="cmpgttmp")
            elif op == "<=":
                left = self.__builder.icmp_signed("<=", left, right, name="cmpletmp")
            elif op == ">=":
                left = self.__builder.icmp_signed(">=", left, right, name="cmpgetmp")
            elif op == "==":
                left = self.__builder.icmp_signed("==", left, right, name="cmpeqtmp")
            elif op == "!=":
                left = self.__builder.icmp_signed("!=", left, right, name="cmpnetmp")

        return left


    # Visit a parse tree produced by AntraxParser#exprAdd.
    def visitExprAdd(self, ctx:AntraxParser.ExprAddContext):
        left = self.visit(ctx.exprMul(0))
        for i in range(1, len(ctx.exprMul())):
            right = self.visit(ctx.exprMul(i))
            op = ctx.getChild(2 * i - 1).getText()  # operadores están entre operandos

            if op == "+":
                left = self.__builder.add(left, right, name="addtmp")
            elif op == "-":
                left = self.__builder.sub(left, right, name="subtmp")

        return left


    # Visit a parse tree produced by AntraxParser#exprMul.
    def visitExprMul(self, ctx:AntraxParser.ExprMulContext):
        left = self.visit(ctx.exprAtom(0))
        for i in range(1, len(ctx.exprAtom())):
            right = self.visit(ctx.exprAtom(i))
            op = ctx.getChild(2 * i - 1).getText()

            if op == "*":
                left = self.__builder.mul(left, right, name="multmp")
            elif op == "/":
                left = self.__builder.sdiv(left, right, name="divtmp")

        return left


    # Visit a parse tree produced by AntraxParser#exprAtom.
    def visitExprAtom(self, ctx:AntraxParser.ExprAtomContext):
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            return self.visit(ctx.expr())
        if ctx.NUM():
            return ir.Constant(ir.IntType(32), int(ctx.NUM().getText()))
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.__variables:
                return self.__builder.load(self.__variables[var_name], name=var_name)
            else:
                raise ValueError(f"Variable '{var_name}' no está definida.")
        if ctx.funcCall():
            return self.visit(ctx.funcCall())
        if ctx.STRING():
            return self.__builder.constant_string(ctx.STRING().getText())

        return ir.Constant(ir.IntType(32), 0)  # Retorno por defecto en caso de error
        

    
    def visitFuncStat(self, ctx: AntraxParser.FuncStatContext):
        """
        Visita el nodo funcStat, se ejecuta cuando se encuentra una declaración de función.
        """
        func_name = ctx.FID().getText()[1:]  # Elimina el @ del nombre
        return_type = self.__getType (ctx.TYPE().getText())

        # Procesar parámetros
        param_types = []
        params_info = []
        if ctx.params():
            for param in ctx.params().param():
                param_type = self.__getType (param.TYPE().getText())
                param_types.append(param_type)
                params_info.append((param.ID().getText(), param_type))

        # Crear tipo de función
        func_type = ir.FunctionType(return_type, param_types)

        # Crear función en el módulo
        function = ir.Function(self.__module, func_type, name=func_name)

        # Guardar información para el cuerpo
        self.__functions[func_name] = {
            "function": function,
            "params_info": params_info,
            "body": ctx.stat(),
        }

        # Crear bloque de entrada
        entry_block = function.append_basic_block(name="entry")
        builder = ir.IRBuilder(entry_block)
        self.__add_scope(func_name, builder)
        self.__change_scope(func_name)

        # Almacenar parámetros en variables locales
        for i, (param_name, param_type) in enumerate(params_info):
            param_var = builder.alloca(param_type, name=param_name)
            builder.store(function.args[i], param_var)
            self.__variables[param_name] = param_var

        # Procesar cuerpo de la función
        for stat in ctx.stat():
            self.visit(stat)

        # # Si no hay return explícito, agregar uno para funciones void
        if return_type == ir.VoidType() and not ctx.stat()[-1].retStat():
            builder.ret_void()
        self.__change_scope("main")

    def visitFuncCall(self, ctx: AntraxParser.FuncCallContext):
        """
        Visita el nodo funcCall, se ejecuta cuando se encuentra una llamada a función.
        """
        func_name = ctx.FID().getText()[1:]  # Elimina el @ del nombre

        if func_name not in self.__functions:
            raise ValueError(f"Función {func_name} no definida")

        # Obtener información de la función
        func_info = self.__functions[func_name]
        function = func_info["function"]

        # Procesar argumentos
        args = []
        for expr in ctx.expr():
            arg_value = self.visit(expr)
            args.append(arg_value)

        # Crear llamada
        call_result = self.__builder.call(function, args)

        # Manejar el valor de retorno
        if function.ftype.return_type == ir.VoidType():
            return None
        return call_result

    def visitRetStat(self, ctx: AntraxParser.RetStatContext):
        """
        Visita el nodo retStat, se ejecuta cuando se encuentra una declaración de retorno.
        """
        if ctx.expr():
            ret_value = self.visit(ctx.expr())
            self.__builder.ret(ret_value)
        elif ctx.STRING():
            # Manejo de strings (similar a print)
            string_val = ctx.STRING().getText()[1:-1]
            str_ptr = self._create_global_string(string_val)
            self.__builder.ret(str_ptr)
        else:
            self.__builder.ret_void()
        return None  # El valor de retorno se maneja en la llamada
    
    # funciones auxiliares

    def __change_scope(self, name):
        """
        Cambia el contexto de la función actual
        """
        if name not in self.__scope:
            raise Exception(f"Scope '{name}' no existe.")
        self.__builder = self.__scope[name]

    def __add_scope(self, name, builder):
        """
        Agrega un nuevo contexto de función
        """
        if name in self.__scope:
            raise Exception(f"Scope '{name}' ya existe.")
        self.__scope[name] = builder

    def __getType (self, type_str):
        if type_str == "int":
            return ir.IntType(32)
        elif type_str == "float":
            return ir.FloatType()
        elif type_str == "boolean":
            return ir.IntType(1)
        elif type_str == "string":
            return ir.IntType(8).as_pointer()
        elif type_str == "void":
            return ir.VoidType()
        else:
            raise ValueError("Unsupported type: " + type_str)
        
    def __has_return(self, ctx):
        """Verifica si el bloque contiene un return"""
        if hasattr(ctx, 'stat'):
            for stat in ctx.stat():
                if stat.retStat():
                    return True
        return False

    def __block_ends_with_return(self, ctx):
        """Verifica si el último statement es un return"""
        if hasattr(ctx, 'stat') and ctx.stat():
            return ctx.stat()[-1].retStat() is not None
        return False

    
