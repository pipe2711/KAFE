import os
from errores import raiseFileNotFound
from global_utils import check_sig
from .utils import inferir_tipo
from .DataFrame import DataFrame
from TypeUtils import cadena_t

@check_sig([1], [cadena_t])
def read_csv(path):
    import globals

    if os.path.isfile(path):
        real_path = path
    else:
        candidate = os.path.join(globals.current_dir, path)
        if os.path.isfile(candidate):
            real_path = candidate
        else:
            raiseFileNotFound(path, globals.current_dir)

    with open(real_path, encoding="utf-8") as f:
        lineas = [l.rstrip("\n") for l in f if l.strip() != ""]
    if len(lineas) == 0:
        return DataFrame([], [])

    header_line = lineas[0]
    if ";" in header_line and header_line.count(";") >= header_line.count(","):
        delim = ";"
    else:
        delim = ","

    header = [h.strip() for h in header_line.split(delim)]
    data = []
    for fila in lineas[1:]:
        partes = [c.strip() for c in fila.split(delim)]
        if len(partes) < len(header):
            partes += [""] * (len(header) - len(partes))
        fila_convertida = [inferir_tipo(c) for c in partes[: len(header)]]
        data.append(fila_convertida)

    return DataFrame(header, data)
