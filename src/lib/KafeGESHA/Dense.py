# lib/KafeGESHA/Dense.py
import random
from lib.KafeGESHA.Gesha import Gesha
from lib.KafeGESHA.utils import check_regularization
from lib.KafeGESHA.ActivationFunctionLoader import ActivationFunctionLoader


class Dense(Gesha):
    """
    Capa totalmente conectada reproducible (soporta seed).

    Parámetros
    ----------
    units : int
        Número de neuronas.
    activation : str|None
        Nombre de la función de activación (None → lineal).
    input_shape : sequence|None
        Shape de entrada (sólo en la primera capa).
    regularization_lambda : float
        L2 (≥ 0).
    seed : int|None
        Semilla para que los pesos iniciales sean reproducibles.
    """

    def __init__(
        self,
        units,
        activation=None,
        input_shape=None,
        regularization_lambda=0.0,
        seed=None,
    ):
        super().__init__()
        self.units = units
        self.activation_name = activation
        self.activation = ActivationFunctionLoader.get(activation)
        self.input_shape = input_shape

        # RNG local (no afecta a random global salvo que seed sea None)
        self._rng = random.Random(seed) if seed is not None else random
        self.seed = seed

        self.weights = None
        self.bias = None
        self.last_input = None
        self.last_z = None

        self.regularization_lambda = check_regularization(regularization_lambda)

    # ---------------------------------------------------------------- helpers
    def _random_matrix(self, rows, cols):
        return [[(self._rng.random() - 0.5) for _ in range(cols)] for _ in range(rows)]

    def _zeros_vector(self, n):
        return [0.0 for _ in range(n)]

    # ---------------------------------------------------------------- build
    def build(self, input_dim):
        self.weights = self._random_matrix(input_dim, self.units)
        self.bias = self._zeros_vector(self.units)

    # ---------------------------------------------------------------- forward
    def forward(self, x):
        self.last_input = x[:]
        if self.weights is None:
            self.build(len(x))

        z = [
            sum(x[i] * self.weights[i][j] for i in range(len(x))) + self.bias[j]
            for j in range(self.units)
        ]
        self.last_z = z[:]

        if self.activation_name and self.activation_name.lower() == "softmax":
            return self.activation.activate(z)

        return [self.activation.activate(v) for v in z]

    # ---------------------------------------------------------------- backward
    def backward(self, output_error, learning_rate, regularization_lambda=None):
        # ---- opción B: garantizar lista
        if not isinstance(output_error, list):
            output_error = [output_error]

        if regularization_lambda is None:
            regularization_lambda = self.regularization_lambda

        if self.activation_name and self.activation_name.lower() == "softmax":
            dL_dz = output_error[:]
        else:
            dL_dz = [
                output_error[j] * self.activation.derivative(self.last_z[j])
                for j in range(self.units)
            ]

        input_dim = len(self.last_input)
        grad_w = [
            [self.last_input[i] * dL_dz[j] for j in range(self.units)]
            for i in range(input_dim)
        ]
        grad_b = dL_dz[:]

        if regularization_lambda > 0:
            for i in range(input_dim):
                for j in range(self.units):
                    grad_w[i][j] += regularization_lambda * self.weights[i][j]

        for i in range(input_dim):
            for j in range(self.units):
                self.weights[i][j] -= learning_rate * grad_w[i][j]
        for j in range(self.units):
            self.bias[j] -= learning_rate * grad_b[j]

        # error para la capa anterior
        return [
            sum(self.weights[i][j] * dL_dz[j] for j in range(self.units))
            for i in range(input_dim)
        ]

    # ---------------------------------------------------------------- summary
    def summary(self):
        act = self.activation_name or "linear"
        reg = f"L2={self.regularization_lambda}" if self.regularization_lambda > 0 else "-"
        sd  = f", seed={self.seed}" if self.seed is not None else ""
        print(f"Dense(units={self.units}, act={act}, {reg}{sd})")
