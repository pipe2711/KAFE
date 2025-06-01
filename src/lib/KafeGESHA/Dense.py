 
#from lib.KafeGESHA.Gesha import Gesha
#from lib.Kafe.activations import get_activation
#from lib.KafeMATH.funciones import dot

class Dense(Gesha):
    def __init__(self, units, activation=None, input_shape=None):
        super().__init__()
        self.units = units
        self.activation_name = activation
        self.activation = get_activation(activation)
        self.input_shape = input_shape
        self.weights = None
        self.bias = None
        self.last_input = None

    def build(self, input_dim):
        from lib.KafeNUMK.funciones import random_matrix, zeros
        self.weights = random_matrix(input_dim, self.units)
        self.bias = zeros(self.units)

    def forward(self, x):
        self.last_input = x
        if self.weights is None:
            self.build(len(x))
        z = [sum([x[i] * self.weights[i][j] for i in range(len(x))]) + self.bias[j] for j in range(self.units)]
        return [self.activation(val) for val in z]