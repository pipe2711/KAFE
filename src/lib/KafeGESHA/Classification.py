# lib/KafeGESHA/Classification.py

from lib.KafeGESHA.GeshaDeep import GeshaDeep

def categorical():
    return GeshaDeep(model_type="classification")
