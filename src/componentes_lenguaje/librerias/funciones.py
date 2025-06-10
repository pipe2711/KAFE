from errores import raiseLibraryNotImported, raiseFunctionNotDefined, raiseVariableNotDefined

def revisarImportacion(library):
    seImporto = library[1]
    if not seImporto:
        raiseLibraryNotImported()


def libraryFunctionCall(library, function_name, args):
    revisarImportacion(library)
    library_module = library[0]
    func = getattr(library_module, function_name, None)

    if func is None:
        raiseFunctionNotDefined(function_name)

    resultado = func(*args)

    return resultado

def libraryConstant(library, constant_name):
    revisarImportacion(library)
    library_module = library[0]
    const = getattr(library_module, constant_name, None)

    if const is None:
        raiseVariableNotDefined(constant_name)

    return const
