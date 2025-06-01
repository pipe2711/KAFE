from abc import ABC, abstractmethod
from lib.KafeMATH.funciones import exp

class ActivationFunction(ABC):

    @abstractmethod
    def activate(self, x):
        pass

    @abstractmethod
    def derivative(self, x):
        pass


class Sigmoide(ActivationFunction):
    def activate(self, x):
        self.last = 1 / (1 + exp(-x))  # Guarda el valor para usar en derivada
        return self.last

    def derivative(self, x):
        # O usa self.last * (1 - self.last) si `activate` ya fue llamada
        s = 1 / (1 + exp(-x))
        return s * (1 - s)


class ReLU(ActivationFunction):
    def activate(self, x):
        return x if x > 0 else 0

    def derivative(self, x):
        return 1 if x > 0 else 0


class Tanh(ActivationFunction):
    def activate(self, x):
        e_pos = exp(x)
        e_neg = exp(-x)
        self.last = (e_pos - e_neg) / (e_pos + e_neg)
        return self.last

    def derivative(self, x):
        t = self.activate(x)
        return 1 - t**2


class Identidad(ActivationFunction):
    def activate(self, x):
        return x

    def derivative(self, x):
        return 1


class Escalonada(ActivationFunction):
    def activate(self, x):
        return 1 if x >= 0 else 0

    def derivative(self, x):
        return 0  # No derivable en 0, pero se puede definir como 0 o usar heurística

class Softmax(ActivationFunction):
    def activate(self, vec):
        exp_vec = [exp(x) for x in vec]
        suma = sum(exp_vec)
        self.last = [x / suma for x in exp_vec]
        return self.last

    def derivative(self, vec):
        """
        Calcula la matriz Jacobiana de softmax:
        J_ij = s_i * (δ_ij - s_j)
        """
        s = self.activate(vec)
        size = len(s)
        jacobian = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if i == j:
                    jacobian[i][j] = s[i] * (1 - s[i])
                else:
                    jacobian[i][j] = -s[i] * s[j]
        return jacobian

# Softmax normalmente no se usa en derivada directa, sino con cross-entropy simplificada.
# Se puede implementar, pero requiere derivada vectorial (jacobiana), no escalar.
