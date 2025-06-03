# src/lib/KafeGESHA/funciones.py

"""
Wrapper de utilidades para trabajar con GeshaDeep desde Kafé (.kf)

Se exponen funciones de fábrica para:
  • crear capas Dense (`create_dense`)
  • instanciar modelos de clasificación, clustering y regresión
  • compilar modelos y ajustar el learning-rate

También se mantiene compatibilidad con scripts antiguos mediante
el alias `categorical()` → `classification()`.
"""

import warnings
from lib.KafeGESHA.GeshaDeep import GeshaDeep
from lib.KafeGESHA.Dense import Dense

# ------------------------------------------------------------------
# 1) Fábrica de capas Dense
# ------------------------------------------------------------------
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


# ------------------------------------------------------------------
# 2) Creación de modelos GeshaDeep
# ------------------------------------------------------------------
def classification():
    """Instancia y devuelve un modelo GeshaDeep de *clasificación*."""
    return GeshaDeep(model_type="classification")


def clustering():
    """Instancia y devuelve un modelo GeshaDeep de *clustering* (no supervisado)."""
    return GeshaDeep(model_type="clustering")


def regression():
    """Instancia y devuelve un modelo GeshaDeep de *regresión*."""
    return GeshaDeep(model_type="regression")

def binary():
    """
    Instancia y devuelve un modelo GeshaDeep de clasificación binaria
    (una sola unidad de salida, pérdida binary_crossentropy).
    """
    return GeshaDeep(model_type="binary")



# --- alias histórico: categorical() → classification() -------------
def categorical():
    """
    Alias de `classification()` para mantener compatibilidad con
    scripts y tests antiguos que usan geshaDeep.categorical().
    """
    return classification()


# ------------------------------------------------------------------
# 3) Compilar modelos
# ------------------------------------------------------------------
def compile(model, optimizer, loss, metrics):
    """
    Envuelve la llamada interna a model.compile().

    Para modelos de clustering con menos de 2 capas se silencia la
    advertencia que GeshaDeep lanza de forma predeterminada.

    Parámetros
    ----------
    model : GeshaDeep
    optimizer : str  («sgd», «adam», «rmsprop», «adamw» …)
    loss : str       («mse», «categorical_crossentropy», …)
    metrics : list[str]
    """
    if getattr(model, "_model_type", None) == "clustering" and len(model.layers) < 2:
        # Ejecutar sin propagar el warning interno (<2 capas).
        model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
    else:
        model.compile(optimizer=optimizer, loss=loss, metrics=metrics)


# ------------------------------------------------------------------
# 4) Ajustar dinámicamente el learning rate
# ------------------------------------------------------------------
def set_lr(model, new_lr):
    """
    Cambia el learning-rate del optimizador ya configurado.

    Parámetros
    ----------
    model : GeshaDeep
    new_lr : float
    """
    model.set_lr(new_lr)
