def verificar_misma_dimension(matriz1, matriz2):
    if len(matriz1) != len(matriz2):
        raise Exception("numkadd: Matrices don't have the same dimension")
    for i in range(len(matriz1)):
        if len(matriz1[i]) != len(matriz2[i]):
            raise Exception("numkadd: Matrices don't have the same dimension")

    return

def obtener_matrices(self, ctx):
    # Obtener las matrices
    matriz1 = self.visit(ctx.expr(0))
    matriz2 = self.visit(ctx.expr(1))

    if verificar_matriz_cuadrada(matriz1) == False or verificar_matriz_cuadrada(matriz2) == False:
        raise Exception("numkadd: Expected matrices as arguments")

    return (matriz1, matriz2)

def verificar_matriz_cuadrada(lst, depth=1):
    if not isinstance(lst, list):
        return False

    if depth > 2:
        return False
    for item in lst:
        if isinstance(item, list):
            if not verificar_matriz_cuadrada(item, depth + 1):
                return False
    return True
