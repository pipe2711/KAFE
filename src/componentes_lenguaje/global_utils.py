from .errores import raiseTypeMismatch

def verificar_tipo(tipo, tipo_valor):
    tipo_original = tipo

    if tipo.startswith("FUNC"):
        tipo = tipo[:4]

    if tipo_valor.startswith("List") and tipo_original.startswith("List"):
        no_tiene_valores = not any(t in tipo_valor for t in ["INT","FLOAT","STR","BOOL"])
        es_lista_vacia = tipo_valor == "List[]"

        if es_lista_vacia:
            tipo_valor = tipo_original
        elif no_tiene_valores:
            tipo = tipo.replace("INT","").replace("FLOAT","").replace("STR","").replace("BOOL","")

    if tipo != tipo_valor:
        raiseTypeMismatch(tipo_valor, tipo_original)

def asignar_variable(self, name, valor, tipo):
    tipo_valor = self.obtener_tipo_dato(valor)

    verificar_tipo(tipo, tipo_valor)

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
