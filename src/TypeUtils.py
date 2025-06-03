nombre_tipos = { int:"INT", float:"FLOAT", str:"STR", bool:"BOOL", list:"List", "void": "VOID", "func": "FUNC",  "gesha": "GESHA", "pandas": "PANDAS" }

def obtener_tipo_dentro_lista(lista):
    tipo_lista = obtener_tipo_lista(lista)
    return tipo_lista.replace("List[", "").replace(']', "")

def construir_tipo_lista(anidamiento, tipo=None):
    tipo_construido = "List["
    if anidamiento == 1:
        tipo_construido += nombre_tipos[tipo] if tipo != None else ""
    else:
        tipo_construido += construir_tipo_lista(anidamiento - 1, tipo=tipo)
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
    from lib.KafePANDAS.DataFrame import DataFrame
    from lib.KafeGESHA.Gesha import Gesha
    if type(dato) is list:
        return obtener_tipo_lista(dato)
    elif callable(dato):
        return nombre_tipos["func"]
    elif isinstance(dato, Gesha):
        return nombre_tipos["gesha"]
    elif isinstance(dato, DataFrame):
        return nombre_tipos["pandas"]
    else:
        return nombre_tipos[type(dato)]

vector_numeros_t      = [construir_tipo_lista(1, int), construir_tipo_lista(1, float)]
matriz_numeros_t      = [construir_tipo_lista(2, int), construir_tipo_lista(2, float)]
matriz_cualquiera_t   = construir_tipo_lista(2)
lista_cadenas_t         = construir_tipo_lista(1, str)
numeros_t             = [nombre_tipos[int], nombre_tipos[float]]
entero_t              = nombre_tipos[int]
flotante_t            = nombre_tipos[float]
booleano_t            = nombre_tipos[bool]
cadena_t              = nombre_tipos[str]
lista_t               = nombre_tipos[list]
gesha_t               = nombre_tipos["gesha"]
pandas_t              = nombre_tipos["pandas"]
void_t                = nombre_tipos['void']
funcion_t             = nombre_tipos["func"]
lista_cualquiera_t    = [construir_tipo_lista(i) for i in range(1, 100)]
todos_t               = numeros_t + [cadena_t, booleano_t] + lista_cualquiera_t
