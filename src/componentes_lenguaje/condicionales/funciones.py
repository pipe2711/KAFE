def ifElseExpr(self, ctx):
    cond_principal = self.visit(ctx.expr())
    if not isinstance(cond_principal, bool):
        raise TypeError(f"Condition in 'if' must be boolean, got {type(cond_principal).__name__}")

    try:
        if cond_principal:
            self.visit(ctx.block(0))  # bloque del if
            return  # salimos si se cumple el if
        else:
            for elif_branch in ctx.elifBranch():
                cond_elif = self.visit(elif_branch.expr())
                if not isinstance(cond_elif, bool):
                    raise TypeError(f"Condition in 'elif' must be boolean, got {type(cond_elif).__name__}")
                if cond_elif:
                    self.visit(elif_branch.block())
                    return  # salimos si se cumple algún elif
        # Si no se cumple ningún if ni elif, revisas el ELSE (si existe)
        if ctx.ELSE() and len(ctx.block()) > 0:
            self.visit(ctx.block(len(ctx.block()) - 1))
    # el último bloque es el else
    except Exception as e:
        raise RuntimeError(f"Error in 'if-else' block: {str(e)}")

