from abc import ABC
from global_utils import check_sig
from TypeUtils import (
    gesha_t, vector_numeros_t, matriz_numeros_t, 
    entero_t, cadena_t, lista_cadenas_t, void_t
)

class Gesha(ABC):
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_name = None
        self.optimizer = None
        self.metrics = []

    @check_sig([2], [gesha_t], is_method=True)
    def add(self, layer):
        if self.layers and hasattr(layer, "input_shape") and not layer.input_shape:
            prev_output = self.layers[-1].units
            layer.input_shape = (prev_output,)
        self.layers.append(layer)

    @check_sig([1, 2, 3, 4], [cadena_t, void_t], [cadena_t, void_t], [lista_cadenas_t, void_t], is_method=True)
    def compile(self, optimizer=None, loss=None, metrics=[]):
        pass

    @check_sig([2], vector_numeros_t, is_method=True)
    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    @check_sig([3, 4, 5], matriz_numeros_t, matriz_numeros_t + vector_numeros_t, [entero_t], [entero_t], is_method=True)
    def fit(self, x_train, y_train, epochs=1, batch_size=1):
        pass

    def summary(self):
        print("Model Summary:")
        for i, layer in enumerate(self.layers):
            print(f"Layer {i+1}: {layer.__class__.__name__}, "
                  f"Input: {getattr(layer, 'input_shape', None)}, "
                  f"Output: {getattr(layer, 'units', None)}")

    @check_sig([3], matriz_numeros_t, matriz_numeros_t + vector_numeros_t, is_method=True)
    def evaluate(self, x_test, y_test):
        pass
