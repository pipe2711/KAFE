class BaseModel:
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

    def compile(self, optimizer, loss, metrics=[]):
        self.loss = get_loss(loss)
        self.loss_name = loss
        self.optimizer = get_optimizer(optimizer)
        self.metrics = metrics

    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

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
