from lib.KafeGESHA.GeshaDeep import GeshaDeep
from lib.KafeGESHA.Dense import Dense

def create_dense(units, activation, input_shape, regularization_lambda, seed=None):
    """
    Crea una capa Dense reproducible.
      · seed: int o None (por defecto) para control de aleatoriedad.
    """
    return Dense(
        units,
        activation,
        input_shape,
        regularization_lambda,
        seed=seed,
    )

def classification():
    return GeshaDeep(model_type="classification")

def clustering():
    return GeshaDeep(model_type="clustering")


def regression():
    return GeshaDeep(model_type="regression")

def binary():
    return GeshaDeep(model_type="binary")

def categorical():
    return classification()

def compile(model, optimizer, loss, metrics):
    if getattr(model, "_model_type", None) == "clustering" and len(model.layers) < 2:
        model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
    else:
        model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

def set_lr(model, new_lr):
    model.set_lr(new_lr)
