# utils.py
import os
import globals

# — Variables de estilo por defecto —
eje_x_label = ""
eje_y_label = ""
titulo_grafico = ""
mostrar_grid = False
color_linea = "blue"
color_puntos = "red"
tamaño_punto = 3
mostrar_valores_barras = False
leyenda_pastel = None

# — NUEVAS variables para acumular SERIES en una misma FIGURA —
_figura_activa = False        # Indica si hay una figura iniciada
_series_acumuladas = []       # Aquí guardaremos cada serie (xs, ys, estilos)

def resetear_variables():
    global eje_x_label, eje_y_label, titulo_grafico, mostrar_valores_barras
    global mostrar_grid, color_puntos, color_linea, tamaño_punto, leyenda_pastel
    global _figura_activa, _series_acumuladas

    eje_x_label = ""
    eje_y_label = ""
    titulo_grafico = ""
    mostrar_grid = False
    color_linea = "blue"
    color_puntos = "red"
    tamaño_punto = 3
    mostrar_valores_barras = False
    leyenda_pastel = None

    _figura_activa = False
    _series_acumuladas = []

def guardar_svg(contenido):
    carpeta_destino = os.path.dirname(globals.ruta_programa)
    nombre_svg = os.path.splitext(os.path.basename(globals.ruta_programa))[0] + ".svg"
    ruta_svg = os.path.join(carpeta_destino, nombre_svg)

    with open(ruta_svg, "w") as f:
        f.write(contenido)
