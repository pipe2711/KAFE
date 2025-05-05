import os

def guardar_svg(contenido, ruta_programa):
    carpeta_destino = os.path.dirname(ruta_programa)
    nombre_base = os.path.splitext(os.path.basename(ruta_programa))[0]
    nombre_svg = f"grafico_{nombre_base}.svg"
    ruta_svg = os.path.join(carpeta_destino, nombre_svg)

    with open(ruta_svg, "w") as f:
        f.write(contenido)
