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
    """
    Decorador para validar la firma de una función (num_args y tipos).
    Soporta formato tradicional: check_sig(num_args, lista_tipos_1, lista_tipos_2, ...)
    Y nuevo formato variable: check_sig({ num_args_1: (tipos_arg1, tipos_arg2, ...), num_args_2: (...) })
    
    is_method: Si es True, ignora el primer argumento (self) para la validación de tipos, 
               pero lo cuenta para num_args (o puedes ajustar n_recibidos según prefieras).
               Por consistencia con Kafe, n_recibidos incluye self.
    """
    config_variable = None
    num_args_permitidos = []
    lista_tipos_fijos = []

    if isinstance(args[0], dict):
        config_variable = args[0]
        num_args_permitidos = list(config_variable.keys())
    else:
        num_args_permitidos = args[0]
        lista_tipos_fijos = list(args[1:])

    func_nombre = kwargs.get('func_nombre', "")
    is_method = kwargs.get('is_method', False)

    def decorator(original_function):
        nombre = func_nombre if func_nombre else original_function.__name__

        def new_function(*args_recibidos, **kwargs_recibidos):
            n_recibidos = len(args_recibidos) + len(kwargs_recibidos)
            
            if n_recibidos not in num_args_permitidos:
                raiseWrongNumberOfArgs(nombre, num_args_permitidos, n_recibidos)

            # Seleccionar la lista de tipos a validar
            if config_variable:
                tipos_a_validar = config_variable[n_recibidos]
            else:
                tipos_a_validar = lista_tipos_fijos

            # Comenzamos desde 1 si es un método para ignorar 'self'
            start_idx = 1 if is_method else 0

            # Validar cada argumento funcional
            for i, arg in enumerate(args_recibidos[start_idx:]):
                # El índice en tipos_a_validar corresponde al argumento funcional
                # Si hay más argumentos que tipos definidos (y no es variable), el n_args ya falló arriba
                # pero por seguridad checamos que i esté en rango si no es config_variable
                if i >= len(tipos_a_validar):
                    continue 

                tipos_definidos = tipos_a_validar[i]
                coincidencias = [esTipoCorrecto(arg, tipo_definido) for tipo_definido in tipos_definidos]

                if not any(coincidencias):
                    # Manejo especial para lista_cualquiera_t para mostrar "lists" en el error
                    if set(lista_cualquiera_t).issubset(tipos_definidos):
                        tipos_err = list(set(tipos_definidos) - set(lista_cualquiera_t))
                        tipos_err.append("lists")
                    else:
                        tipos_err = tipos_definidos

                    raiseFunctionIncorrectArgumentType(nombre, arg, tipos_err)

            return original_function(*args_recibidos, **kwargs_recibidos)

        return new_function
    return decorator
