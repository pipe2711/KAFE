from errores import raiseConditionMustBeBoolean

def ifElseExpr(self, ctx):
    cond_principal = self.visit(ctx.expr())
    if not isinstance(cond_principal, bool):
        raiseConditionMustBeBoolean("if", cond_principal)

    if cond_principal:
        self.visit(ctx.block(0))  # bloque del if
        return  # salimos si se cumple el if
    else:
        for elif_branch in ctx.elifBranch():
            cond_elif = self.visit(elif_branch.expr())
            if not isinstance(cond_elif, bool):
                raiseConditionMustBeBoolean("elif", cond_elif)
            if cond_elif:
                self.visit(elif_branch.block())
                return  # salimos si se cumple algún elif
    # Si no se cumple ningún if ni elif, revisas el ELSE (si existe)
    if ctx.ELSE() and len(ctx.block()) > 0:
        self.visit(ctx.block(len(ctx.block()) - 1))
