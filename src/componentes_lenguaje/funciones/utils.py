from componentes_lenguaje.global_utils import verificar_tipo

class ReturnValue(Exception):
    def __init__(self, value):
        super().__init__()
        self.value = value

def check_value_type(self, value, declared_type):
    if declared_type == "VOID":
        if value is not None:
            raise TypeError("Function declared VOID must not return a value")
        return

    tipo_valor = self.obtener_tipo_dato(value)
    verificar_tipo(declared_type, tipo_valor)
