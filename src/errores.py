from TypeUtils import obtener_tipo_dato, void_t

def raiseVoidAsVariableType():
    message = f"{void_t} cannot be used as variable type"
    raise TypeError(message)

def raiseVoidAsParameterType():
    message = f"{void_t} cannot be used as parameter type"
    raise TypeError(message)

def raiseFunctionAlreadyDefined(function_name):
    message = f"Function '{function_name}' already defined"
    raise NameError(message)

def raiseVariableAlreadyDefined(variable_name):
    message = f"Variable '{variable_name}' already defined"
    raise NameError(message)

def raiseFunctionNotDefined(function_name):
    message = f"Function '{function_name}' not defined"
    raise NameError(message)

def raiseVariableNotDefined(variable_name):
    message = f"Variable '{variable_name}' not defined"
    raise NameError(message)

def raiseExpectedHomogeneousList():
    message = "Expected homogeneous list"
    raise Exception(message)

def raiseNonIntegerIndex(valor):
    tipo = obtener_tipo_dato(valor)
    message = f"Index must be an integer, got {tipo}"
    raise IndexError(message)

def raiseIndexOutOfBounds(index, length):
    message = f"Index {index} out of bounds for collection of size {length}"
    raise IndexError(message)

def raiseTypeMismatch(variable, tipo_definido):
    tipo_valor = obtener_tipo_dato(variable)
    message = f"Expected {tipo_definido}, obtained {tipo_valor}"
    raise TypeError(message)

def raiseFunctionIncorrectArgumentType(function_name, valor, tipo_definido):
    tipo_valor = obtener_tipo_dato(valor)

    if type(tipo_definido) == list:
        tipos_esperados = ""
        for i in range(len(tipo_definido) - 1):
            tipos_esperados += tipo_definido[i] + " or "
        tipos_esperados += tipo_definido[len(tipo_definido) - 1]
    else:
        tipos_esperados = tipo_definido

    message = f"Function {function_name} expects argument of type {tipos_esperados}, got type {tipo_valor}"
    raise TypeError(message)

def raiseConditionMustBeBoolean(place, variable):
    tipo = obtener_tipo_dato(variable)

    message = f"Condition in {place} must be boolean, got {tipo}"
    raise TypeError(message)

def raiseExceededIterationCount():
    message = "Maximum number of iterations exceeded in while loop (possible infinite loop)"
    raise RuntimeError(message)

def raiseNonIterableVariable(variable):
    tipo = obtener_tipo_dato(variable)

    message = f"Variable in for must be iterable (list or string or range), got {tipo}"
    raise TypeError(message)

def raiseWrongNumberOfArgs(function_name, num_args, recv_args):
    if type(num_args) == list:
        num_args_str = ""
        for i in range(len(num_args) - 1):
            num_args_str += num_args[i] + " or "
        num_args_str += str(num_args[len(num_args) - 1])
    else:
        num_args_str = num_args

    message = f"'{function_name}' expects {num_args_str} args, got {recv_args}"
    raise Exception(message)

def raiseModuleNotFound(module_name, path):
    message = f"Module file for '{module_name}' not found. Tried: {path}"
    raise FileNotFoundError(message)

def raiseRuntimeError(place, exception):
    message = f"Error in {place} block: {str(exception)}"
    raise RuntimeError(message)

def raiseFunctionCantReturnVoid():
    message = f"Function declared {void_t} must not return a value"
    raise TypeError(message)

def raiseLibraryNotImported():
    message = "library not imported"
    raise Exception(message)

def raiseVariableIsNotObject():
    message = "variable is not of type object"
    raise Exception(message)

def raiseFileAlreadyExists(nombre, ruta):
    message = f"File '{nombre}' already exists at {ruta}"
    raise FileExistsError(message)

def raiseFileNotFound(nombre, ruta):
    message = f"File '{nombre}' not found at {ruta}"
    raise FileNotFoundError(message)

def raiseSignatureMismatch(expected_signature, obtained_signature, origin=""):
    message = f"Expected {expected_signature}, obtained {obtained_signature}"
    if origin:
        message = origin + ": " + message
    raise TypeError(message)