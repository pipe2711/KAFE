def inferir_tipo(celda):
    if celda == "":
        return float("nan")
    try:
        return int(celda)
    except ValueError:
        try:
            return float(celda)
        except ValueError:
            return celda
