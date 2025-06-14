from Kafe_GrammarParser import Kafe_GrammarParser

from TypeUtils import funcion_t, void_t, entero_t, todos_t, lista_cualquiera_t
from errores import (
    raiseFunctionAlreadyDefined,
    raiseVoidAsParameterType,
    raiseWrongNumberOfArgs,
    raiseFunctionNotDefined,
    raiseSignatureMismatch
)
from global_utils import asignar_variable, check_sig
from .utils import ReturnValue, check_value_type, _parse_signature

def _get_top_params(signature: str) -> list[str]:
    s = signature.replace(" ", "")
    if not s.startswith("FUNC("):
        return []
    inner = s[len("FUNC("):]
    idx = inner.find(")")
    params = inner[:idx]
    return params.split(",") if params else []

def functionDecl(self, ctx):
    name = ctx.ID().getText()
    if name in self.variables:
        tipo_existente, _ = self.variables[name]
        if tipo_existente == funcion_t:
            raiseFunctionAlreadyDefined(name)

    param_lists  = ctx.getTypedRuleContexts(Kafe_GrammarParser.ParamListContext)
    params_flat  = []
    param_groups = []
    for pl in param_lists:
        grp = []
        for p in pl.paramDecl():
            t = p.typeDecl().getText().replace(" ", "")
            grp.append(t)
            params_flat.append(p)
        param_groups.append(grp)

    for p in params_flat:
        if p.typeDecl().getText().replace(" ", "") == void_t:
            raiseVoidAsParameterType()
    ret_type = ctx.typeDecl().getText().replace(" ", "")
    body     = ctx.block()
    outer    = self
    total    = len(params_flat)

    if param_groups:
        prefix = "".join(f"FUNC({','.join(grp)})=>" for grp in param_groups)
        full_sig = prefix + ret_type
    else:
        full_sig = f"FUNC()=>{ret_type}"

    class KafeFunction:
        def __init__(self, collected=None):
            self.collected      = collected[:] if collected else []
            self._name          = name
            self._signature     = full_sig
            self._total         = total

        @property
        def signature(self):
            return self._signature

        def __str__(self):
            raise Exception(
                f"'{self._name}' expects {self._total} args, got {len(self.collected)}"
            )
        __repr__ = __str__

        def __call__(self, *args):
            ncol = len(self.collected) + len(args)
            if ncol > self._total:
                raiseWrongNumberOfArgs(self._name, self._total, ncol)

            new_vals = self.collected + list(args)
            if ncol < self._total:
                return KafeFunction(new_vals)

            saved = dict(outer.variables)
            try:
                for decl, val in zip(params_flat, new_vals):
                    expected = decl.typeDecl().getText().replace(" ", "")

                    sig_obt = getattr(val, "signature", None)
                    if sig_obt:
                        act_p, act_r = _parse_signature(sig_obt)
                        exp_p, exp_r = _parse_signature(expected)
                        if not (act_p == exp_p and act_r == exp_r):
                            top_act = _get_top_params(sig_obt)
                            top_exp = _get_top_params(expected)
                            if len(top_act) != len(top_exp):
                                pname = decl.ID().getText()
                                raise TypeError(
                                    f"Function parameter '{pname}' "
                                    f"must accept {len(top_exp)} parameter(s), "
                                    f"but got {len(top_act)}."
                                )

                    check_value_type(val, expected)

                    pid   = decl.ID().getText()
                    ptype = funcion_t if expected.startswith("FUNC") else expected
                    asignar_variable(outer, pid, val, ptype)

                result = None
                try:
                    outer.dentro_bloque = True
                    outer.visit(body)
                except ReturnValue as rv:
                    result = rv.value
            finally:
                outer.variables = saved

            if ret_type.startswith("FUNC"):
                exp_p, exp_r = _parse_signature(ret_type)
                if len(exp_p) > 1:
                    sig_ret = getattr(result, "signature", None)
                    if sig_ret is None:
                        raiseSignatureMismatch(ret_type, "")
                    act_p, act_r = _parse_signature(sig_ret)
                    if act_p != exp_p or act_r != exp_r:
                        raiseSignatureMismatch(ret_type, sig_ret)
                else:
                    pass
            else:
                check_value_type(result, ret_type)

            outer.dentro_bloque = False
            return result

    self.variables[name] = (funcion_t, KafeFunction())

def lambdaExpr(self, ctx):
    params = (ctx.paramList().paramDecl()
              if hasattr(ctx, "paramList") and ctx.paramList()
              else [ctx.paramDecl()])

    for p in params:
        if p.typeDecl().getText().replace(" ", "") == void_t:
            raiseVoidAsParameterType()

    in_types = [p.typeDecl().getText().replace(" ", "") for p in params]
    lam_sig  = f"FUNC({','.join(in_types)})=>ANY"
    total    = len(params)
    body     = ctx.expr()
    captured = dict(self.variables)
    outer    = self

    class LambdaFn:
        def __init__(self, collected=None):
            self.collected  = collected[:] if collected else []
            self._signature = lam_sig
            self._total     = total

        @property
        def signature(self):
            return self._signature

        def __str__(self):
            raise Exception(
                f"'<lambda>' expects {self._total} args, got {len(self.collected)}"
            )
        __repr__ = __str__

        def __call__(self, *args):
            ncol = len(self.collected) + len(args)
            if ncol > self._total:
                raiseWrongNumberOfArgs("<lambda>", self._total, ncol)

            new_vals = self.collected + list(args)
            if ncol < self._total:
                return LambdaFn(new_vals)

            saved = outer.variables
            outer.variables = dict(captured)
            try:
                outer.dentro_bloque = True
                for decl, val in zip(params, new_vals):
                    expected = decl.typeDecl().getText().replace(" ", "")

                    sig_obt = getattr(val, "signature", None)
                    if sig_obt:
                        act_p, act_r = _parse_signature(sig_obt)
                        exp_p, exp_r = _parse_signature(expected)
                        if not (act_p == exp_p and act_r == exp_r):
                            top_act = _get_top_params(sig_obt)
                            top_exp = _get_top_params(expected)
                            if len(top_act) != len(top_exp):
                                pname = decl.ID().getText()
                                raise TypeError(
                                    f"Function parameter '{pname}' "
                                    f"must accept {len(top_exp)} parameter(s), "
                                    f"but got {len(top_act)}."
                                )

                    check_value_type(val, expected)
                    pid   = decl.ID().getText()
                    ptype = funcion_t if expected.startswith("FUNC") else expected
                    asignar_variable(outer, pid, val, ptype)

                outer.dentro_bloque = False
                return outer.visit(body)
            finally:
                outer.variables = saved

    return LambdaFn()

def functionCall(self, ctx):
    name     = ctx.ID().getText()
    if name not in self.variables:
        raiseFunctionNotDefined(name)
    func     = self.variables[name][1]
    children = list(ctx.getChildren())
    i        = 0
    while i < len(children):
        if children[i].getText() == "(":
            if (i + 1 < len(children)
                and isinstance(children[i+1], Kafe_GrammarParser.ArgListContext)):
                args = [self.visit(a) for a in children[i+1].arg()]
                func = func(*args)
                i   += 3
            else:
                func = func()
                i   += 2
        else:
            i += 1
    return func

def returnStmt(self, ctx):
    raise ReturnValue(self.visit(ctx.expr()))

@check_sig([2], lista_cualquiera_t, todos_t, func_nombre="append")
def visitAppendCall(lista, elem):
    lista.append(elem)

@check_sig([2], lista_cualquiera_t, todos_t, func_nombre="remove")
def visitRemoveCall(lista, elem):
    lista.remove(elem)
    return None

@check_sig([1], lista_cualquiera_t, func_nombre="len")
def visitLenCall(lista):
    return len(lista)

@check_sig([1, 2, 3], [entero_t], [entero_t], [entero_t], func_nombre="range")
def rangeExpr(*args):
    start = None
    stop = None
    step = None

    stop = args[0]

    if len(args) >= 2:
        start = args[0]
        stop = args[1]

    if len(args) == 3:
        step = args[2]

    if len(args) == 1:
        return list(range(stop))
    elif len(args) == 2:
        return list(range(start, stop))
    else:
        return list(range(start, stop, step))

def showStmt(self, ctx):
    val = self.visit(ctx.expr())
    if hasattr(val, 'total') and hasattr(val, 'collected') and len(val.collected) < val.total:
        raiseWrongNumberOfArgs(val.name, val.total, len(val.collected))
    print(val)

def pourStmt(self, ctx):
    return input(self.visit(ctx.expr()))
