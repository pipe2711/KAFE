import warnings

def warn_if(condición, mensaje):
    if condición:
        warnings.warn(mensaje, stacklevel=2)

def check_regularization(value):
    if value is None:
        return 0.0
    try:
        val = float(value)
    except:
        raise ValueError("El parámetro de regularización debe ser numérico o None.")
    if val < 0:
        raise ValueError("El parámetro de regularización no puede ser negativo.")
    return val
