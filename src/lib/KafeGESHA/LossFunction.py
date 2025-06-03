# lib/KafeGESHA/LossFunction.py
# ------------------------------------------------------------
#  Funciones de pérdida para GeshaDeep
#  Incluye BCE robusta que ahora acepta float ó lista [float]
# ------------------------------------------------------------
from abc import ABC, abstractmethod
from lib.KafeMATH.funciones import log, math_abs


# ============================================================ #
#  Interface genérica
# ============================================================ #
class LossFunction(ABC):
    @abstractmethod
    def compute(self, y_true, y_pred):
        """Devuelve el valor promedio de la pérdida"""
        pass

    @abstractmethod
    def derivative(self, y_true, y_pred):
        """Devuelve el gradiente ∂L/∂y_pred"""
        pass


# ============================================================ #
#  1) Pérdidas de regresión
# ============================================================ #
class MeanSquaredError(LossFunction):
    def compute(self, y_true, y_pred):
        errors = [(yt - yp) * (yt - yp) for yt, yp in zip(y_true, y_pred)]
        return sum(errors) / len(errors)

    def derivative(self, y_true, y_pred):
        n = len(y_true)
        return [2 * (yp - yt) / n for yt, yp in zip(y_true, y_pred)]


class MeanAbsoluteError(LossFunction):
    def compute(self, y_true, y_pred):
        errors = [math_abs(yt - yp) for yt, yp in zip(y_true, y_pred)]
        return sum(errors) / len(errors)

    def derivative(self, y_true, y_pred):
        n = len(y_true)
        return [
            ((yp - yt) / math_abs(yp - yt)) / n if yp != yt else 0
            for yt, yp in zip(y_true, y_pred)
        ]


# ============================================================ #
#  2) Pérdidas de clasificación
# ============================================================ #
class BinaryCrossEntropy(LossFunction):
    """
    BCE robusta:
    • Clippea las predicciones al rango (ε, 1-ε).
    • Acepta probabilidad escalar o lista [probabilidad].
    """

    def __init__(self, epsilon: float = 1e-8):
        self.epsilon = epsilon

    # ----- helpers internos ---------------------------------
    def _as_scalar(self, yp):
        """
        Convierte yp a escalar si es [escala].
        Mantiene float si ya lo es.
        """
        return yp[0] if isinstance(yp, list) and len(yp) == 1 else yp

    def _clip(self, p):
        p = self._as_scalar(p)
        return max(self.epsilon, min(1.0 - self.epsilon, p))

    # ----- API pública --------------------------------------
    def compute(self, y_true, y_pred):
        loss = []
        for yt, yp in zip(y_true, y_pred):
            yp_c = self._clip(yp)
            term = -(yt * log(yp_c) + (1 - yt) * log(1 - yp_c))
            loss.append(term)
        return sum(loss) / len(loss)

    def derivative(self, y_true, y_pred):
        grads = []
        for yt, yp in zip(y_true, y_pred):
            yp_c = self._clip(yp)
            grad = (yp_c - yt) / (yp_c * (1 - yp_c) + self.epsilon)
            grads.append(grad)
        return grads


class CategoricalCrossEntropy(LossFunction):
    def __init__(self, epsilon: float = 1e-8):
        self.epsilon = epsilon

    def compute(self, y_true, y_pred):
        loss = [
            -sum(yt_i * log(yp_i + self.epsilon) for yt_i, yp_i in zip(yt, yp))
            for yt, yp in zip(y_true, y_pred)
        ]
        return sum(loss) / len(loss)

    def derivative(self, y_true, y_pred):
        return [
            [yp_i - yt_i for yt_i, yp_i in zip(yt, yp)]
            for yt, yp in zip(y_true, y_pred)
        ]


class SparseCategoricalCrossEntropy(LossFunction):
    def __init__(self, epsilon: float = 1e-8):
        self.epsilon = epsilon

    def compute(self, y_true, y_pred):
        loss = [-log(yp[int(yt)] + self.epsilon) for yt, yp in zip(y_true, y_pred)]
        return sum(loss) / len(loss)

    def derivative(self, y_true, y_pred):
        grads = []
        for yt, yp in zip(y_true, y_pred):
            grad = [yp_i for yp_i in yp]
            grad[int(yt)] -= 1
            grads.append(grad)
        return grads
