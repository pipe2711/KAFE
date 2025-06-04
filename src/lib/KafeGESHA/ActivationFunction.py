
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from lib.KafeMATH.funciones import exp

class ActivationFunction(ABC):
    """
    Interfaz base para cualquier función de activación.
    """

    @abstractmethod
    def activate(self, x):
        """
        Calcula la salida de la activación para la entrada x (escalares o vectores).
        """
        pass

    @abstractmethod
    def derivative(self, x):
        """
        Devuelve la derivada de la función de activación en x.
        """
        pass


class Sigmoide(ActivationFunction):
    def __init__(self):
        self.last_output = None

    def activate(self, x):
        s = 1.0 / (1.0 + exp(-x))
        self.last_output = s
        return s

    def derivative(self, x):
        # Si activate(x) ya fue llamado, self.last_output ya está calculado.
        if self.last_output is None:
            s = 1.0 / (1.0 + exp(-x))
            return s * (1.0 - s)
        return self.last_output * (1.0 - self.last_output)


class ReLU(ActivationFunction):
    def __init__(self):
        self.last_input = None

    def activate(self, x):
        self.last_input = x
        return x if x > 0 else 0

    def derivative(self, x):
        # Usar last_input para consistencia
        inp = self.last_input if self.last_input is not None else x
        return 1 if inp > 0 else 0


class Tanh(ActivationFunction):
    def __init__(self):
        self.last_output = None

    def activate(self, x):
        e_pos = exp(x)
        e_neg = exp(-x)
        t = (e_pos - e_neg) / (e_pos + e_neg)
        self.last_output = t
        return t

    def derivative(self, x):
        # Si last_output no se ha calculado, lo calculamos:
        if self.last_output is None:
            t = self.activate(x)
            return 1.0 - t * t
        return 1.0 - self.last_output * self.last_output


class Identidad(ActivationFunction):
    def activate(self, x):
        return x

    def derivative(self, x):
        return 1.0


class Escalonada(ActivationFunction):
    def activate(self, x):
        return 1 if x >= 0 else 0

    def derivative(self, x):
        # No es diferenciable en x=0; se define como 0
        return 0.0


class Softmax(ActivationFunction):
    """
    Softmax para vectores completos. Debe usarse preferiblemente junto a CategoricalCrossEntropy,
    pues la derivada manual de softmax en red completa es costosa. 
    """

    def __init__(self):
        self.last_output = None

    def activate(self, vec):
        """
        vec: lista de números
        devuelve: lista de probabilidades (suma=1)
        """
        exp_vec = [exp(x) for x in vec]
        s = sum(exp_vec)
        salida = [v / s for v in exp_vec]
        self.last_output = salida[:]
        return salida

    def derivative(self, vec):
        """
        Devuelve la matriz Jacobiana de Softmax: J_ij = s_i * (δ_ij - s_j).
        vec: lista de números (cada elemento x_i)
        """
        # Primero recalculamos la activación para obtener s
        s = self.activate(vec)
        size = len(s)
        jacobian = [[0.0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if i == j:
                    jacobian[i][j] = s[i] * (1.0 - s[i])
                else:
                    jacobian[i][j] = - s[i] * s[j]
        return jacobian

    # Observación: en la práctica, al usar Softmax + CategoricalCrossEntropy,
    # suele emplearse la derivada simplificada: y_pred - y_true para evitar cálculo de la jacobiana completa.