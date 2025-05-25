from componentes_lenguaje.errores import raiseTypeMismatch
from TypeUtils import nombre_tipos, obtener_tipo_dato

def esTipoCorrecto(valor, tipo):
    tipo_valor = obtener_tipo_dato(valor)
    tipo_original = tipo

    if tipo.startswith(nombre_tipos["func"]):
        tipo = tipo[:4]

    if tipo_valor.startswith(nombre_tipos[list]) and tipo_original.startswith(nombre_tipos[list]):
        no_tiene_valores = not any(t in tipo_valor for t in [
            nombre_tipos[tipo] for tipo in [int, float, str, bool]
        ])
        es_lista_vacia = tipo_valor == obtener_tipo_dato([])

        if es_lista_vacia:
            tipo_valor = tipo_original
        elif no_tiene_valores:
            tipo = tipo.replace(nombre_tipos[int],"").replace(nombre_tipos[float],"")
            tipo = tipo.replace(nombre_tipos[str],"").replace(nombre_tipos[bool],"")

    if tipo != tipo_valor:
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