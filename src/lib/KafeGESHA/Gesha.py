from abc import ABC, abstractmethod
from losses import get_loss
from optimizers import get_optimizer

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

    @abstractmethod
    def compile(self, optimizer=None, loss=None, metrics=[]):
        self.loss = get_loss(loss)
        self.loss_name = loss
        self.optimizer = get_optimizer(optimizer)
        self.metrics = metrics

    @abstractmethod
    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    @abstractmethod
    def fit(self, x_train, y_train, epochs=1, batch_size=1):
        for epoch in range(epochs):
            total_loss = 0
            for x, y in zip(x_train, y_train):
                output = x
                for layer in self.layers:
                    output = layer.forward(output)

                total_loss += self.loss.compute([y], [output])
                error = self.loss.derivative([y], [output])[0]

                for layer in reversed(self.layers):
                    error = layer.backward(error, learning_rate=self.optimizer.lr)

            print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss / len(x_train)}")

    @abstractmethod
    def summary(self):
        print("Model Summary:")
        for i, layer in enumerate(self.layers):
            print(f"Layer {i+1}: {layer.__class__.__name__}, Input: {getattr(layer, 'input_shape', None)}, Output: {getattr(layer, 'units', None)}")

    @abstractmethod
    def evaluate(self, x_test, y_test):
        correct = 0
        total = len(x_test)

        for x, y in zip(x_test, y_test):
            output = self.predict(x)
            pred = output.index(max(output)) if isinstance(output, list) else round(output)
            true = y.index(max(y)) if isinstance(y, list) else y

            if pred == true:
                correct += 1

        accuracy = correct / total
        print(f"Accuracy: {accuracy * 100:.2f}%")
        return accuracy
