import subprocess
import pytest
import os
from utils import obtener_parametros, get_programs, get_invalid_programs

@pytest.mark.parametrize("programa, entrada, salida_esperada", list(obtener_parametros(get_programs("../tests/KafeFiles"))))
def test_valid_programs(programa, entrada, salida_esperada):
    result = subprocess.run(["python", "Kafe.py", programa],
                            capture_output=True, text=True, input=entrada)

    carpeta_destino = os.path.dirname(programa)
    nombre_base = os.path.splitext(os.path.basename(programa))[0]
    txt_generado_base = f"archivo_{nombre_base}.txt"
    txt_prueba_base = f"{nombre_base}.txt"
    txt_generado_path = os.path.join(carpeta_destino, txt_generado_base)
    txt_prueba_path = os.path.join(carpeta_destino, txt_prueba_base)

    try:
        with open(txt_generado_path) as f:
            txt_generado = f.read()
            os.remove(txt_generado_path)
    except FileNotFoundError:
        txt_generado = ""

    try:
        with open(txt_prueba_path) as f:
            txt_prueba = f.read()
    except FileNotFoundError:
        txt_prueba = ""


    assert txt_generado == txt_prueba, f"{txt_prueba_path} doesn't match {txt_generado_path}"
    assert result.returncode == 0, f"Non-zero exit for {programa}"
    assert result.stdout == salida_esperada, f"Incorrect output for {programa}"


@pytest.mark.parametrize("programa, entrada, salida_esperada", list(obtener_parametros(get_invalid_programs("../tests/KafeFiles"))))
def test_invalid_programs(programa, entrada, salida_esperada):
    result = subprocess.run(["python", "Kafe.py", programa],
                            capture_output=True, text=True, input=entrada)

    assert result.returncode == 1, f"Zero exit for {programa}"
    assert result.stderr.splitlines()[-1] + '\n' == salida_esperada, f"Incorrect output for {programa}"
