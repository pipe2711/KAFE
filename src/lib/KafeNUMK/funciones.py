from componentes_lenguaje.errores import raiseWrongNumberOfArgs, raiseFunctionIncorrectArgumentType
from lib.KafeNUMK.utils import verificar_misma_dimension, obtener_matrices, verificar_matriz_2dim

class Numk:
    def __init__(self):
        self.nombre_lib = "numk"
        self.funciones = {
            "add": "add",
            "sub": "sub",
            "mul": "mul",
            "inv": "inv",
            "transpose": "transpose"
        }

    def operar_matrices(self, matriz1, matriz2, operacion):
        # Sumar las matrices
        resultado = []
        for i in range(len(matriz1)):
            fila = []
            for j in range(len(matriz1[i])):
                fila.append(operacion(matriz1[i][j], matriz2[i][j]))
            resultado.append(fila)

        return resultado

    def add(self, matriz1, matriz2):
        return self.operar_matrices(matriz1, matriz2, lambda x, y: x + y)

    def sub(self, matriz1, matriz2):
        return self.operar_matrices(matriz1, matriz2, lambda x, y: x - y)

    def mul(self, matriz1, matriz2):
        # Verificar si las matrices son compatibles para la multiplicación
        if len(matriz1[0]) != len(matriz2):
            raise Exception(f"{self.nombre_lib}.{self.funciones['mul']}: Matrices are not compatible for multiplication")

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

    def inv(self, matriz):
        # Verificar que la matriz sea cuadrada
        if len(matriz) != len(matriz[0]):
            raise Exception(f"{self.nombre_lib}.{self.funciones['inv']}: Matrix is not square")

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
                raise Exception(f"{self.nombre_lib}.{self.funciones['inv']}: Matrix is singular")
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

    def transpose(self, matriz):
        # Transponer la matriz
        transpuesta = []

        for i in range(len(matriz[0])):
            fila = []
            for j in range(len(matriz)):
                fila.append(matriz[j][i])
            transpuesta.append(fila)

        return transpuesta

def numkadd(self, ctx, numk):
    nombre_funcion = numk.funciones["add"]

    if len(ctx.expr()) != 2:
        raiseWrongNumberOfArgs(nombre_funcion, 2, len(ctx.expr()), origin=numk.nombre_lib)

    matriz1, matriz2 = obtener_matrices(self, ctx, numk.nombre_lib, nombre_funcion)
    verificar_misma_dimension(matriz1, matriz2, numk.nombre_lib, nombre_funcion)

    return numk.add(matriz1, matriz2)

def numksub(self, ctx, numk):
    nombre_funcion = numk.funciones["sub"]
    if len(ctx.expr()) != 2:
        raiseWrongNumberOfArgs(nombre_funcion, 2, len(ctx.expr()), origin=numk.nombre_lib)

    matriz1, matriz2 = obtener_matrices(self, ctx, numk.nombre_lib, nombre_funcion)
    verificar_misma_dimension(matriz1, matriz2, numk.nombre_lib, nombre_funcion)

    return numk.sub(matriz1, matriz2)

def numkmul(self, ctx, numk):
    nombre_funcion = numk.funciones["mul"]
    if len(ctx.expr()) != 2:
        raiseWrongNumberOfArgs(nombre_funcion, 2, len(ctx.expr()), origin=numk.nombre_lib)

    matriz1, matriz2 = obtener_matrices(self, ctx, numk.nombre_lib, nombre_funcion)
    return numk.mul(matriz1, matriz2)

def numkinv(self, ctx, numk):
    matriz = self.visit(ctx.expr())

    if verificar_matriz_2dim(matriz) == False:
        raiseFunctionIncorrectArgumentType(numk.funciones['inv'], matriz, "matrix", origin=numk.nombre_lib)

    return numk.inv(matriz)

def numktranspose(self, ctx, numk):
    matriz = self.visit(ctx.expr())

    if verificar_matriz_2dim(matriz) == False:
        raiseFunctionIncorrectArgumentType(numk.funciones['inv'], matriz, "matrix", origin=numk.nombre_lib)

    return numk.transpose(matriz)
