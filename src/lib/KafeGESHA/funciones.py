from global_utils import check_sig
from TypeUtils import numeros_t, cadena_t, lista_t, flotante_t
import lib.KafeGESHA.utils as activar
from lib.KafeNUMK.funciones import dot,dot_matrix,zeros,zeros_matrix,shape

modelo_actual = {}

@check_sig([4],cadena_t, lista_t, flotante_t, cadena_t)
def perceptron_binary(tipo,entradas, bias, activacion ):
    '''import geshaDeep;

   model = geshaDeep.perceptron(type="and",x1= 1,, x2 = 0 , activacion = "sigmoide");

    geshadeep.fit(model);

    geshaDeep.evaluate(perceptron);'''

    if tipo == "AND":
        datos_entrenamiento = [
            (0, 0, 0),
            (0, 1, 0),
            (1, 0, 0),
            (1, 1, 1)
        ]
    elif tipo == "OR":
        datos_entrenamiento = [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 1)
        ]
    elif tipo == "XOR":
        datos_entrenamiento = [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 0)
        ]
    elif tipo == "NOT":
        datos_entrenamiento = [
            (0, 0, 1),
            (1, 0, 0)
        ]
    else:
        raise ValueError("Tipo no soportado")

    modelo_actual['tipo'] = tipo
    modelo_actual['bias'] = bias
    modelo_actual['activacion'] = activar(activacion)
    modelo_actual['datos'] = datos_entrenamiento
    modelo_actual['historial'] = []

    print(f"Perceptrón binario creado con pesos={pesos}, bias={bias}, activacion={activacion}, tipo={tipo}")


