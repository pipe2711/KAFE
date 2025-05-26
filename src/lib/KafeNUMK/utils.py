def es_misma_dimension(matriz1, matriz2):
    if len(matriz1) == len(matriz2):
        mismaDimension_filas = True
        for i in range(len(matriz1)):
            if len(matriz1[i]) != len(matriz2[i]):
                mismaDimension_filas = False
                break

        if (mismaDimension_filas):
            return True

    return False

def es_uniforme(matriz):
    if not matriz:
        return True

    longitud_fila = len(matriz[0])
    for fila in matriz:
        if len(fila) != longitud_fila:
            return False
    return True
