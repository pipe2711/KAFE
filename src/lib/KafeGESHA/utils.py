from lib.KafeMATH.funciones import exp, pow_
from  lib.KafeNUMK.funciones import shape,dot,dot_matrix,zeros,zeros_matrix

def escalonada(x):
    return 1 if x >= 0 else 0

def sigmoide(x):
    return 1 / (1 + exp(-x))

def relu(x):
    return x if x > 0 else 0

def identidad(x):
    return x

def tanh(x):
    e_pos = exp(x)
    e_neg = exp(-x)
    return (e_pos - e_neg) / (e_pos + e_neg)

def softmax(vec):
    """Softmax aplicada a un vector de valores"""
    exp_vec = [exp(x) for x in vec]
    suma = sum(exp_vec)
    return [x / suma for x in exp_vec]

def activar(nombre: str):
    funciones = {
        "escalonada": escalonada,
        "sigmoide": sigmoide,
        "relu": relu,
        "tanh": tanh,
        "identidad": identidad,
    }
    if nombre not in funciones:
        raise ValueError(f"Función de activación '{nombre}' no soportada.")
    return funciones[nombre]

