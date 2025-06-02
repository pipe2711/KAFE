# lib/KafeGESHA/Classification.py

from lib.KafeGESHA.GeshaDeep import GeshaDeep

def categorical():
    """
    Crea y devuelve un modelo de clasificación (categorical) listo para agregar capas.
    Uso típico:
        from lib.KafeGESHA.Classification import categorical
        model = categorical()
        model.add(Dense(...))
        ...
    """
    return GeshaDeep(model_type="classification")
