class Plot:
    def __init__(self):
        self.eje_x_label = ""
        self.eje_y_label = ""
        self.titulo_grafico = ""
        self.mostrar_grid = False
        self.color_linea = "blue"
        self.color_puntos = "red"
        self.tamaño_punto = 3
        self.mostrar_valores_barras = False
        self.leyenda_pastel = None

    def reset(self):
        self.__init__()

    def set_legend(self, valor):
        self.leyenda_pastel = valor

    def set_bar_values(self, valor):
        self.mostrar_valores_barras = valor

    def set_xlabel(self, x_label):
        self.eje_x_label = x_label

    def set_ylabel(self, y_label):
        self.eje_y_label = y_label

    def set_title(self, title):
        self.titulo_grafico = title

    def set_grid(self, valor):
        self.mostrar_grid = valor

    def set_color(self, valor):
        self.color_linea = valor

    def set_point_color(self, valor):
        self.color_puntos = valor

    def set_point_size(self, valor):
        self.tamaño_punto = valor

    def deg_to_rad(self, grados):
        return grados * 3.141592653589793 / 180

    def sin(self, angle_deg):
        x = self.deg_to_rad(angle_deg)
        return x - (x**3)/6 + (x**5)/120 - (x**7)/5040 + (x**9)/362880

    def cos(self, angle_deg):
        x = self.deg_to_rad(angle_deg)
        return 1 - (x**2)/2 + (x**4)/24 - (x**6)/720 + (x**8)/40320


    def plotgraph(self, xs, ys):
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
        if self.mostrar_grid:
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
            lineas += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{self.color_linea}" stroke-width="2" />\n'

        # ========== SVG: PUNTOS ==========
        puntos_svg = "".join([f'<circle cx="{x}" cy="{y}" r="{self.tamaño_punto}" fill="{self.color_puntos}"/>\n' for x, y in puntos])

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
        etiqueta_eje_x = f'<text x="{width // 2}" y="{height - 5}" font-size="12" text-anchor="middle">{self.eje_x_label}</text>' if self.eje_x_label else ''
        etiqueta_eje_y = f'<g transform="translate(20,{height // 2}) rotate(-90)"><text font-size="12" text-anchor="middle">{self.eje_y_label}</text></g>' if self.eje_y_label else ''
        etiqueta_titulo = f'<text x="{width // 2}" y="20" font-size="14" text-anchor="middle" font-weight="bold">{self.titulo_grafico}</text>' if self.titulo_grafico else ''

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

        return contenido

    def plot_bar(self, valores, etiquetas):
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
            if self.mostrar_valores_barras:
                svg += f'<text x="{x + bar_width // 2}" y="{y - 5}" font-size="10" text-anchor="middle">{val}</text>\n'

        # Ejes y etiquetas opcionales
        if self.titulo_grafico:
            svg += f'<text x="{width // 2}" y="20" font-size="14" font-weight="bold" text-anchor="middle">{self.titulo_grafico}</text>\n'
        if self.eje_y_label:
            svg += f'<g transform="translate(20,{height // 2}) rotate(-90)"><text font-size="12" text-anchor="middle">{self.eje_y_label}</text></g>\n'

        # Ejes X y Y visibles
        svg += f'<line x1="{padding}" y1="{height - padding}" x2="{width - padding}" y2="{height - padding}" stroke="black" stroke-width="1" />'
        svg += f'<line x1="{padding}" y1="{padding}" x2="{padding}" y2="{height - padding}" stroke="black" stroke-width="1"/>\n'

        svg += '</svg>'

        return svg

    def plot_pie(self, valores, etiquetas):
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

            x1 = cx + radio * self.cos(start_angle)
            y1 = cy + radio * self.sin(start_angle)
            x2 = cx + radio * self.cos(end_angle)
            y2 = cy + radio * self.sin(end_angle)

            large_arc = 1 if angle > 180 else 0
            color = colores[i % len(colores)]

            path = f'M {cx},{cy} L {x1},{y1} A {radio},{radio} 0 {large_arc},1 {x2},{y2} Z'
            svg += f'<path d="{path}" fill="{color}" stroke="white" stroke-width="1"/>\n'

            # Porcentaje centrado
            mid_angle = start_angle + angle / 2
            tx = cx + (radio / 1.5) * self.cos(mid_angle)
            ty = cy + (radio / 1.5) * self.sin(mid_angle)
            porcentaje = round(val / total * 100, 1)
            svg += f'<text x="{tx}" y="{ty}" font-size="12" text-anchor="middle" dominant-baseline="middle">{porcentaje}%</text>\n'

            start_angle = end_angle

        # ======= LEYENDA OPCIONAL =======
        if self.leyenda_pastel:
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

        return svg
