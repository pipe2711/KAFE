
from lib.KafeGESHA.ActivationFunction import Sigmoide, ReLU, Tanh, Identidad, Escalonada, Softmax

class ActivationFunctionLoader:
    @staticmethod
    def get(name):

        if not name:
            return Identidad()
        n = name.lower()
        if n in ("sigmoid", "sigmoide"):
            return Sigmoide()
        if n == "relu":
            return ReLU()
        if n in ("tanh", "tangente"):
            return Tanh()
        if n in ("linear", "identity", "identidad"):
            return Identidad()
        if n in ("step", "escalon", "escalonada"):
            return Escalonada()
        if n == "softmax":
            return Softmax()
        from warnings import warn
        warn(f"Función de activación '{name}' no reconocida. Se usará 'Identidad' por defecto.", stacklevel=2)
        return Identidad()