# lib/KafeGESHA/utils.py

import warnings

def warn_if(condición, mensaje):
    """
    Lanza una advertencia (warning) si la condición es True.
    """
    if condición:
        warnings.warn(mensaje, stacklevel=2)

def check_regularization(value):
    """
    Verifica que el valor de regularización sea >= 0. En caso contrario, lanza ValueError.
    """
    if value is None:
        return 0.0
    try:
        val = float(value)
    except:
        raise ValueError("El parámetro de regularización debe ser numérico o None.")
    if val < 0:
        raise ValueError("El parámetro de regularización no puede ser negativo.")
    return val