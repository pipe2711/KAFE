# lib/KafeGESHA/funciones.py

from lib.KafeGESHA.GeshaDeep import GeshaDeep
from lib.KafeGESHA.Dense import Dense

# ————————————————
# Fábricas de modelos:
# ————————————————

def categorical():
    """
    Crea y devuelve un modelo de clasificación (categorical).
    """
    return GeshaDeep(model_type="classification")

def clustering():
    """
    Crea y devuelve un modelo de clustering (no supervisado).
    """
    return GeshaDeep(model_type="clustering")

def regression():
    """
    Crea y devuelve un modelo de regresión.
    """
    return GeshaDeep(model_type="regression")


# ————————————————
# Helper para capa Dense:
# ————————————————

def create_dense(units, activation, input_shape, regularization_lambda):
    """
    Crea y devuelve una capa Dense.
    
    Parámetros:
    - units: número de unidades (neuronas) en la capa.
    - activation: nombre de la función de activación (string).
    - input_shape: lista o tupla con la forma de entrada (ej. [784]). 
                   Si se deja vacía, se hereda de la capa anterior.
    - regularization_lambda: coeficiente de L2 para regularización (float).
    """
    return Dense(units, activation, input_shape, regularization_lambda)
