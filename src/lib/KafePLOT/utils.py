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
ultimo_svg_generado = None  # nuevo

# — NUEVAS variables para acumular SERIES en una misma FIGURA —
_figura_activa = False        # Indica si hay una figura iniciada
_series_acumuladas = []       # Aquí guardaremos cada serie (xs, ys, estilos)

def resetear_variables():
    global eje_x_label, eje_y_label, titulo_grafico, mostrar_valores_barras
    global mostrar_grid, color_puntos, color_linea, tamaño_punto, leyenda_pastel
    global _figura_activa, _series_acumuladas, ultimo_svg_generado

    eje_x_label = ""
    eje_y_label = ""
    titulo_grafico = ""
    mostrar_grid = False
    color_linea = "blue"
    color_puntos = "red"
    tamaño_punto = 3
    mostrar_valores_barras = False
    leyenda_pastel = None
    ultimo_svg_generado = None

    _figura_activa = False
    _series_acumuladas = []

def guardar_svg(contenido):
    global ultimo_svg_generado
    nombre_svg = os.path.splitext(os.path.basename(globals.ruta_programa))[0] + ".svg"
    ruta_svg = os.path.join("/home/ubuntu/KAFE/KAFE-SAAS/SERVER-FLASK/static", nombre_svg)

    with open(ruta_svg, "w") as f:
        f.write(contenido)

    ultimo_svg_generado = nombre_svg
