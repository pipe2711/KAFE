# lib/KafeGESHA/Dense.py

import random
from lib.KafeGESHA.Gesha import Gesha
from lib.KafeGESHA.utils import check_regularization
from lib.KafeGESHA.ActivationFunctionLoader import ActivationFunctionLoader

class Dense(Gesha):
    """
    Capa totalmente conectada (Dense) con soporte L2.
    """

    def __init__(self, units, activation=None, input_shape=None, regularization_lambda=0.0):
        super().__init__()
        self.units = units
        self.activation_name = activation
        self.activation = ActivationFunctionLoader.get(activation)
        self.input_shape = input_shape

        self.weights = None
        self.bias = None
        self.last_input = None
        self.last_z = None

        self.regularization_lambda = check_regularization(regularization_lambda)

    def _random_matrix(self, rows, cols):
        return [
            [(random.random() - 0.5) for _ in range(cols)]
            for _ in range(rows)
        ]

    def _zeros_vector(self, length):
        return [0.0 for _ in range(length)]

    def build(self, input_dim):
        self.weights = self._random_matrix(input_dim, self.units)
        self.bias = self._zeros_vector(self.units)

    def forward(self, x):
        """
        Propagación hacia adelante. Si la activación es 'softmax',
        aplicarla sobre el vector completo de pre-activaciones.
        """
        self.last_input = x[:]
        if self.weights is None:
            self.build(len(x))

        # 1) Calcular pre-activaciones z_j = Σ_i x_i * w_ij + b_j
        z = []
        for j in range(self.units):
            suma = 0.0
            for i in range(len(x)):
                suma += x[i] * self.weights[i][j]
            suma += self.bias[j]
            z.append(suma)
        self.last_z = z[:]

        # 2) Si la activación es softmax, aplicarla sobre todo z
        if self.activation_name and self.activation_name.lower() == "softmax":
            return self.activation.activate(z)

        # 3) En caso contrario, aplicar activación elemento a elemento
        return [self.activation.activate(val) for val in z]

    def backward(self, output_error, learning_rate, regularization_lambda=None):
        """
        Retropropagación:
        - output_error: vector [units], ∂L/∂a_j para capa actual.
        - learning_rate: float
        - regularization_lambda: opcional; por defecto self.regularization_lambda.
        Retorna: input_error (lista de tamaño input_dim), ∂L/∂x_i.
        """
        if regularization_lambda is None:
            regularization_lambda = self.regularization_lambda

        # 1) dL/dz_j
        if self.activation_name and self.activation_name.lower() == "softmax":
            # Para Softmax + CCE, el gradiente dL/dz es precisamente output_error
            dL_dz = output_error[:]
        else:
            # Para las demás activaciones, multiplicar error por derivada local
            dL_dz = []
            for j in range(self.units):
                deriv = self.activation.derivative(self.last_z[j])
                dL_dz.append(output_error[j] * deriv)

        # 2) Calcular gradientes de pesos y bias
        input_dim = len(self.last_input)
        grad_w = [[0.0] * self.units for _ in range(input_dim)]
        for i in range(input_dim):
            for j in range(self.units):
                grad_w[i][j] = self.last_input[i] * dL_dz[j]
        grad_b = dL_dz[:]

        # 3) L2 regularización (si λ > 0)
        if regularization_lambda > 0:
            for i in range(input_dim):
                for j in range(self.units):
                    grad_w[i][j] += regularization_lambda * self.weights[i][j]

        # 4) Actualizar pesos y bias
        for i in range(input_dim):
            for j in range(self.units):
                self.weights[i][j] -= learning_rate * grad_w[i][j]
        for j in range(self.units):
            self.bias[j] -= learning_rate * grad_b[j]

        # 5) Calcular el error para la capa anterior (∂L/∂x_i)
        input_error = [0.0 for _ in range(input_dim)]
        for i in range(input_dim):
            suma = 0.0
            for j in range(self.units):
                suma += self.weights[i][j] * dL_dz[j]
            input_error[i] = suma

        return input_error

    def summary(self):
        reg_txt = f"L2={self.regularization_lambda}" if self.regularization_lambda > 0 else "sin regularización"
        act_txt = self.activation_name or "linear"
        print(f"Dense(units={self.units}, activation={act_txt}, regularization={reg_txt})")
