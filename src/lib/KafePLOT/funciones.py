from global_utils import check_sig
from TypeUtils import (
    cadena_t, booleano_t, construir_tipo_lista,
    entero_t, obtener_tipo_dato, vector_numeros_t
)
from errores import raiseFunctionIncorrectArgumentType
from lib.KafeMATH.funciones import radians, sin, cos
import lib.KafePLOT.utils as utils

@check_sig([0], [])
def figure():

    utils.resetear_variables()
    utils._figura_activa = True

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


def graph(*args):
    n = len(args)
    if n < 1 or n > 3:
        raise Exception(
            "graph: se permiten 1, 2 o 3 argumentos:\n"
            "  • graph(ys)\n"
            "  • graph(xs, ys)\n"
            "  • graph(xs, ys, style)\n"
            "  • graph(lista_de_pares)\n"
        )


    if n == 1:
        dato = args[0]

        tipo_dato = obtener_tipo_dato(dato)
        if tipo_dato in vector_numeros_t:
            ys = dato
            xs = list(range(len(ys)))
            style = "both"

        elif (isinstance(dato, list)
              and len(dato) > 0
              and all(isinstance(par, list) and len(par) == 2 for par in dato)):

            xs, ys = [], []
            for par in dato:
                x_val, y_val = par

                tipo_x = obtener_tipo_dato(x_val)
                tipo_y = obtener_tipo_dato(y_val)
                if tipo_x not in vector_numeros_t and not isinstance(x_val, (int, float)):
                    raiseFunctionIncorrectArgumentType('graph', x_val, tipo_x)
                if tipo_y not in vector_numeros_t and not isinstance(y_val, (int, float)):
                    raiseFunctionIncorrectArgumentType('graph', y_val, tipo_y)
                xs.append(x_val)
                ys.append(y_val)
            style = "both"

        else:
            raiseFunctionIncorrectArgumentType('graph', dato, obtener_tipo_dato(dato))


    elif n == 2:
        primero, segundo = args

        if isinstance(segundo, str):
            dato = primero
            estilo_raw = segundo

            if (isinstance(dato, list)
                and len(dato) > 0
                and all(isinstance(par, list) and len(par) == 2 for par in dato)):
                xs, ys = [], []
                for par in dato:
                    x_val, y_val = par[0], par[1]

                    tipo_x = obtener_tipo_dato(x_val)
                    tipo_y = obtener_tipo_dato(y_val)
                    if tipo_x not in vector_numeros_t and not isinstance(x_val, (int, float)):
                        raiseFunctionIncorrectArgumentType('graph', x_val, tipo_x)
                    if tipo_y not in vector_numeros_t and not isinstance(y_val, (int, float)):
                        raiseFunctionIncorrectArgumentType('graph', y_val, tipo_y)
                    xs.append(x_val)
                    ys.append(y_val)

                style = estilo_raw.lower()
                if style not in ("line", "point", "both"):
                    raise Exception("graph: style debe ser 'line', 'point' o 'both'.")
            else:
                raise Exception(
                    "graph: si se pasan dos argumentos, el primero debe ser una lista de pares [[x,y],…] "
                    "y el segundo un string con el estilo ('line','point' o 'both')."
                )


        else:
            xs, ys = primero, segundo
            tipo_xs = obtener_tipo_dato(xs)
            tipo_ys = obtener_tipo_dato(ys)
            if tipo_xs not in vector_numeros_t:
                raiseFunctionIncorrectArgumentType('graph', xs, tipo_xs)
            if tipo_ys not in vector_numeros_t:
                raiseFunctionIncorrectArgumentType('graph', ys, tipo_ys)
            if len(xs) != len(ys):
                raise Exception("graph: Listas x e y deben tener el mismo largo.")
            style = "both"



    else:
        xs, ys, estilo_raw = args


        tipo_xs = obtener_tipo_dato(xs)
        tipo_ys = obtener_tipo_dato(ys)
        if tipo_xs not in vector_numeros_t:
            raiseFunctionIncorrectArgumentType('graph', xs, tipo_xs)
        if tipo_ys not in vector_numeros_t:
            raiseFunctionIncorrectArgumentType('graph', ys, tipo_ys)
        if len(xs) != len(ys):
            raise Exception("graph: Listas x e y deben tener el mismo largo.")


        if not isinstance(estilo_raw, str):
            raise Exception("graph: style debe ser una cadena literal.")
        style = estilo_raw.lower()
        if style not in ("line", "point", "both"):
            raise Exception("graph: style debe ser 'line', 'point' o 'both'.")


    auto_show = False
    if not utils._figura_activa:
        utils.resetear_variables()
        utils._figura_activa = True
        auto_show = True


    serie_info = {
        "xs": xs[:],
        "ys": ys[:],
        "color_linea": utils.color_linea,
        "color_puntos": utils.color_puntos,
        "tamaño_punto": utils.tamaño_punto,
        "draw_line":  (style in ("line", "both")),
        "draw_point": (style in ("point", "both"))
    }
    utils._series_acumuladas.append(serie_info)


    if auto_show:
        render()



@check_sig([0], [])
def render():

    if not utils._figura_activa or len(utils._series_acumuladas) == 0:
        raise Exception("render: No hay ninguna figura activa o no se llamó a graph() antes.")


    total_width    = 700
    total_height   = 350
    legend_space   = 200
    plot_width     = total_width - legend_space
    height         = total_height


    todas_x = [x for serie in utils._series_acumuladas for x in serie["xs"]]
    todas_y = [y for serie in utils._series_acumuladas for y in serie["ys"]]
    max_x, min_x = max(todas_x), min(todas_x)
    max_y, min_y = max(todas_y), min(todas_y)
    rango_x = max_x - min_x + 1e-5
    rango_y = max_y - min_y + 1e-5


    etiquetas_y_numeros = [round(min_y + i * (max_y - min_y) / 5, 1) for i in range(6)]
    numero_mas_largo = max(len(str(num)) for num in etiquetas_y_numeros)
    padding = int(10 + (numero_mas_largo + 2) * 6 + 20)


    def escalar_x(x):
        return padding + int((x - min_x) / rango_x * (plot_width - 2 * padding))
    def escalar_y(y):
        return height - padding - int((y - min_y) / rango_y * (height - 2 * padding))


    contenido  = f'<svg width="{total_width}" height="{total_height}" xmlns="http://www.w3.org/2000/svg">\n'
    contenido += f'  <rect x="0" y="0" width="{total_width}" height="{total_height}" fill="white"/>\n'


    if utils.mostrar_grid:

        for i in range(6):
            valor_y = min_y + i * (max_y - min_y) / 5
            y = escalar_y(valor_y)
            contenido += (
                f'  <line x1="{padding}" y1="{y}" '
                f'x2="{plot_width - padding}" y2="{y}" '
                f'stroke="#ddd" stroke-width="1"/>\n'
            )

        for xval in sorted(set(todas_x)):
            x_svg = escalar_x(xval)
            contenido += (
                f'  <line x1="{x_svg}" y1="{padding}" '
                f'x2="{x_svg}" y2="{height - padding}" '
                f'stroke="#ddd" stroke-width="1"/>\n'
            )


    for serie in utils._series_acumuladas:
        xs = serie["xs"]
        ys = serie["ys"]
        clr_linea = serie["color_linea"]
        clr_puntos = serie["color_puntos"]
        tam = serie["tamaño_punto"]
        draw_line = serie["draw_line"]
        draw_point = serie["draw_point"]


        if draw_line:
            for i in range(len(xs) - 1):
                x1, y1 = escalar_x(xs[i]), escalar_y(ys[i])
                x2, y2 = escalar_x(xs[i+1]), escalar_y(ys[i+1])
                contenido += (
                    f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                    f'stroke="{clr_linea}" stroke-width="2" />\n'
                )


        if draw_point:
            for xv, yv in zip(xs, ys):
                x_svg, y_svg = escalar_x(xv), escalar_y(yv)
                contenido += (
                    f'  <circle cx="{x_svg}" cy="{y_svg}" r="{tam}" fill="{clr_puntos}"/>\n'
                )


    contenido += (
        f'  <line x1="{padding}" y1="{height - padding}" '
        f'x2="{plot_width - padding}" y2="{height - padding}" '
        f'stroke="black" stroke-width="1" />\n'
    )

    contenido += (
        f'  <line x1="{padding}" y1="{padding}" '
        f'x2="{padding}" y2="{height - padding}" '
        f'stroke="black" stroke-width="1" />\n'
    )


    for i in range(6):
        valor_y = min_y + i * (max_y - min_y) / 5
        y_pos = escalar_y(valor_y)
        contenido += (
            f'  <text x="{padding - 10}" y="{y_pos + 4}" '
            f'font-size="10" text-anchor="end">{round(valor_y, 1)}</text>\n'
        )


    for xval in sorted(set(todas_x)):
        x_pos = escalar_x(xval)
        contenido += (
            f'  <text x="{x_pos}" y="{height - padding + 15}" '
            f'font-size="10" text-anchor="middle">{round(xval, 1)}</text>\n'
        )


    if utils.titulo_grafico:
        contenido += (
            f'  <text x="{total_width // 2}" y="20" '
            f'font-size="14" text-anchor="middle" font-weight="bold">'
            f'{utils.titulo_grafico}</text>\n'
        )

    if utils.eje_x_label:
        x_center_plot = padding + (plot_width - 2 * padding) // 2
        contenido += (
            f'  <text x="{x_center_plot}" y="{height - 5}" '
            f'font-size="12" text-anchor="middle">{utils.eje_x_label}</text>\n'
        )

    if utils.eje_y_label:
        contenido += (
            f'  <g transform="translate(20,{height // 2}) rotate(-90)">'
            f'<text font-size="12" text-anchor="middle">{utils.eje_y_label}</text></g>\n'
        )


    if utils.leyenda_pastel:

        leyenda_x = plot_width + 20
        leyenda_y = 30
        lineas = [linea.strip() for linea in utils.leyenda_pastel.split(";") if linea.strip() != ""]
        alto_recuadro = 20 * len(lineas) + 40
        ancho_recuadro = legend_space - 40


        contenido += (
            f'  <rect x="{leyenda_x - 10}" y="{leyenda_y - 25}" '
            f'width="{ancho_recuadro}" height="{alto_recuadro}" '
            f'fill="white" stroke="#ccc" rx="5"/>\n'
        )

        contenido += (
            f'  <text x="{leyenda_x}" y="{leyenda_y}" '
            f'font-size="12" font-weight="bold">Leyenda</text>\n'
        )


        y_offset = leyenda_y + 20
        for linea in lineas:

            if ":" in linea:
                color_str, texto = linea.split(":", 1)
                color_str = color_str.strip()
                texto = texto.strip()
                contenido += (
                    f'  <rect x="{leyenda_x}" y="{y_offset - 10}" '
                    f'width="10" height="10" fill="{color_str}"/>\n'
                )
                contenido += (
                    f'  <text x="{leyenda_x + 15}" y="{y_offset}" '
                    f'font-size="10">{texto}</text>\n'
                )
            else:

                contenido += (
                    f'  <text x="{leyenda_x}" y="{y_offset}" '
                    f'font-size="10">{linea}</text>\n'
                )
            y_offset += 20

    contenido += '</svg>\n'


    utils.guardar_svg(contenido)
    utils.resetear_variables()


@check_sig([2], [construir_tipo_lista(1, str)], vector_numeros_t)
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


    for i in range(6):
        val = round(max_val * i / 5)
        y = height - padding - int((val / max_val) * (height - 2 * padding))
        svg += f'<line x1="{padding}" y1="{y}" x2="{width - padding}" y2="{y}" stroke="#ccc" />\n'
        svg += f'<text x="{padding - 10}" y="{y + 4}" font-size="10" text-anchor="end">{val}</text>\n'


    for i, (etq, val) in enumerate(zip(etiquetas, valores)):
        x = padding + i * bar_width
        h = int((val / max_val) * (height - 2 * padding))
        y = height - padding - h
        svg += f'<rect x="{x}" y="{y}" width="{bar_width - 5}" height="{h}" fill="steelblue" />\n'
        svg += f'<text x="{x + bar_width // 2}" y="{height - padding + 15}" font-size="10" text-anchor="middle">{etq}</text>\n'
        if utils.mostrar_valores_barras:
            svg += f'<text x="{x + bar_width // 2}" y="{y - 5}" font-size="10" text-anchor="middle">{val}</text>\n'


    if utils.titulo_grafico:
        svg += f'<text x="{width // 2}" y="20" font-size="14" font-weight="bold" text-anchor="middle">{utils.titulo_grafico}</text>\n'
    if utils.eje_y_label:
        svg += f'<g transform="translate(20,{height // 2}) rotate(-90)"><text font-size="12" text-anchor="middle">{utils.eje_y_label}</text></g>\n'


    svg += f'<line x1="{padding}" y1="{height - padding}" x2="{width - padding}" y2="{height - padding}" stroke="black" stroke-width="1" />\n'
    svg += f'<line x1="{padding}" y1="{padding}" x2="{padding}" y2="{height - padding}" stroke="black" stroke-width="1"/>\n'

    svg += '</svg>'
    utils.guardar_svg(svg)
    utils.resetear_variables()


@check_sig([2], [construir_tipo_lista(1, str)], vector_numeros_t)
def pie(etiquetas, valores):
    if len(etiquetas) != len(valores):
        raise Exception("pie: labels and values must have the same length")

    total = sum(valores)
    if total == 0:
        raise Exception("plot.pie: Total must be mayor que cero")

    width = height = 600
    cx = int(width * 0.40)
    cy = height // 2
    radio = int(width * 0.3)

    start_angle = -180
    colores = ["#f4d03f", "#82e0aa", "#ec7063", "#85c1e9", "#bb8fce",
               "#f5b7b1", "#f1948a", "#7fb3d5", "#f8c471", "#aed6f1"]

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
        color_segment = colores[i % len(colores)]

        path = f'M {cx},{cy} L {x1},{y1} A {radio},{radio} 0 {large_arc},1 {x2},{y2} Z'
        svg += f'<path d="{path}" fill="{color_segment}" stroke="white" stroke-width="1"/>\n'


        mid_angle = start_angle + angle / 2
        tx = cx + (radio / 1.5) * cos(radians(mid_angle))
        ty = cy + (radio / 1.5) * sin(radians(mid_angle))
        porcentaje = round(val / total * 100, 1)
        svg += f'<text x="{tx}" y="{ty}" font-size="12" text-anchor="middle" dominant-baseline="middle">{porcentaje}%</text>\n'

        start_angle = end_angle


    if utils.leyenda_pastel:
        leyenda_x = width - 170
        leyenda_y = 40
        alto_recuadro = 20 * len(etiquetas) + 60

        svg += f'<rect x="{leyenda_x - 10}" y="{leyenda_y - 25}" width="160" height="{alto_recuadro}" fill="white" stroke="#ccc" rx="5"/>\n'
        svg += f'''<text x="{leyenda_x}" y="{leyenda_y}" font-size="12" font-weight="bold">
  <tspan x="{leyenda_x}" dy="0">Leyenda</tspan>
</text>\n'''
        for i, etq in enumerate(etiquetas):
            y_offset = leyenda_y + 30 + i * 20
            color_segment = colores[i % len(colores)]
            svg += f'<rect x="{leyenda_x}" y="{y_offset - 10}" width="10" height="10" fill="{color_segment}"/>\n'
            svg += f'<text x="{leyenda_x + 15}" y="{y_offset}" font-size="10">{etq}</text>\n'

    svg += '</svg>\n'
    utils.guardar_svg(svg)
    utils.resetear_variables()
