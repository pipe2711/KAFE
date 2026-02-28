import warnings
from global_utils import check_sig
from TypeUtils import booleano_t, cadena_t, flotante_t, entero_t, void_t

@check_sig([2], [booleano_t], [cadena_t])
def warn_if(condición, mensaje):
    if condición:
        warnings.warn(mensaje, stacklevel=2)

@check_sig([1], [flotante_t, entero_t, cadena_t, void_t])
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
