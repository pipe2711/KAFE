# EvalVisitorPrimitivo.py

import os
import pathlib
from antlr4 import FileStream, CommonTokenStream
from Kafe_GrammarLexer import Kafe_GrammarLexer
from Kafe_GrammarVisitor import Kafe_GrammarVisitor
from Kafe_GrammarParser import Kafe_GrammarParser
from utils import obtener_tipo_lista, verificarHomogeneidad


class ReturnValue(Exception):
    def __init__(self, value):
        super().__init__()
        self.value = value


class EvalVisitorPrimitivo(Kafe_GrammarVisitor):
    def __init__(self):
        self.variables    = {}
        self.type_mapping = {"INT": int, "FLOAT": float, "STR": str, "BOOL": bool}
        self.imported     = set()
        # Directorio actual de .kf para imports relativos
        self.current_dir  = None

    # Soporte para "import módulo;"
    def visitImportStmt(self, ctx):
        module = ctx.ID().getText()
        if module in self.imported:
            return
        self.imported.add(module)

        # Construir lista de rutas a probar
        candidates = []
        if self.current_dir:
            candidates.append(pathlib.Path(self.current_dir) / f"{module}.kf")
        base = pathlib.Path(__file__).parent
        candidates.append(base / f"{module}.kf")
        candidates.append(base.parent / f"{module}.kf")

        filename = None
        for path in candidates:
            if path.is_file():
                filename = path
                break
        if filename is None:
            tried = ", ".join(str(p) for p in candidates)
            raise FileNotFoundError(f"Module file for '{module}' not found. Tried: {tried}")

        # Ajustar directorio para imports dentro del módulo
        prev_dir = self.current_dir
        self.current_dir = filename.parent

        # Parsear y ejecutar el módulo
        input_stream = FileStream(str(filename), encoding='utf-8')
        lexer        = Kafe_GrammarLexer(input_stream)
        tokens       = CommonTokenStream(lexer)
        parser       = Kafe_GrammarParser(tokens)
        tree         = parser.program()
        self.visit(tree)

        # Restaurar directorio anterior
        self.current_dir = prev_dir
        return

    def _check_value_type(self, value, declared_type):
        if declared_type == "VOID":
            if value is not None:
                raise TypeError("Function declared VOID must not return a value")
            return
        if declared_type in self.type_mapping:
            if not isinstance(value, self.type_mapping[declared_type]):
                raise TypeError(f"Expected {declared_type}, obtained {type(value).__name__.upper()}")
            return
        if declared_type.startswith("List"):
            if not isinstance(value, list):
                raise TypeError(f"Expected {declared_type}, obtained {type(value).__name__}")
            if value:
                tipo_valor = obtener_tipo_lista(value)
                if tipo_valor != declared_type:
                    raise TypeError(f"Expected {declared_type}, obtained {tipo_valor}")
                if not verificarHomogeneidad(value):
                    raise TypeError("Expected homogeneous list")
            return
        if declared_type.startswith("FUNC"):
            if not callable(value):
                raise TypeError(f"Expected function, got {type(value).__name__}")
            return
        raise TypeError(f"Unknown type '{declared_type}'")

    def asignar_variable(self, name, valor, tipo):
        if tipo.startswith("FUNC"):
            if not callable(valor):
                raise TypeError(f"Expected function, got {type(valor).__name__}")
            self.variables[name] = (tipo, valor)
            return True
        if tipo in self.type_mapping:
            if type(valor) is not self.type_mapping[tipo]:
                raise TypeError(f"Expected {tipo}, obtained {type(valor).__name__.upper()}")
            self.variables[name] = (tipo, valor)
            return True
        if tipo.startswith("List") and any(t in tipo for t in ["INT","FLOAT","STR","BOOL"]):
            if not verificarHomogeneidad(valor):
                raise TypeError("Expected homogeneous list")
            tipo_valor = obtener_tipo_lista(valor)
            tipo_base  = tipo.replace("INT","").replace("FLOAT","")
            tipo_base  = tipo_base.replace("STR","").replace("BOOL","")
            if valor and tipo_valor not in (tipo, tipo_base):
                raise TypeError(f"Expected {tipo}, obtained {tipo_valor}")
            self.variables[name] = (tipo, valor)
            return True
        return False

    def visitVarDecl(self, ctx):
        tipo = ctx.typeDecl().getText()
        if tipo == "VOID":
            raise TypeError("VOID cannot be used as variable type")
        name = ctx.ID().getText()
        val  = self.visit(ctx.expr())
        if name in self.variables:
            raise NameError(f"Variable '{name}' already defined")
        if not self.asignar_variable(name, val, tipo):
            raise TypeError(f"Type '{tipo}' not recognized")

    def visitAssignStmt(self, ctx):
        name, val = ctx.ID().getText(), self.visit(ctx.expr())
        if name not in self.variables:
            raise NameError(f"Variable '{name}' not defined")
        tipo = self.variables[name][0]
        if not self.asignar_variable(name, val, tipo):
            raise TypeError(f"Cannot assign to '{name}' of type '{tipo}'")

    def visitFunctionDecl(self, ctx):
        name   = ctx.ID().getText()
        retTyp = ctx.typeDecl().getText()
        params = [p for pl in ctx.paramList() for p in pl.paramDecl()]
        for p in params:
            if (not isinstance(p, Kafe_GrammarParser.FunctionParamContext)
                    and p.typeDecl().getText() == "VOID"):
                raise TypeError(f"Parameter '{p.ID().getText()}' in '{name}' cannot be of type VOID")
        body  = ctx.block()
        outer = self
        class KafeFunction:
            def __init__(self, collected=None):
                self.collected = collected or []
                self.total     = len(params)
            def __call__(self, *args):
                if len(self.collected)+len(args) > self.total:
                    raise TypeError(f"{name} expects {self.total} args, got {len(self.collected)+len(args)}")
                new_vals = self.collected+list(args)
                if len(new_vals)<self.total:
                    return KafeFunction(new_vals)
                saved = dict(outer.variables)
                for decl,val in zip(params,new_vals):
                    pid   = decl.ID().getText()
                    ptype = ("FUNC" if isinstance(decl,Kafe_GrammarParser.FunctionParamContext)
                             else decl.typeDecl().getText())
                    outer.asignar_variable(pid,val,ptype)
                result=None
                try:
                    outer.visit(body)
                except ReturnValue as rv:
                    result=rv.value
                finally:
                    outer.variables=saved
                outer._check_value_type(result,retTyp)
                return result
        self.variables[name] = ("FUNC", KafeFunction())

    def visitLambdaExpr(self, ctx):
        param    = ctx.paramDecl()
        pid      = param.ID().getText()
        ptype    = param.typeDecl().getText()
        if ptype == "VOID":
            raise TypeError("Lambda parameter cannot be of type VOID")
        body     = ctx.expr()
        captured = dict(self.variables)
        outer    = self
        class LambdaFn:
            def __call__(self,val):
                local = dict(captured)
                saved = outer.variables
                outer.variables = local
                outer.asignar_variable(pid,val,ptype)
                try: res=outer.visit(body)
                finally: outer.variables=saved
                return res
        return LambdaFn()

    def visitLambdaExpresion(self, ctx):
        return self.visit(ctx.lambdaExpr())

    def visitFunctionCall(self, ctx):
        name = ctx.ID().getText()
        if name not in self.variables:
            raise NameError(f"Function '{name}' not defined")
        func = self.variables[name][1]
        ch, i = list(ctx.getChildren()), 0
        while i < len(ch):
            if ch[i].getText() == '(':
                if (i+1 < len(ch) and isinstance(ch[i+1], Kafe_GrammarParser.ArgListContext)):
                    args = [self.visit(a) for a in ch[i+1].arg()]
                    func = func(*args); i += 3
                else:
                    func = func();      i += 2
            else:
                i += 1
        if hasattr(func,"total") and len(func.collected) < func.total:
            raise TypeError(f"{name} expects {func.total} args, got {len(func.collected)}")
        return func

    def visitReturnStmt(self, ctx):        raise ReturnValue(self.visit(ctx.expr()))
    def visitShowStmt(self, ctx):          print(self.visit(ctx.expr()))
    def visitPourStmt(self, ctx):          return input(self.visit(ctx.expr()))
    def visitBlock(self, ctx):             return self.visitChildren(ctx)
    def visitIfElseExpr(self, ctx):        return self.visitChildren(ctx)
    def visitMatchExpr(self, ctx):         return self.visitChildren(ctx)
    def visitExpr(self, ctx):              return self.visitChildren(ctx)

    def visitLogicExpr(self, ctx):
        r = self.visit(ctx.equalityExpr(0))
        for i in range(1,len(ctx.equalityExpr())):
            op  = ctx.getChild(2*i-1).getText()
            rhs = self.visit(ctx.equalityExpr(i))
            r   = r and rhs if op=='&&' else r or rhs
        return r

    def visitEqualityExpr(self, ctx):
        r = self.visit(ctx.relationalExpr(0))
        for i in range(1,len(ctx.relationalExpr())):
            op  = ctx.getChild(2*i-1).getText()
            rhs = self.visit(ctx.relationalExpr(i))
            r   = r==rhs if op=='==' else r!=rhs
        return r

    def visitRelationalExpr(self, ctx):
        r = self.visit(ctx.additiveExpr(0))
        for i in range(1,len(ctx.additiveExpr())):
            op  = ctx.getChild(2*i-1).getText()
            rhs = self.visit(ctx.additiveExpr(i))
            if op=='<': r=r<rhs
            elif op=='<=': r=r<=rhs
            elif op=='>': r=r>rhs
            else: r=r>=rhs
        return r

    def visitAdditiveExpr(self, ctx):
        r = self.visit(ctx.multiplicativeExpr(0))
        for i in range(1,len(ctx.multiplicativeExpr())):
            op  = ctx.getChild(2*i-1).getText()
            rhs = self.visit(ctx.multiplicativeExpr(i))
            r   = r+rhs if op=='+' else r-rhs
        return r

    def visitMultiplicativeExpr(self, ctx):
        r = self.visit(ctx.powerExpr(0))
        for i in range(1,len(ctx.powerExpr())):
            op  = ctx.getChild(2*i-1).getText()
            rhs = self.visit(ctx.powerExpr(i))
            if op=='*': r*=rhs
            elif op=='/': r/=rhs
            else: r%=rhs
        return r

    def visitPowerExpr(self, ctx):
        base = self.visit(ctx.unaryExpr(0))
        for i in range(1,len(ctx.unaryExpr())):
            base **= self.visit(ctx.unaryExpr(i))
        return base

    def visitUnaryExpresion(self, ctx):
        op = ctx.getChild(0).getText()
        v  = self.visit(ctx.unaryExpr())
        return -v if op=='-' else not v

    def visitPrimaryExpresion(self, ctx): return self.visitChildren(ctx)

    def visitIndexingExpr(self, ctx):
        col = self.visit(ctx.primaryExpr()); idx = self.visit(ctx.expr())
        if not isinstance(idx,int): raise TypeError("Index must be int")
        return col[idx]

    def visitParenExpr(self, ctx): return self.visit(ctx.expr())

    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()
        if name not in self.variables: raise NameError(f"Variable '{name}' not defined")
        return self.variables[name][1]

    def visitIntLiteral(self, ctx):    return int(ctx.getText())
    def visitFloatLiteral(self, ctx):  return float(ctx.getText())
    def visitStringLiteral(self, ctx):text = ctx.getText(); return text[1:-1]
    def visitBoolLiteral(self, ctx):  return ctx.getText()=="True"
    def visitListLiteral(self, ctx):  return [self.visit(e) for e in ctx.expr()]
    def visitStrCastExpr(self, ctx):  return str(self.visit(ctx.expr()))
    def visitBoolCastExpr(self, ctx): return bool(self.visit(ctx.expr()))
    def visitFloatCastExpr(self, ctx):return float(self.visit(ctx.expr()))
    def visitIntCastExpr(self, ctx):  return int(self.visit(ctx.expr()))