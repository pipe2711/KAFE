from TypeUtils import nombre_tipos, obtener_tipo_dato

def raiseVoidAsVariableType(origin=""):
    message = f"{nombre_tipos['void']} cannot be used as variable type"
    if origin:
        message = origin + ": " + message
    raise TypeError(message)

def raiseVoidAsParameterType(origin=""):
    message = f"{nombre_tipos['void']} cannot be used as parameter type"
    if origin:
        message = origin + ": " + message
    raise TypeError(message)

def raiseFunctionAlreadyDefined(function_name, origin=""):
    message = f"Function '{function_name}' already defined"
    if origin:
        message = origin + ": " + message
    raise NameError(message)

def raiseVariableAlreadyDefined(variable_name, origin=""):
    message = f"Variable '{variable_name}' already defined"
    if origin:
        message = origin + ": " + message
    raise NameError(message)

def raiseFunctionNotDefined(function_name, origin=""):
    message = f"Function '{function_name}' not defined"
    if origin:
        message = origin + ": " + message
    raise NameError(message)

def raiseVariableNotDefined(variable_name, origin=""):
    message = f"Variable '{variable_name}' not defined"
    if origin:
        message = origin + ": " + message
    raise NameError(message)

def raiseExpectedHomogeneousList(origin=""):
    message = "Expected homogeneous list"
    if origin:
        message = origin + ": " + message
    raise Exception(message)

def raiseNonIntegerIndex(valor, origin=""):
    tipo = obtener_tipo_dato(valor)
    message = f"Index must be an integer, got {tipo}"
    if origin:
        message = origin + ": " + message
    raise IndexError(message)

def raiseIndexOutOfBounds(index, length, origin=""):
    message = f"Index {index} out of bounds for collection of size {length}"
    if origin:
        message = origin + ": " + message
    raise IndexError(message)

def raiseTypeMismatch(variable, tipo_definido, origin=""):
    tipo_valor = obtener_tipo_dato(variable)
    message = f"Expected {tipo_definido}, obtained {tipo_valor}"
    if origin:
        message = origin + ": " + message
    raise TypeError(message)

def raiseFunctionIncorrectArgumentType(function_name, valor, tipo_definido, origin=""):
    tipo_valor = obtener_tipo_dato(valor)

    if type(tipo_definido) == list:
        tipos_esperados = ""
        for i in range(len(tipo_definido) - 1):
            tipos_esperados += tipo_definido[i] + " or "
        tipos_esperados += tipo_definido[len(tipo_definido) - 1]
    else:
        tipos_esperados = tipo_definido

    message = f"Function {function_name} expects argument of type {tipos_esperados}, got type {tipo_valor}"
    if origin:
        message = origin + ": " + message
    raise TypeError(message)

def raiseConditionMustBeBoolean(place, variable, origin=""):
    tipo = obtener_tipo_dato(variable)

    message = f"Condition in {place} must be boolean, got {tipo}"
    if origin:
        message = origin + ": " + message
    raise TypeError(message)

def raiseExceededIterationCount(origin=""):
    message = "Maximum number of iterations exceeded in while loop (possible infinite loop)"
    if origin:
        message = origin + ": " + message
    raise RuntimeError(message)

def raiseNonIterableVariable(variable, origin=""):
    tipo = obtener_tipo_dato(variable)

    message = f"Variable in for must be iterable (list or string), got {tipo}"
    if origin:
        message = origin + ": " + message
    raise TypeError(message)

def raiseWrongNumberOfArgs(function_name, num_args, recv_args, origin=""):
    message = f"'{function_name}' expects {num_args} args, got {recv_args}"
    if origin:
        message = origin + ": " + message
    raise Exception(message)

def raiseModuleNotFound(module_name, path, origin=""):
    message = f"Module file for '{module_name}' not found. Tried: {path}"
    if origin:
        message = origin + ": " + message
    raise FileNotFoundError(message)

def raiseRuntimeError(place, exception, origin=""):
    message = f"Error in {place} block: {str(exception)}"
    if origin:
        message = origin + ": " + message
    raise RuntimeError(message)

def raiseFunctionCantReturnVoid(origin=""):
    message = f"Function declared {nombre_tipos['void']} must not return a value"
    if origin:
        message = origin + ": " + message
    raise TypeError(message)

def raiseLibraryNotImported(library, origin=""):
    message = f"{library} library not imported"
    if origin:
        message = origin + ": " + message
    raise Exception(message)
