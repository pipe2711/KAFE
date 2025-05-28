from TypeUtils import void_t
from errores import raiseFunctionCantReturnVoid, raiseTypeMismatch
from global_utils import esTipoCorrecto

class ReturnValue(Exception):
    def __init__(self, value):
        super().__init__()
        self.value = value

def check_value_type(value, declared_type):
    if declared_type == void_t:
        if value is not None:
            raiseFunctionCantReturnVoid()
        return

    if not esTipoCorrecto(value, declared_type):
        raiseTypeMismatch(value, declared_type)
