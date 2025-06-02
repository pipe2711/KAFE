# lib/KafeGESHA/GeshaDeep.py

import warnings
import math
import random
from lib.KafeGESHA.Gesha import Gesha
from lib.KafeGESHA.LossFunction import (
    MeanSquaredError, MeanAbsoluteError,
    BinaryCrossEntropy, CategoricalCrossEntropy
)
from lib.KafeGESHA.Optimizer import SGD, RMSprop, Adam, AdamW
from lib.KafeGESHA.utils import check_regularization


class GeshaDeep(Gesha):
    def __init__(self, model_type="classification", global_regularization=0.0):
        super().__init__()
        if model_type not in ("classification", "clustering", "regression"):
            raise ValueError(
                f"model_type debe ser 'classification', 'clustering' o 'regression'. Se recibió: {model_type}"
            )
        self.model_type = model_type
        self.global_regularization = check_regularization(global_regularization)

        self._loss_fn = None
        self.loss_name = None
        self._optimizer_obj = None
        self.metrics = []

        # Para clustering “soft k-means”
        self._centroids = None

    def compile(self, optimizer="sgd", loss=None, metrics=None):
        if loss is None:
            if self.model_type == "classification":
                loss_name = "categorical_crossentropy"
            else:
                loss_name = "mse"
        else:
            loss_name = loss

        loss_map = {
            "mse": MeanSquaredError(),
            "mean_squared_error": MeanSquaredError(),
            "mae": MeanAbsoluteError(),
            "mean_absolute_error": MeanAbsoluteError(),
            "binary_crossentropy": BinaryCrossEntropy(),
            "categorical_crossentropy": CategoricalCrossEntropy()
        }
        key = loss_name.lower()
        if key not in loss_map:
            raise ValueError(
                f"Función de pérdida '{loss_name}' no reconocida. Usa uno de {list(loss_map.keys())}."
            )
        self._loss_fn = loss_map[key]
        self.loss_name = key

        optimizer_map = {
            "sgd": SGD(),
            "rmsprop": RMSprop(),
            "adam": Adam(),
            "adamw": AdamW()
        }
        if optimizer is None:
            self._optimizer_obj = SGD()
        else:
            opt_key = optimizer.lower()
            if opt_key not in optimizer_map:
                raise ValueError(
                    f"Optimizador '{optimizer}' no válido. Usa uno de {list(optimizer_map.keys())}."
                )
            self._optimizer_obj = optimizer_map[opt_key]

        self.metrics = metrics if metrics else []

        if self.model_type == "clustering":
            warnings.warn(
                "Advertencia: un modelo de clustering con menos de 2 capas puede no tener suficiente capacidad.",
                stacklevel=2
            )

    def predict(self, x):
        out = x
        for layer in self.layers:
            out = layer.forward(out)
        return out

    def fit(self, x_train, y_train=None, epochs=1, batch_size=1, x_val=None, y_val=None):
        """
        Entrena el modelo.
        - classification/regression: necesita y_train para cálculo de pérdida y backprop.
        - clustering: ignora y_train y utiliza “soft k-means” para actualizar pesos.
        """

        # Validaciones iniciales
        if self.model_type in ("classification", "regression"):
            if y_train is None:
                raise ValueError(f"Para modelo {self.model_type} debes pasar x_train e y_train.")
            if len(x_train) != len(y_train):
                raise ValueError("x_train e y_train deben tener la misma longitud.")
        else:  # clustering
            if y_train is not None:
                warnings.warn("Modelo de clustering: y_train será ignorado.", stacklevel=2)

        if (x_val is None) ^ (y_val is None):
            raise ValueError("Si vas a pasar validación, debes pasar tanto x_val como y_val.")

        n_samples = len(x_train)

        for epoch in range(epochs):
            total_loss = 0.0
            count = 0

            for start in range(0, n_samples, batch_size):
                end = min(start + batch_size, n_samples)
                x_batch = x_train[start:end]
                B = len(x_batch)
                if B == 0:
                    continue

                if self.model_type == "clustering":
                    # → SOFT K-MEANS NO SUPERVISADO ←

                    # 1) Inicializar centroides la primera vez
                    if self._centroids is None:
                        # Tomamos la primera muestra para inferir dimensión de h(x)
                        dummy = x_batch[0]
                        h_dummy = dummy
                        for layer in self.layers[:-1]:
                            h_dummy = layer.forward(h_dummy)
                        dim_h = len(h_dummy)

                        # Inicializar 2 centroides aleatorios de dimensión dim_h
                        self._centroids = [
                            [random.random() for _ in range(dim_h)] for _ in range(2)
                        ]

                    # 2) Forward pass: obtener H = [h(x_i)] y P = [p_i = softmax(z_i)]
                    H = []
                    P = []
                    for x in x_batch:
                        # Pasar hasta penúltima capa para obtener h
                        h = x
                        for layer in self.layers[:-1]:
                            h = layer.forward(h)
                        H.append(h)

                        # Capa final: Softmax
                        out = h
                        out = self.layers[-1].forward(out)
                        if not isinstance(out, list):
                            out = [out]
                        P.append(out)

                    # 3) Recalcular centroides “suaves”
                    K = 2
                    numerators = [[0.0] * len(H[0]) for _ in range(K)]
                    denominators = [0.0] * K
                    for i in range(B):
                        for k in range(K):
                            pk = P[i][k]
                            denominators[k] += pk
                            for d in range(len(H[i])):
                                numerators[k][d] += pk * H[i][d]
                    for k in range(K):
                        if denominators[k] > 0:
                            for d in range(len(self._centroids[k])):
                                self._centroids[k][d] = numerators[k][d] / denominators[k]

                    # 4) Calcular pérdida “soft k-means”
                    loss_batch = 0.0
                    for i in range(B):
                        for k in range(K):
                            sq = 0.0
                            for d in range(len(H[i])):
                                diff = H[i][d] - self._centroids[k][d]
                                sq += diff * diff
                            loss_batch += P[i][k] * sq
                    loss_batch /= B
                    total_loss += loss_batch
                    count += 1

                    # 5) Gradiente ∂L/∂H[i]
                    dLdH = []
                    for i in range(B):
                        grad_h = [0.0] * len(H[i])
                        for k in range(K):
                            coeff = 2.0 * P[i][k]
                            for d in range(len(H[i])):
                                grad_h[d] += coeff * (H[i][d] - self._centroids[k][d])
                        # Normalizar por B
                        dLdH.append([gh / B for gh in grad_h])

                    # 6) Backprop en capas ocultas (sin tocar última capa Softmax)
                    for i_in_batch, x in enumerate(x_batch):
                        error = dLdH[i_in_batch]
                        for layer in reversed(self.layers[:-1]):
                            reg_lambda = getattr(layer, "regularization_lambda", self.global_regularization)
                            error = layer.backward(
                                error,
                                learning_rate=self._optimizer_obj.lr,
                                regularization_lambda=reg_lambda
                            )

                else:
                    # → SUPERVISADO: CLASSIFICATION O REGRESSION ←
                    for idx in range(len(x_batch)):
                        x = x_batch[idx]
                        y = y_train[start + idx]

                        # Forward completo
                        output = x
                        for layer in self.layers:
                            output = layer.forward(output)
                        if not isinstance(output, list):
                            output = [output]

                        if self.model_type == "classification":
                            # Etiqueta a one-hot si es int
                            if isinstance(y, int):
                                y_onehot = [0.0] * len(output)
                                if 0 <= y < len(output):
                                    y_onehot[y] = 1.0
                                else:
                                    raise ValueError(
                                        f"Etiqueta {y} fuera de rango [0, {len(output)-1}]."
                                    )
                            elif isinstance(y, list):
                                y_onehot = y
                            else:
                                raise ValueError(
                                    f"En clasificación, y debe ser INT o LIST. Se recibió: {type(y)}"
                                )
                            y_vec = y_onehot

                            # Pérdida y gradiente
                            loss_val = self._loss_fn.compute([y_vec], [output])
                            total_loss += loss_val
                            count += 1

                            grad_list = self._loss_fn.derivative([y_vec], [output])
                            grad = grad_list[0]

                            # Backprop
                            error = grad
                            for layer in reversed(self.layers):
                                reg_lambda = getattr(layer, "regularization_lambda", self.global_regularization)
                                error = layer.backward(
                                    error,
                                    learning_rate=self._optimizer_obj.lr,
                                    regularization_lambda=reg_lambda
                                )

                        else:
                            # → REGRESSION ←
                            if isinstance(y, (int, float)):
                                y_scalar = float(y)
                            elif isinstance(y, list):
                                y_scalar = float(y[0])
                            else:
                                raise ValueError(
                                    f"En regresión, y debe ser numérico o lista. Se recibió: {type(y)}"
                                )

                            out_scalar = output[0]
                            loss_val = self._loss_fn.compute([y_scalar], [out_scalar])
                            total_loss += loss_val
                            count += 1

                            deriv_list = self._loss_fn.derivative([y_scalar], [out_scalar])
                            grad = deriv_list[0]

                            error = [grad]
                            for layer in reversed(self.layers):
                                reg_lambda = getattr(layer, "regularization_lambda", self.global_regularization)
                                error = layer.backward(
                                    error,
                                    learning_rate=self._optimizer_obj.lr,
                                    regularization_lambda=reg_lambda
                                )

            # Fin de cada epoch: imprimir pérdida promedio
            if self.model_type in ("classification", "regression"):
                avg_loss = total_loss / count if count > 0 else 0.0
                print(f"Epoch {epoch+1}/{epochs} — Loss promedio: {avg_loss:.6f}")
            else:
                avg_loss = total_loss / count if count > 0 else 0.0
                print(f"Epoch {epoch+1}/{epochs} — Loss (soft k-means): {avg_loss:.6f}")

    def summary(self):
        print(f"*** Resumen del modelo (tipo: {self.model_type}) ***")
        for i, layer in enumerate(self.layers):
            print(f" Capa {i+1}: {layer.__class__.__name__}", end=" — ")
            if hasattr(layer, "summary"):
                layer.summary()
            else:
                print(f"unidades={getattr(layer, 'units', None)}")

    def evaluate(self, x_test, y_test=None):
        if self.model_type == "classification":
            if y_test is None:
                raise ValueError("Para clasificación debes pasar x_test e y_test.")
            correct = 0
            total = len(x_test)
            for x, y in zip(x_test, y_test):
                out = self.predict(x)
                if not isinstance(out, list):
                    out = [out]
                pred = out.index(max(out))
                true = y if isinstance(y, int) else y.index(max(y))
                if pred == true:
                    correct += 1
            accuracy = correct / total
            print(f"Accuracy: {accuracy*100:.2f}%")
            return accuracy

        elif self.model_type == "regression":
            if y_test is None:
                raise ValueError("Para regresión debes pasar x_test e y_test.")
            mse_total = 0.0
            n = len(x_test)
            for x, y in zip(x_test, y_test):
                pred = self.predict(x)
                if not isinstance(pred, list):
                    pred = [pred]
                true_val = y if not isinstance(y, list) else y[0]
                mse_total += (pred[0] - true_val) ** 2
            mse = mse_total / n
            print(f"MSE: {mse:.6f}")
            return mse

        else:  # clustering
            warnings.warn("evaluate() no está implementado para clustering.", stacklevel=2)
            return None
