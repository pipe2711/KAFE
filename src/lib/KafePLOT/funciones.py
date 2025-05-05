from lib.KafePLOT.utils import guardar_svg

def set_xlabel(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        raise Exception("xlabel must be a string")
    plot.set_xlabel(valor)

def set_ylabel(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        raise Exception("ylabel must be a string")
    plot.set_ylabel(valor)

def set_title(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        raise Exception("title must be a string")
    plot.set_title(valor)

def set_grid(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, bool):
        raise Exception("grid must be True or False")
    plot.set_grid(valor)

def set_color(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        raise Exception("color must be a string")
    plot.set_color(valor)

def set_point_color(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        raise Exception("pointColor must be a string")
    plot.set_point_color(valor)

def set_point_size(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, int):
        raise Exception("pointSize must be an integer")
    plot.set_point_size(valor)

def plotgraph(self, ctx, plot, ruta_programa):
    args = ctx.expr()
    args = args if isinstance(args, list) else [args]

    # ========== MANEJO DE ARGUMENTOS ==========
    if len(args) == 1:
        datos = self.visit(args[0])

        if not isinstance(datos, list):
            raise Exception("plot.graph: Expected a list")

        if all(isinstance(v, (int, float)) for v in datos):
            xs = list(range(len(datos)))
            ys = datos
        elif all(isinstance(v, list) and len(v) == 2 for v in datos):
            xs = [v[0] for v in datos]
            ys = [v[1] for v in datos]
        else:
            raise Exception("plot.graph: List must contain numbers or [x, y] pairs")

    elif len(args) == 2:
        xs = self.visit(args[0])
        ys = self.visit(args[1])

        if not (isinstance(xs, list) and isinstance(ys, list)):
            raise Exception("plot.graph: Both arguments must be lists")

        if len(xs) != len(ys):
            raise Exception("plot.graph: Lists x and y must have the same length")

    else:
        raise Exception("plot.graph: Invalid number of arguments")

    contenido = plot.plotgraph(xs, ys)
    guardar_svg(contenido, ruta_programa)
    plot.reset()

def set_bar_values(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, bool):
        raise Exception("barValues must be True or False")
    plot.set_bar_values(valor)

def plot_bar(self, ctx, plot, ruta_programa):
    args = ctx.expr()
    if len(args) != 2:
        raise Exception("plot.bar: Expected 2 arguments (labels, values)")

    etiquetas = self.visit(args[0])
    valores = self.visit(args[1])

    if not (isinstance(etiquetas, list) and isinstance(valores, list)):
        raise Exception("plot.bar: Both arguments must be lists")

    if len(etiquetas) != len(valores):
        raise Exception("plot.bar: labels and values must have the same length")

    contenido = plot.plot_bar(valores, etiquetas)
    guardar_svg(contenido, ruta_programa)
    plot.reset()

def set_legend(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        raise Exception("legend must be a string")
    plot.set_legend(valor)

def plot_pie(self, ctx, plot, ruta_programa):
    args = ctx.expr()
    if len(args) != 2:
        raise Exception("plot.pie: Expected 2 arguments (labels, values)")

    etiquetas = self.visit(args[0])
    valores = self.visit(args[1])

    if not (isinstance(etiquetas, list) and isinstance(valores, list)):
        raise Exception("plot.pie: Both arguments must be lists")

    if len(etiquetas) != len(valores):
        raise Exception("plot.pie: Labels and values must be of equal length")

    contenido = plot.plot_pie(valores, etiquetas)
    guardar_svg(contenido, ruta_programa)
    plot.reset()
