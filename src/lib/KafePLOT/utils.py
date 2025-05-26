import os
import globals

eje_x_label = ""
eje_y_label = ""
titulo_grafico = ""
mostrar_grid = False
color_linea = "blue"
color_puntos = "red"
tamaño_punto = 3
mostrar_valores_barras = False
leyenda_pastel = None

def resetear_variables():
    global eje_x_label, eje_y_label, titulo_grafico, mostrar_valores_barras, mostrar_grid, color_puntos, color_linea, tamaño_punto, leyenda_pastel

    eje_x_label = ""
    eje_y_label = ""
    titulo_grafico = ""
    mostrar_grid = False
    color_linea = "blue"
    color_puntos = "red"
    tamaño_punto = 3
    mostrar_valores_barras = False
    leyenda_pastel = None

def guardar_svg(contenido):
    carpeta_destino = os.path.dirname(globals.ruta_programa)
    nombre_base = os.path.splitext(os.path.basename(globals.ruta_programa))[0]
    nombre_svg = f"grafico_{nombre_base}.svg"
    ruta_svg = os.path.join(carpeta_destino, nombre_svg)

    with open(ruta_svg, "w") as f:
        f.write(contenido)
