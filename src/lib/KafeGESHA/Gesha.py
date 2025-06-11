from abc import ABC

class Gesha(ABC):
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_name = None
        self.optimizer = None
        self.metrics = []

    def add(self, layer):
        if self.layers and hasattr(layer, "input_shape") and not layer.input_shape:
            prev_output = self.layers[-1].units
            layer.input_shape = (prev_output,)
        self.layers.append(layer)

    def compile(self, optimizer=None, loss=None, metrics=[]):
        pass

    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def fit(self, x_train, y_train, epochs=1, batch_size=1):
        pass

    def summary(self):
        print("Model Summary:")
        for i, layer in enumerate(self.layers):
            print(f"Layer {i+1}: {layer.__class__.__name__}, "
                  f"Input: {getattr(layer, 'input_shape', None)}, "
                  f"Output: {getattr(layer, 'units', None)}")

    def evaluate(self, x_test, y_test):
        pass
