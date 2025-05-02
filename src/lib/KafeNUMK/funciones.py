from lib.KafeNUMK.utils import verificar_misma_dimension, obtener_matrices, verificar_matriz_cuadrada

def numkadd(self, ctx):
    if len(ctx.expr()) != 2:
        raise Exception("numkadd: Expected 2 arguments")

    matriz1, matriz2 = obtener_matrices(self, ctx)
    verificar_misma_dimension(matriz1, matriz2)

    # Sumar las matrices
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[i])):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)

    return resultado

def numksub(self, ctx):
    if len(ctx.expr()) != 2:
        raise Exception("numkadd: Expected 2 arguments")

    matriz1, matriz2 = obtener_matrices(self, ctx)
    verificar_misma_dimension(matriz1, matriz2)

    # Restar las matrices
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[i])):
            fila.append(matriz1[i][j] - matriz2[i][j])
        resultado.append(fila)

    return resultado

def numkmul(self, ctx):
    if len(ctx.expr()) != 2:
        raise Exception("numkadd: Expected 2 arguments")

    matriz1, matriz2 = obtener_matrices(self, ctx)

    # Verificar si las matrices son compatibles para la multiplicación
    if len(matriz1[0]) != len(matriz2):
        raise Exception("numkmul: Matrices are not compatible for multiplication")

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

def numkinv(self, ctx):
    matriz = self.visit(ctx.expr())

    if verificar_matriz_cuadrada(matriz) == False:
        raise Exception("numkadd: Expected matrix as argument")

    # Verificar que la matriz sea cuadrada
    if len(matriz) != len(matriz[0]):
        raise Exception("numkinv: Matrix is not square")

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
            raise Exception("numkinv: Matrix is singular")
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

def numktranspose(self, ctx):
    matriz = self.visit(ctx.expr())

    if verificar_matriz_cuadrada(matriz) == False:
        raise Exception("numkadd: Expected matrix as argument")

    transpuesta = []

    for i in range(len(matriz[0])):
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        transpuesta.append(fila)

    return transpuesta
