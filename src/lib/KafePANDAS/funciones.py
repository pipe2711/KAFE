# lib/KafePANDAS/funciones.py

import os
import math
from global_utils import check_sig
from errores import raiseTypeMismatch, raiseFunctionIncorrectArgumentType

class DataFrame:

    def __init__(self, columns, data):
        if not isinstance(columns, list) or not all(isinstance(c, str) for c in columns):
            raiseTypeMismatch(columns, "List[STR]")
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raiseTypeMismatch(data, "List[List]")
        for row in data:
            if len(row) != len(columns):
                raiseFunctionIncorrectArgumentType("DataFrame", row, ["dimensiones inconsistentes"])

        self.columns = columns
        self.data = data

    def __repr__(self):
        if len(self.columns) == 1:
            return repr([row[0] for row in self.data])
        contenido = [self.columns] + self.data
        return repr(contenido)

    def head(self, n=5):

        if not isinstance(n, int):
            raiseTypeMismatch(n, "INT")
        return DataFrame(self.columns, self.data[:n])

    def tail(self, n=5):

        if not isinstance(n, int):
            raiseTypeMismatch(n, "INT")
        if n <= len(self.data):
            return DataFrame(self.columns, self.data[-n:])
        else:
            return DataFrame(self.columns, self.data[:])

    def shape(self):

        n_filas = len(self.data)
        n_cols  = len(self.columns)
        cols = ["dimension", "value"]
        filas = [
            ["Rows",   n_filas],
            ["Columns", n_cols]
        ]
        return DataFrame(cols, filas)

    def col(self, column_name):

        if not isinstance(column_name, str):
            raiseTypeMismatch(column_name, "STR")
        if column_name not in self.columns:
            raise Exception(f"Columna '{column_name}' no existe")
        idx = self.columns.index(column_name)

        # Raw: lista con valores, incluidos nan
        raw = [row[idx] for row in self.data]

        # Obtener DataFrame de dtypes y su data (lista de [col, tipo])
        dtype_df = self.dtypes()      
        dtypes_rows = dtype_df.data   

        # Buscar tipo de la columna
        tipo_col = None
        for col, tipo in dtypes_rows:
            if col == column_name:
                tipo_col = tipo
                break

        # Crear filas normalizadas, cada fila es [valor]
        result_rows = []
        if tipo_col == "STR":
            for v in raw:
                if isinstance(v, float) and math.isnan(v):
                    result_rows.append([""])
                else:
                    result_rows.append([str(v)])

        elif tipo_col == "INT":
            for v in raw:
                result_rows.append([int(v)])

        elif tipo_col == "FLOAT":
            for v in raw:
                if isinstance(v, float) and math.isnan(v):
                    result_rows.append([float("nan")])
                else:
                    result_rows.append([float(v)])
        else:
            # Caso improbable, convertir todo a str
            for v in raw:
                result_rows.append([str(v)])

        return DataFrame([column_name], result_rows)

    def dtypes(self):

        filas = []
        for j, col_name in enumerate(self.columns):
            vals = [
                row[j]
                for row in self.data
                if not (isinstance(row[j], float) and math.isnan(row[j])) and row[j] is not None
            ]
            tipo_col = "STR"
            if len(vals) > 0 and all(isinstance(v, int) for v in vals):
                tipo_col = "INT"
            elif len(vals) > 0 and all(isinstance(v, (int, float)) for v in vals):
                tipo_col = "FLOAT"
            filas.append([col_name, tipo_col])

        return DataFrame(["column", "type"], filas)

    def info(self):

        n_filas = len(self.data)
        n_cols  = len(self.columns)

        cols_str = ",".join(self.columns)
        tipo_df = self.dtypes()       # DataFrame(["column","type"], ...)
        dtypes_rows = tipo_df.data    # [[col1,t1], [col2,t2], ...]
        dtypes_str = ",".join(f"{c}:{t}" for c, t in dtypes_rows)

        filas = [
            ["Rows",         n_filas],
            ["Columns",      n_cols],
            ["Column_Names", cols_str],
            ["Dtypes",       dtypes_str]
        ]
        return DataFrame(["key", "value"], filas)

    def describe(self):

        cols = ["column", "count", "mean", "std", "min", "max"]
        filas = []

        tipo_df = self.dtypes().data  
        for col_name, tipo in tipo_df:
            if tipo in ("INT", "FLOAT"):
                idx = self.columns.index(col_name)
                nums = [
                    row[idx]
                    for row in self.data
                    if isinstance(row[idx], (int, float)) and not (isinstance(row[idx], float) and math.isnan(row[idx]))
                ]
                if not nums:
                    continue
                count   = len(nums)
                mean    = sum(nums) / count
                var     = sum((x - mean) ** 2 for x in nums) / count
                std     = var ** 0.5
                min_val = min(nums)
                max_val = max(nums)
                filas.append([
                    col_name,
                    str(count),
                    str(mean),
                    str(std),
                    str(min_val),
                    str(max_val)
                ])

        return DataFrame(cols, filas)

def _inferir_tipo(celda):

    if celda == "":
        return float("nan")
    try:
        return int(celda)
    except ValueError:
        try:
            return float(celda)
        except ValueError:
            return celda

@check_sig([1], ["STR"])
def read_csv(path):

    import globals

    if os.path.isfile(path):
        real_path = path
    else:
        candidate = os.path.join(globals.current_dir, path)
        if os.path.isfile(candidate):
            real_path = candidate
        else:
            raise FileNotFoundError(f"Archivo '{path}' no encontrado")

    with open(real_path, encoding="utf-8") as f:
        lineas = [l.rstrip("\n") for l in f if l.strip() != ""]
    if len(lineas) == 0:
        return DataFrame([], [])

    # Detectar separador según la primera línea (encabezado)
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
        fila_convertida = [_inferir_tipo(c) for c in partes[: len(header)]]
        data.append(fila_convertida)

    return DataFrame(header, data)
