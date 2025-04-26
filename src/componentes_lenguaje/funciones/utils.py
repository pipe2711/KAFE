from ..global_utils import obtener_tipo_lista, verificarHomogeneidad

class ReturnValue(Exception):
    def __init__(self, value):
        super().__init__()
        self.value = value

def _check_value_type(self, value, declared_type):
    if declared_type == "VOID":
        if value is not None:
            raise TypeError("Function declared VOID must not return a value")
        return
    if declared_type in self.type_mapping:
        if not isinstance(value, self.type_mapping[declared_type]):
            raise TypeError(f"Expected {declared_type}, obtained {type(value).__name__.upper()}")
        return
    if declared_type.startswith("List"):
        if not isinstance(value, list):
            raise TypeError(f"Expected {declared_type}, obtained {type(value).__name__}")
        if value:
            tipo_valor = obtener_tipo_lista(value, self.nombre_tipos)
            if tipo_valor != declared_type:
                raise TypeError(f"Expected {declared_type}, obtained {tipo_valor}")
            if not verificarHomogeneidad(value):
                raise TypeError("Expected homogeneous list")
        return
    if declared_type.startswith("FUNC"):
        if not callable(value):
            raise TypeError(f"Expected function, got {type(value).__name__}")
        return
    raise TypeError(f"Unknown type '{declared_type}'")
