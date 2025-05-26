from .errores import raiseDifferentDimension, raiseNonUniformMatrix
from .utils import es_misma_dimension, es_uniforme
from TypeUtils import matriz_cualquiera_t
from global_utils import check_sig

def operar_matrices(matriz1, matriz2, operacion):
    # Sumar las matrices
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[i])):
            fila.append(operacion(matriz1[i][j], matriz2[i][j]))
        resultado.append(fila)

    return resultado

@check_sig([2], [matriz_cualquiera_t], [matriz_cualquiera_t])
def add(matriz1, matriz2):
    if not es_misma_dimension(matriz1, matriz2):
        raiseDifferentDimension('add')

    return operar_matrices(matriz1, matriz2, lambda x, y: x + y)

@check_sig([2], [matriz_cualquiera_t], [matriz_cualquiera_t])
def sub(matriz1, matriz2):
    if not es_misma_dimension(matriz1, matriz2):
        raiseDifferentDimension('sub')

    return operar_matrices(matriz1, matriz2, lambda x, y: x - y)

@check_sig([2], [matriz_cualquiera_t], [matriz_cualquiera_t])
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

@check_sig([1], [matriz_cualquiera_t])
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
