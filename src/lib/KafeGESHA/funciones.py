from TypeUtils import cadena_t
from global_utils import check_sig

@check_sig([1], [cadena_t])
def hola(texto):
    return(texto + "alksjdfklasd")
