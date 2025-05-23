from componentes_lenguaje.errores import raiseFunctionIncorrectArgumentType

def verificar_misma_dimension(matriz1, matriz2, nombre_lib, funcion):
    if len(matriz1) == len(matriz2):
        mismaDimension_filas = True
        for i in range(len(matriz1)):
            if len(matriz1[i]) != len(matriz2[i]):
                mismaDimension_filas = False
                break

        if (mismaDimension_filas):
            return

    raise Exception(f"{nombre_lib}.{funcion}: Matrices don't have the same dimension")

def obtener_matrices(self, ctx, nombre_lib, funcion):
    # Obtener las matrices
    matriz1 = self.visit(ctx.expr(0))
    matriz2 = self.visit(ctx.expr(1))

    tipo_matriz1 = self.obtener_tipo_dato(matriz1)
    tipo_matriz2 = self.obtener_tipo_dato(matriz2)

    if verificar_matriz_2dim(matriz1) == False:
        raiseFunctionIncorrectArgumentType(funcion, tipo_matriz1, "matrix", origin=nombre_lib)

    if verificar_matriz_2dim(matriz2) == False:
        raiseFunctionIncorrectArgumentType(funcion, tipo_matriz2, "matrix", origin=nombre_lib)

    return (matriz1, matriz2)

def verificar_matriz_2dim(lst, depth=1):
    if not isinstance(lst, list):
        return False

    if depth > 2:
        return False
    for item in lst:
        if isinstance(item, list):
            if not verificar_matriz_2dim(item, depth + 1):
                return False
    return True
