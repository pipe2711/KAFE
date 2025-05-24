type_mapping = {"INT": int, "FLOAT": float, "STR": str, "BOOL": bool}
nombre_tipos = { int:"INT", float:"FLOAT", str:"STR", bool:"BOOL", list:"List", "void": "VOID", "func": "FUNC"}

def obtener_tipo_dentro_lista(lista):
    tipo_lista = obtener_tipo_lista(lista)
    return tipo_lista.replace("List[", "").replace(']', "")

def construir_tipo_lista(tipo, anidamiento):
    tipo_construido = "List["

    if anidamiento == 1:
        tipo_construido += nombre_tipos[tipo]
    else:
        tipo_construido += construir_tipo_lista(tipo, anidamiento - 1)

    tipo_construido += "]"

    return tipo_construido

def obtener_tipo_lista(lista):
    tipo = "List["

    if len(lista) != 0:
        if type(lista[0]) is list:
            tipo += obtener_tipo_lista(lista[0])
        else:
            tipo += nombre_tipos[type(lista[0])]

    tipo += ']'

    return tipo

def obtener_tipo_dato(dato):
    if type(dato) is list:
        return obtener_tipo_lista(dato)
    elif callable(dato):
        return "FUNC"
    else:
        return nombre_tipos[type(dato)]
