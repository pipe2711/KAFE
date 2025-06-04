# src/lib/KafeGESHA/GeshaDeep.py
# ------------------------------------------------------------
#  GeshaDeep  – ajuste: gradiente seguro para BCE y otras pérdidas
# ------------------------------------------------------------
import warnings
from lib.KafeGESHA.Gesha import Gesha
from lib.KafeGESHA.LossFunction import (
    MeanSquaredError, MeanAbsoluteError,
    BinaryCrossEntropy, CategoricalCrossEntropy,
    SparseCategoricalCrossEntropy,
)
from lib.KafeGESHA.Optimizer import SGD, RMSprop, Adam, AdamW
from lib.KafeMATH.funciones import log


class GeshaDeep(Gesha):
    # ----------------------------------------------------- 0) ctor
    def __init__(self, model_type: str = "classification"):
        super().__init__()
        self._model_type = model_type
        self._loss_fn = None
        self._optimizer_obj = None
        self._metrics = []

    # ----------------------------------------------------- 1) add
    def add(self, layer):
        if self.layers and hasattr(layer, "input_shape") and not layer.input_shape:
            layer.input_shape = (self.layers[-1].units,)
        self.layers.append(layer)

    # ----------------------------------------------------- 2) compile
    def compile(self, optimizer=None, loss=None, metrics=None):
        if loss == "mse":
            self._loss_fn = MeanSquaredError()
        elif loss == "mae":
            self._loss_fn = MeanAbsoluteError()
        elif loss == "binary_crossentropy":
            self._loss_fn = BinaryCrossEntropy()
        elif loss == "categorical_crossentropy":
            self._loss_fn = CategoricalCrossEntropy()
        elif loss == "sparse_categorical_crossentropy":
            self._loss_fn = SparseCategoricalCrossEntropy()
        else:
            raise ValueError(f"Loss '{loss}' no reconocido.")

        if optimizer == "sgd":
            self._optimizer_obj = SGD(lr=0.01)
        elif optimizer == "rmsprop":
            self._optimizer_obj = RMSprop(lr=0.001)
        elif optimizer == "adam":
            self._optimizer_obj = Adam(lr=0.001)
        elif optimizer == "adamw":
            self._optimizer_obj = AdamW(lr=0.001)
        else:
            raise ValueError(f"Optimizer '{optimizer}' no reconocido.")

        self._metrics = metrics or []
        if self._model_type == "clustering" and len(self.layers) < 2:
            warnings.warn(
                "Advertencia: un modelo de clustering con menos de 2 capas puede no tener suficiente capacidad."
            )

    # ----------------------------------------------------- 3) set_lr
    def set_lr(self, new_lr: float):
        if not self._optimizer_obj:
            raise AttributeError("compile() debe llamarse antes de set_lr().")
        self._optimizer_obj.lr = new_lr

    # ----------------------------------------------------- 4) predict “crudo”
    def predict(self, x):
        out = x
        for layer in self.layers:
            out = layer.forward(out)
        return out

    # ----------------------------------------------------- 5) fit
    def fit(self, x_train, y_train=None, epochs=1, batch_size=1, x_val=None, y_val=None):
        n_samples = len(x_train)
        has_val = x_val is not None and y_val is not None and len(x_val) > 0

        def _forward(xi):
            out = xi
            for layer in self.layers:
                out = layer.forward(out)
            return out

        def _backward(err):
            # asegura lista de errores para capas Dense
            if not isinstance(err, list):
                err = [err]
            for layer in reversed(self.layers):
                err = layer.backward(err, learning_rate=self._optimizer_obj.lr)

        # ---------- clustering ----------
        alpha = 0.5

        for epoch in range(1, epochs + 1):
            total = 0.0
            for i in range(0, n_samples, batch_size):
                for xi in x_train[i : min(i + batch_size, n_samples)]:
                    # 1) Forward
                    z = _forward(xi)             # z = [z0, z1]
                    k_hat = z.index(max(z))      # argmax actual

                    total += -log(z[k_hat] + 1e-8)

                    # 2) Target suave: [0.7, 0.3] o [0.3, 0.7]
                    k = len(z)   # aquí k = 2
                    target = [ (1.0 - alpha) / (k - 1) ] * k  # → [0.3, 0.3] inicial
                    target[k_hat] = alpha                   # → [0.7, 0.3] si k_hat=0, o [0.3, 0.7] si k_hat=1

                    # 3) Gradiente: z - target
                    delta = [ z[j] - target[j] for j in range(k) ]
                    _backward(delta)

            print(f"Epoch {epoch}/{epochs} — Loss (soft k-means): {total / n_samples:.6f}")
        return
        # ---------- clasificación múlticlase / binaria con abordagem “categorical” ----------
        if self._model_type == "classification":
            for epoch in range(1, epochs + 1):
                total = 0.0
                for i in range(0, n_samples, batch_size):
                    bx = x_train[i:min(i + batch_size, n_samples)]
                    by = y_train[i:min(i + batch_size, n_samples)]
                    for xi, yi in zip(bx, by):
                        out = _forward(xi)
                        total += self._loss_fn.compute([yi], [out])
                        dg = self._loss_fn.derivative([yi], [out])  # lista de grads por sample
                        grad_out = dg[0] if isinstance(dg[0], list) else dg  # lista para Dense
                        _backward(grad_out)
                msg = f"Epoch {epoch}/{epochs} — Loss {total / n_samples:.6f}"
                if has_val:
                    correct = sum(
                        1 for xv, yv in zip(x_val, y_val)
                        if _forward(xv).index(max(_forward(xv))) ==
                           (yv.index(max(yv)) if isinstance(yv, list) else yv)
                    )
                    msg += f" — val_accuracy {correct/len(x_val):.4f}"
                print(msg)
            return

        # ---------- binaria ----------
        if self._model_type == "binary":
            for epoch in range(1, epochs + 1):
                total = 0.0
                for i in range(0, n_samples, batch_size):
                    bx = x_train[i:min(i + batch_size, n_samples)]
                    by = y_train[i:min(i + batch_size, n_samples)]
                    for xi, yi in zip(bx, by):
                        p = _forward(xi)[0]
                        total += self._loss_fn.compute([yi], [p])
                        grad = self._loss_fn.derivative([yi], [p])  # lista [grad]
                        _backward(grad)
                msg = f"Epoch {epoch}/{epochs} — Loss {total / n_samples:.6f}"
                if has_val:
                    correct = sum(
                        1 for xv, yv in zip(x_val, y_val)
                        if (1 if _forward(xv)[0] >= 0.5 else 0) == yv
                    )
                    msg += f" — val_accuracy {correct/len(x_val):.4f}"
                print(msg)
            return

        # ---------- regresión ----------
        if self._model_type == "regression":
            for epoch in range(1, epochs + 1):
                total = 0.0
                for i in range(0, n_samples, batch_size):
                    bx = x_train[i:min(i + batch_size, n_samples)]
                    by = y_train[i:min(i + batch_size, n_samples)]
                    for xi, yi in zip(bx, by):
                        p = _forward(xi)[0]
                        total += self._loss_fn.compute([yi], [p])
                        grad = self._loss_fn.derivative([yi], [p])  # lista [grad]
                        _backward(grad)
                msg = f"Epoch {epoch}/{epochs} — Loss {total / n_samples:.6f}"
                if has_val:
                    val_loss = sum(
                        self._loss_fn.compute([yv], [_forward(xv)[0]])
                        for xv, yv in zip(x_val, y_val)
                    )
                    msg += f" — val_mse {val_loss/len(x_val):.6f}"
                print(msg)
            return

        raise ValueError("Tipo de modelo no soportado en fit().")

    # ----------------------------------------------------- 6) summary
    def summary(self):
        print(f"*** Resumen (tipo: {self._model_type}) ***")
        for i, layer in enumerate(self.layers, 1):
            act = layer.activation_name or "linear"
            reg = (
                f"L2={layer.regularization_lambda}"
                if hasattr(layer, "regularization_lambda")
                else "sin regularización"
            )
            print(f" Capa {i}: Dense(units={layer.units}, activation={act}, {reg})")

    # ----------------------------------------------------- 7) evaluate
    def evaluate(self, x_test, y_test):
        if self._model_type == "clustering":
            avg = sum(
                -log(self.predict(xi)[self.predict(xi).index(max(self.predict(xi)))] + 1e-8)
                for xi in x_test
            ) / len(x_test)
            print(f"Soft k-means loss (eval): {avg:.6f}")
            return avg

        if self._model_type == "binary":
            acc = sum(
                1 for xi, yi in zip(x_test, y_test)
                if (1 if self.predict(xi)[0] >= 0.5 else 0) == yi
            ) / len(x_test)
            print(f"Accuracy: {acc*100:.2f}%")
            return acc

        if self._model_type == "classification":
            acc = sum(
                1 for xi, yi in zip(x_test, y_test)
                if self.predict(xi).index(max(self.predict(xi))) ==
                   (yi.index(max(yi)) if isinstance(yi, list) else yi)
            ) / len(x_test)
            print(f"Accuracy: {acc*100:.2f}%")
            return acc

        if self._model_type == "regression":
            mse = sum(
                self._loss_fn.compute([yi], [self.predict(xi)[0]])
                for xi, yi in zip(x_test, y_test)
            ) / len(x_test)
            print(f"MSE promedio: {mse:.6f}")
            return mse

        raise ValueError("Tipo de modelo no soportado en evaluate().")

    # ----------------------------------------------------- 8) utilidades de predicción
    def predict_proba(self, x):
        out = self.predict(x)
        if self._model_type in ("binary", "regression"):
            return out[0] if isinstance(out, list) else out
        return out

    def predict_label(self, x):
        if self._model_type == "regression":
            raise ValueError("predict_label() no aplica a modelos de regresión.")
        if self._model_type == "binary":
            return 1 if self.predict_proba(x) >= 0.5 else 0
        return self.predict_proba(x).index(max(self.predict_proba(x)))
