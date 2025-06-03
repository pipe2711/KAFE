import lib.KafeMATH.funciones as math
from global_utils import check_sig
from TypeUtils import pandas_t, lista_cadenas_t, matriz_cualquiera_t, entero_t, cadena_t, flotante_t

class DataFrame:
    @check_sig([3], [pandas_t], [lista_cadenas_t], [matriz_cualquiera_t])
    def __init__(self, columns, data):
        for row in data:
            if len(row) != len(columns):
                raise Exception(f"Inconsistent dimensions")

        self.columns = columns
        self.data = data

    def __repr__(self):
        contenido = f"cols: {self.columns}, rows: {self.data}"
        return repr(contenido)

    @check_sig([1, 2], [pandas_t], [entero_t])
    def head(self, *args):
        n = 5
        if len(args) == 1:
            n = args[0]

        return DataFrame(self.columns, self.data[:n])

    @check_sig([1, 2], [pandas_t], [entero_t])
    def tail(self, *args):
        n = 5
        if len(args) == 1:
            n = args[0]

        if n <= len(self.data):
            return DataFrame(self.columns, self.data[-n:])
        else:
            return DataFrame(self.columns, self.data[:])

    @check_sig([1], [pandas_t])
    def shape(self):
        n_filas = len(self.data)
        n_cols  = len(self.columns)
        return [n_filas, n_cols]

    @check_sig([2], [pandas_t], [cadena_t])
    def col(self, column_name):
        if column_name not in self.columns:
            raise Exception(f"Column '{column_name}' doesn't exist")
        idx = self.columns.index(column_name)

        # Raw: lista con valores, incluidos nan
        raw = [row[idx] for row in self.data]

        # Obtener DataFrame de dtypes y su data (lista de [col, tipo])
        dtypes_rows = self.dtypes()

        # Buscar tipo de la columna
        tipo_col = None
        for col, tipo in dtypes_rows:
            if col == column_name:
                tipo_col = tipo
                break

        # Crear filas normalizadas, cada fila es [valor]
        result_rows = []
        if tipo_col == cadena_t:
            for v in raw:
                if isinstance(v, float) and math.isnan(v):
                    result_rows.append("")
                else:
                    result_rows.append(str(v))

        elif tipo_col == entero_t:
            for v in raw:
                result_rows.append(int(v))

        elif tipo_col == flotante_t:
            for v in raw:
                if isinstance(v, float) and math.isnan(v):
                    result_rows.append(float("nan"))
                else:
                    result_rows.append(float(v))
        else:
            # Caso improbable, convertir todo a str
            for v in raw:
                result_rows.append(str(v))

        return result_rows

    @check_sig([1], [pandas_t])
    def dtypes(self):
        filas = []
        for j, col_name in enumerate(self.columns):
            vals = [
                row[j]
                for row in self.data
                if not (isinstance(row[j], float) and math.isnan(row[j])) and row[j] is not None
            ]
            tipo_col = cadena_t
            if len(vals) > 0 and all(isinstance(v, int) for v in vals):
                tipo_col = entero_t
            elif len(vals) > 0 and all(isinstance(v, (int, float)) for v in vals):
                tipo_col = flotante_t
            filas.append([col_name, tipo_col])

        return filas

    @check_sig([1], [pandas_t])
    def info(self):
        n_filas = len(self.data)
        n_cols  = len(self.columns)

        cols_str = ", ".join(self.columns)
        dtypes_rows = self.dtypes()    # [[col1,t1], [col2,t2], ...]
        dtypes_str = ", ".join(f"{c}:{t}" for c, t in dtypes_rows)

        filas = [
            ["Rows",         n_filas],
            ["Columns",      n_cols],
            ["Column_Names", cols_str],
            ["Dtypes",       dtypes_str]
        ]
        return f"{filas}"

    @check_sig([1], [pandas_t])
    def describe(self):
        cols = ["column", "count", "mean", "std", "min", "max"]
        filas = []

        tipo_df = self.dtypes()
        for i, tipo in enumerate(tipo_df):
            col_name = self.columns[i]
            if tipo[1] in (entero_t, flotante_t):
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
