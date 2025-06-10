import subprocess
import pytest
import os
from utils import obtener_parametros, get_programs, get_invalid_programs

@pytest.mark.parametrize("programa, entrada, salida_esperada", list(obtener_parametros(get_programs("../tests/KafePLOT"))))
def test_valid_programs(programa, entrada, salida_esperada):
    result = subprocess.run(["python", "Kafe.py", programa],
                            capture_output=True, text=True, input=entrada)

    carpeta_destino = os.path.dirname(programa)
    nombre_base = os.path.splitext(os.path.basename(programa))[0]
    svg_prueba_base = f"grafico_{nombre_base}.svg"
    svg_generado_base = f"{nombre_base}.svg"
    svg_generado_path = os.path.join(carpeta_destino, svg_generado_base)
    svg_prueba_path = os.path.join(carpeta_destino, svg_prueba_base)

    with open(svg_generado_path) as f:
        svg_generado = f.read()

    with open(svg_prueba_path) as f:
        svg_prueba = f.read()

    os.remove(svg_generado_path)

    assert result.returncode == 0, f"Non-zero exit for {programa}"
    assert svg_generado == svg_prueba, f"{svg_prueba_path} doesn't match {svg_generado_path}"


@pytest.mark.parametrize("programa, entrada, salida_esperada", list(obtener_parametros(get_invalid_programs("../tests/KafePLOT"))))
def test_invalid_programs(programa, entrada, salida_esperada):
    result = subprocess.run(["python", "Kafe.py", programa],
                            capture_output=True, text=True, input=entrada)

    assert result.returncode == 1, f"Zero exit for {programa}"
    assert result.stderr.splitlines()[-1] + '\n' == salida_esperada, f"Incorrect output for {programa}"
