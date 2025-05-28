import subprocess
import pytest
from utils import obtener_parametros, get_programs

@pytest.mark.parametrize("programa, entrada, salida_esperada", list(obtener_parametros(get_programs("../tests/Algorithms"))))
def test_valid_programs(programa, entrada, salida_esperada):
    result = subprocess.run(["python", "Kafe.py", programa],
                            capture_output=True, text=True, input=entrada)

    assert result.returncode == 0, f"Non-zero exit for {programa}"
    assert result.stdout == salida_esperada, f"Incorrect output for {programa}"
