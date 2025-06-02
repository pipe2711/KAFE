# lib/KafeGESHA/LinearRegression.py

from lib.KafeGESHA.GeshaDeep import GeshaDeep

def regression():
    """
    Crea y devuelve un modelo de regresión (regresión lineal o múltiple).
    Uso típico:
        from lib.KafeGESHA.LinearRegression import regression
        model = regression()
        model.add(Dense(...))
        ...
    """
    return GeshaDeep(model_type="regression")
