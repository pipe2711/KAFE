from global_utils import check_sig
from TypeUtils import cadena_t, booleano_t, entero_t, obtener_tipo_dato, vector_numeros_t, matriz_numeros_t, lista_cadenas_t
from errores import raiseFunctionIncorrectArgumentType
from lib.KafeMATH.funciones import radians, sin, cos
import lib.KafePLOT.utils as utils

@check_sig([1], [cadena_t])
def legend(valor):
    utils.leyenda_pastel = valor

@check_sig([1], [booleano_t])
def barValues(valor):
    utils.mostrar_valores_barras = valor

@check_sig([1], [cadena_t])
def xlabel(x_label):
    utils.eje_x_label = x_label

@check_sig([1], [cadena_t])
def ylabel(y_label):
    utils.eje_y_label = y_label

@check_sig([1], [cadena_t])
def title(title):
    utils.titulo_grafico = title

@check_sig([1], [booleano_t])
def grid(valor):
    utils.mostrar_grid = valor

@check_sig([1], [cadena_t])
def color(valor):
    utils.color_linea = valor

@check_sig([1], [cadena_t])
def pointColor(valor):
    utils.color_puntos = valor

@check_sig([1], [entero_t])
def pointSize(valor):
    utils.tamaño_punto = valor

@check_sig([1, 2], vector_numeros_t + matriz_numeros_t, vector_numeros_t)
def graph(*args):
    datos = args[0]
    tipo_datos = obtener_tipo_dato(datos)

    if len(args) == 2:
        xs = datos

        if tipo_datos not in vector_numeros_t:
            raiseFunctionIncorrectArgumentType('graph', datos, tipo_datos)

        ys = args[1]

        if len(xs) != len(ys):
            raise Exception("graph: Lists x and y must have the same length")
    else:
        if tipo_datos in vector_numeros_t:
            xs = list(range(len(datos)))
            ys = datos
        else:
            if all(len(v) == 2 for v in datos):
                xs = [v[0] for v in datos]
                ys = [v[1] for v in datos]
            else:
                raise Exception("graph: Expected pairs of numbers [x, y]")


    # ========== ESCALADO Y PUNTOS ==========
    width = 500
    height = 300

    max_x, min_x = max(xs), min(xs)
    max_y, min_y = max(ys), min(ys)

    etiquetas_y_numeros = [round(min_y + i * (max_y - min_y) / 5, 1) for i in range(6)]
    numero_mas_largo = max(len(str(num)) for num in etiquetas_y_numeros)
    padding = int(10 + (numero_mas_largo + 2) * 6 + 20)  # dinámico sin escalar ylabel

    def escalar_x(x):
        return padding + int((x - min_x) / (max_x - min_x + 1e-5) * (width - 2 * padding))

    def escalar_y(y):
        return height - padding - int((y - min_y) / (max_y - min_y + 1e-5) * (height - 2 * padding))

    puntos = [(escalar_x(x), escalar_y(y)) for x, y in zip(xs, ys)]

    # ========== SVG: REJILLA ==========
    rejilla = ""
    if utils.mostrar_grid:
        for i in range(6):
            y = escalar_y(min_y + i * (max_y - min_y) / 5)
            rejilla += f'<line x1="{padding}" y1="{y}" x2="{width - padding}" y2="{y}" stroke="#ddd" stroke-width="1"/>\n'
        for xval in xs:
            x = escalar_x(xval)
            rejilla += f'<line x1="{x}" y1="{padding}" x2="{x}" y2="{height - padding}" stroke="#ddd" stroke-width="1"/>\n'

    # ========== SVG: LÍNEAS ==========
    lineas = ""
    for i in range(len(puntos) - 1):
        x1, y1 = puntos[i]
        x2, y2 = puntos[i + 1]
        lineas += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{utils.color_linea}" stroke-width="2" />\n'

    # ========== SVG: PUNTOS ==========
    puntos_svg = "".join([f'<circle cx="{x}" cy="{y}" r="{utils.tamaño_punto}" fill="{utils.color_puntos}"/>\n' for x, y in puntos])

    # ========== SVG: EJES ==========
    eje_x = f'<line x1="{padding}" y1="{height - padding}" x2="{width - padding}" y2="{height - padding}" stroke="black" stroke-width="1" />'
    eje_y = f'<line x1="{padding}" y1="{padding}" x2="{padding}" y2="{height - padding}" stroke="black" stroke-width="1" />'

    # ========== SVG: ETIQUETAS Y ==========
    etiquetas_y = ""
    for i in range(6):
        valor = min_y + i * (max_y - min_y) / 5
        y_pos = escalar_y(valor)
        etiquetas_y += f'<text x="{padding - 10}" y="{y_pos + 4}" font-size="10" text-anchor="end">{round(valor, 1)}</text>\n'

    # ========== SVG: ETIQUETAS X ==========
    etiquetas_x = ""
    for i, xval in enumerate(xs):
        x = escalar_x(xval)
        etiquetas_x += f'<text x="{x}" y="{height - padding + 15}" font-size="10" text-anchor="middle">{round(xval, 1)}</text>\n'

    # ========== SVG: ETIQUETAS DE LOS EJES ==========
    etiqueta_eje_x = f'<text x="{width // 2}" y="{height - 5}" font-size="12" text-anchor="middle">{utils.eje_x_label}</text>' if utils.eje_x_label else ''
    etiqueta_eje_y = f'<g transform="translate(20,{height // 2}) rotate(-90)"><text font-size="12" text-anchor="middle">{utils.eje_y_label}</text></g>' if utils.eje_y_label else ''
    etiqueta_titulo = f'<text x="{width // 2}" y="20" font-size="14" text-anchor="middle" font-weight="bold">{utils.titulo_grafico}</text>' if utils.titulo_grafico else ''

    # ========== SVG COMPLETO ==========
    contenido = f'''
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="{width}" height="{height}" fill="white"/>
  {rejilla}
  {eje_x}
  {eje_y}
  {etiquetas_y}
  {etiquetas_x}
  {lineas}
  {puntos_svg}
  {etiqueta_eje_x}
  {etiqueta_eje_y}
  {etiqueta_titulo}
</svg>
'''

    utils.guardar_svg(contenido)
    utils.resetear_variables()

@check_sig([2], [lista_cadenas_t], vector_numeros_t)
def bar(etiquetas, valores):
    if len(etiquetas) != len(valores):
        raise Exception("bar: labels and values must have the same length")

    width = 500
    height = 300
    padding = 60

    max_val = max(valores)
    bar_width = (width - 2 * padding) // len(valores)

    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
    svg += f'<rect width="100%" height="100%" fill="white"/>\n'

    # Eje Y
    for i in range(6):
        val = round(max_val * i / 5)
        y = height - padding - int((val / max_val) * (height - 2 * padding))
        svg += f'<line x1="{padding}" y1="{y}" x2="{width - padding}" y2="{y}" stroke="#ccc" />\n'
        svg += f'<text x="{padding - 10}" y="{y + 4}" font-size="10" text-anchor="end">{val}</text>\n'

    # Barras
    for i, (etq, val) in enumerate(zip(etiquetas, valores)):
        x = padding + i * bar_width
        h = int((val / max_val) * (height - 2 * padding))
        y = height - padding - h
        svg += f'<rect x="{x}" y="{y}" width="{bar_width - 5}" height="{h}" fill="steelblue" />\n'
        svg += f'<text x="{x + bar_width // 2}" y="{height - padding + 15}" font-size="10" text-anchor="middle">{etq}</text>\n'
        if utils.mostrar_valores_barras:
            svg += f'<text x="{x + bar_width // 2}" y="{y - 5}" font-size="10" text-anchor="middle">{val}</text>\n'

    # Ejes y etiquetas opcionales
    if utils.titulo_grafico:
        svg += f'<text x="{width // 2}" y="20" font-size="14" font-weight="bold" text-anchor="middle">{utils.titulo_grafico}</text>\n'
    if utils.eje_y_label:
        svg += f'<g transform="translate(20,{height // 2}) rotate(-90)"><text font-size="12" text-anchor="middle">{utils.eje_y_label}</text></g>\n'

    # Ejes X y Y visibles
    svg += f'<line x1="{padding}" y1="{height - padding}" x2="{width - padding}" y2="{height - padding}" stroke="black" stroke-width="1" />'
    svg += f'<line x1="{padding}" y1="{padding}" x2="{padding}" y2="{height - padding}" stroke="black" stroke-width="1"/>\n'

    svg += '</svg>'

    utils.guardar_svg(svg)
    utils.resetear_variables()

@check_sig([2], [lista_cadenas_t], vector_numeros_t)
def pie(etiquetas, valores):
    if len(etiquetas) != len(valores):
        raise Exception("pie: labels and values must have the same length")

    total = sum(valores)
    if total == 0:
        raise Exception("plot.pie: Total must be greater than zero")

    width = height = 600
    cx = int(width * 0.40)  # desplazamos el centro hacia la izquierda
    cy = height // 2
    radio = int(width * 0.3)

    start_angle = -180
    colores = ["#f4d03f", "#82e0aa", "#ec7063", "#85c1e9", "#bb8fce", "#f5b7b1", "#f1948a", "#7fb3d5", "#f8c471", "#aed6f1"]


    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
    svg += f'<rect width="100%" height="100%" fill="white"/>\n'

    for i, (_, val) in enumerate(zip(etiquetas, valores)):
        angle = val / total * 360
        end_angle = start_angle + angle

        x1 = cx + radio * cos(radians(start_angle))
        y1 = cy + radio * sin(radians(start_angle))
        x2 = cx + radio * cos(radians(end_angle))
        y2 = cy + radio * sin(radians(end_angle))

        large_arc = 1 if angle > 180 else 0
        color = colores[i % len(colores)]

        path = f'M {cx},{cy} L {x1},{y1} A {radio},{radio} 0 {large_arc},1 {x2},{y2} Z'
        svg += f'<path d="{path}" fill="{color}" stroke="white" stroke-width="1"/>\n'

        # Porcentaje centrado
        mid_angle = start_angle + angle / 2
        tx = cx + (radio / 1.5) * cos(radians(mid_angle))
        ty = cy + (radio / 1.5) * sin(radians(mid_angle))
        porcentaje = round(val / total * 100, 1)
        svg += f'<text x="{tx}" y="{ty}" font-size="12" text-anchor="middle" dominant-baseline="middle">{porcentaje}%</text>\n'

        start_angle = end_angle

    # ======= LEYENDA OPCIONAL =======
    if utils.leyenda_pastel:
        leyenda_x = width - 170
        leyenda_y = 40
        alto_recuadro = 20 * len(etiquetas) + 60

        svg += f'<rect x="{leyenda_x - 10}" y="{leyenda_y - 25}" width="160" height="{alto_recuadro}" fill="white" stroke="#ccc" rx="5"/>\n'

        svg += f'''<text x="{leyenda_x}" y="{leyenda_y}" font-size="12" font-weight="bold">
  <tspan x="{leyenda_x}" dy="0">Lenguajes de</tspan>
  <tspan x="{leyenda_x}" dy="15">Programación Populares</tspan>
</text>\n'''

        for i, (etq, color) in enumerate(zip(etiquetas, colores)):
            y_offset = leyenda_y + 30 + i * 20
            svg += f'<rect x="{leyenda_x}" y="{y_offset - 10}" width="10" height="10" fill="{color}"/>\n'
            svg += f'<text x="{leyenda_x + 15}" y="{y_offset}" font-size="10">{etq}</text>\n'

    svg += '</svg>\n'

    utils.guardar_svg(svg)
    utils.resetear_variables()
