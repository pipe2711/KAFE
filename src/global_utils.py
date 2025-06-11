from errores import raiseTypeMismatch, raiseFunctionIncorrectArgumentType, raiseWrongNumberOfArgs
from TypeUtils import obtener_tipo_dato, entero_t, flotante_t, booleano_t, cadena_t, funcion_t, lista_t, lista_cualquiera_t

def esTipoCorrecto(valor, tipo_definido):
    tipo_valor = obtener_tipo_dato(valor)

    if tipo_definido.startswith(funcion_t):
        tipo_definido = tipo_definido[:4]

    if tipo_valor.startswith(lista_t) and tipo_definido.startswith(lista_t):
        posibles_tipos_internos = [entero_t, flotante_t, booleano_t, cadena_t]

        tipo_valor_no_tiene_tipo_interno = not any(t in tipo_valor for t in posibles_tipos_internos)
        tipo_definido_no_tiene_tipo_interno = not any(t in tipo_definido for t in posibles_tipos_internos)

        es_lista_vacia = tipo_valor == obtener_tipo_dato([])

        if es_lista_vacia:
            tipo_valor = tipo_definido
        elif tipo_valor_no_tiene_tipo_interno or tipo_definido_no_tiene_tipo_interno:
            tipo_definido = tipo_definido.replace(entero_t,"").replace(flotante_t,"")
            tipo_definido = tipo_definido.replace(cadena_t,"").replace(booleano_t,"")
            tipo_valor = tipo_valor.replace(entero_t,"").replace(flotante_t,"")
            tipo_valor = tipo_valor.replace(cadena_t,"").replace(booleano_t,"")


    if tipo_definido != tipo_valor:
        return False
    else:
        return True

def asignar_variable(self, name, valor, tipo):
    if not esTipoCorrecto(valor, tipo):
        raiseTypeMismatch(valor, tipo)

    self.variables[name] = (tipo, valor)

def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def obtener_nivel_anidamiento(lista):
    if not isinstance(lista, list):
        return 0

    max_depth = 0
    for item in lista:
        if isinstance(item, list):
            depth = obtener_nivel_anidamiento(item)
            if depth > max_depth:
                max_depth = depth

    return max_depth + 1

def verificarHomogeneidad(lista):
    if len(lista) != 0:
        anidamiento = obtener_nivel_anidamiento(lista[0])
        for elemento in lista:
            if obtener_nivel_anidamiento(elemento) != anidamiento:
                return False

    lista = flatten_list(lista)
    if (len(lista) != 0):
        tipo = type(lista[0])
        for elemento in lista:
            if type(elemento) != tipo:
                return False

    return True

def check_sig(*args, **kwargs):

    num_args = args[0]

    arg_types = []
    for i in range(1, len(args)):
        arg_types.append(args[i])

    if kwargs.get('func_nombre') != None:
        func_nombre = kwargs['func_nombre']
    else:
        func_nombre = ""

    def decorator(original_function):
        if func_nombre == "":
            nombre = original_function.__name__
        else:
            nombre = func_nombre

        def new_function(*args, **kwargs):
            if len(args) not in num_args:
                raiseWrongNumberOfArgs(nombre, num_args, len(args))

            for i, arg in enumerate(args):
                tipos_definidos = arg_types[i]
                coincidencias = [esTipoCorrecto(arg, tipo_definido) for tipo_definido in tipos_definidos]

                if not any(coincidencias):
                    if set(lista_cualquiera_t).issubset(tipos_definidos):
                        tipos_definidos = list(set(tipos_definidos) - set(lista_cualquiera_t))
                        tipos_definidos.append("lists")

                    raiseFunctionIncorrectArgumentType(nombre, arg, tipos_definidos)


            return original_function(*args, **kwargs)

        return new_function
    return decorator
