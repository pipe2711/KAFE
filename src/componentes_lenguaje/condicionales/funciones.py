from ..errores import raiseConditionMustBeBoolean

from componentes_lenguaje.funciones.utils import ReturnValue, check_value_type

def ifElseExpr(self, ctx):
    cond_principal = self.visit(ctx.expr())
    if not isinstance(cond_principal, bool):
        raiseConditionMustBeBoolean("if", cond_principal)

    if cond_principal:
        try:
            self.visit(ctx.block(0))  
        except ReturnValue as rv:
            raise rv
        return 
    else:
        for elif_branch in ctx.elifBranch():
            cond_elif = self.visit(elif_branch.expr())
            if not isinstance(cond_elif, bool):
                raiseConditionMustBeBoolean("elif", cond_elif)
            if cond_elif:
                try:
                    self.visit(elif_branch.block())
                except ReturnValue as rv:
                    raise rv
                return 

    if ctx.ELSE() and len(ctx.block()) > 0:
        try:
            self.visit(ctx.block(len(ctx.block()) - 1))
        except ReturnValue as rv:
            raise rv
