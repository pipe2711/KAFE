def obtener_tipo_lista(lista):
    tipo = "List["

    if len(lista) != 0:
        if type(lista[0]) is int:
            tipo += "INT"
        elif type(lista[0]) is float:
            tipo += "FLOAT"
        elif type(lista[0]) is str:
            tipo += "STRING"
        elif type(lista[0]) is bool:
            tipo += "BOOL"
        else:
            tipo += obtener_tipo_lista(lista[0])

    tipo += ']'

    return tipo

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
