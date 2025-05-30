from errores import raiseVariableIsNotObject, raiseFunctionNotDefined, raiseVariableNotDefined

def esObjeto(var):
    if isinstance(var, (str, int, float, bool, type(None))):
        return False
    return True

def objectFunctionCall(object_t, function_name, args):
    if not esObjeto(object_t):
        raiseVariableIsNotObject()

    func = getattr(object_t, function_name, None)

    if func is None:
        raiseFunctionNotDefined(function_name)

    resultado = func(*args)

    return resultado

def objectConstant(object_t, constant_name):
    if not esObjeto(object_t):
        raiseVariableIsNotObject()

    const = getattr(object_t, constant_name, None)

    if const is None:
        raiseVariableNotDefined(constant_name)

    return const
