from .errores import raiseDifferentDimension, raiseNonUniformMatrix
from .utils import es_misma_dimension, es_uniforme, operar_matrices
from TypeUtils import matriz_cualquiera_t, matriz_numeros_t, vector_numeros_t, entero_t
from global_utils import check_sig

@check_sig([2], matriz_numeros_t, matriz_numeros_t)
def add(matriz1, matriz2):
    if not es_misma_dimension(matriz1, matriz2):
        raiseDifferentDimension('add')

    return operar_matrices(matriz1, matriz2, lambda x, y: x + y)

@check_sig([2], matriz_numeros_t, matriz_numeros_t)
def sub(matriz1, matriz2):
    if not es_misma_dimension(matriz1, matriz2):
        raiseDifferentDimension('sub')

    return operar_matrices(matriz1, matriz2, lambda x, y: x - y)

@check_sig([2], matriz_numeros_t, matriz_numeros_t)
def mul(matriz1, matriz2):
    if not es_uniforme(matriz1) or not es_uniforme(matriz2):
        raiseNonUniformMatrix('mul')

    # Verificar si las matrices son compatibles para la multiplicación
    if len(matriz1) != 0 and len(matriz1[0]) != len(matriz2):
        raise Exception("mul: Matrices are not compatible for multiplication")

    # Multiplicar las matrices
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz2[0])):
            suma = 0
            for k in range(len(matriz2)):
                suma += matriz1[i][k] * matriz2[k][j]
            fila.append(suma)
        resultado.append(fila)

    return resultado

@check_sig([1], matriz_numeros_t)
def inv(matriz):
    if not es_uniforme(matriz):
        raiseNonUniformMatrix('inv')

    # Verificar que la matriz sea cuadrada
    if len(matriz) != 0 and len(matriz) != len(matriz[0]):
        raise Exception("inv: Matrix is not square")

    # Calcular la inversa de la matriz
    n = len(matriz)
    m = len(matriz[0])

    # Crear la matriz identidad
    identidad = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        identidad[i][i] = 1

    # Crear la matriz aumentada
    matriz_aumentada = [fila + identidad[i] for i, fila in enumerate(matriz)]

    m *= 2

    # Aplicar el método de Gauss-Jordan
    for i in range(n):
        # Hacer que el elemento diagonal sea 1
        factor = matriz_aumentada[i][i]
        if factor == 0:
            raise Exception("inv: Matrix is singular")
        for j in range(m):
            matriz_aumentada[i][j] /= factor
        # Hacer que los elementos de la columna sean 0
        for k in range(n):
            if k != i:
                factor = matriz_aumentada[k][i]
                for j in range(m):
                    matriz_aumentada[k][j] -= factor * matriz_aumentada[i][j]

    # Obtener la matriz inversa
    inversa = [fila[n:] for fila in matriz_aumentada]

    return inversa

@check_sig([1], [matriz_cualquiera_t])
def transpose(matriz):
    return list(map(list, zip(*matriz)))


#================== Agregando mas funciones NUMK para GESHA =========================

@check_sig([2], vector_numeros_t, vector_numeros_t)
def dot(vec1, vec2):
    if len(vec1) != len(vec2):
        raiseDifferentDimension('dot')

    return sum(x * y for x, y in zip(vec1, vec2))


@check_sig([2], matriz_numeros_t, matriz_numeros_t)
def dot_matrix(m1, m2):
    if not es_uniforme(m1) or not es_uniforme(m2):
        raiseNonUniformMatrix('dot')

    if len(m1[0]) != len(m2):
        raiseDifferentDimension('dot_matrix')

    resultado = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m2[0])):
            suma = 0
            for k in range(len(m2)):
                suma += m1[i][k] * m2[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

@check_sig([1], [entero_t])
def zeros(n):
    """Genera un vector de ceros de tamaño n"""
    return [0 for _ in range(n)]

@check_sig([2], [entero_t], [entero_t])
def zeros_matrix(filas, columnas):
    """Genera una matriz de ceros tamaño filas x columnas"""
    return [[0 for _ in range(columnas)] for _ in range(filas)]

@check_sig([1], [matriz_cualquiera_t])
def shape(obj):
    dimensiones = []
    while isinstance(obj, list):
        dimensiones.append(len(obj))
        if len(obj) == 0:
            break
        obj = obj[0]
    return tuple(dimensiones)
