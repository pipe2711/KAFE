# lib/KafeGESHA/Clustering.py

from lib.KafeGESHA.GeshaDeep import GeshaDeep

def clustering():
    """
    Crea y devuelve un modelo de clustering (no supervisado).
    Uso típico:
        from lib.KafeGESHA.Clustering import clustering
        model = clustering()
        model.add(Dense(...))
        ...
    """
    return GeshaDeep(model_type="clustering")
