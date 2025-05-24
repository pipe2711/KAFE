from TypeUtils import construir_tipo_lista, obtener_tipo_dato, nombre_tipos
from componentes_lenguaje.errores import raiseFunctionIncorrectArgumentType, raiseWrongNumberOfArgs
from lib.KafePLOT.utils import guardar_svg

def set_xlabel(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        raiseFunctionIncorrectArgumentType(plot.funciones['xlabel'], valor, nombre_tipos[str], origin=plot.nombre_lib)
    plot.set_xlabel(valor)

def set_ylabel(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        raiseFunctionIncorrectArgumentType(plot.funciones['ylabel'], valor, nombre_tipos[str], origin=plot.nombre_lib)
    plot.set_ylabel(valor)

def set_title(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        raiseFunctionIncorrectArgumentType(plot.funciones['title'], valor, nombre_tipos[str], origin=plot.nombre_lib)
    plot.set_title(valor)

def set_grid(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, bool):
        raiseFunctionIncorrectArgumentType(plot.funciones['grid'], valor, nombre_tipos[bool], origin=plot.nombre_lib)
    plot.set_grid(valor)

def set_color(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        raiseFunctionIncorrectArgumentType(plot.funciones['color'], valor, nombre_tipos[str], origin=plot.nombre_lib)
    plot.set_color(valor)

def set_point_color(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        raiseFunctionIncorrectArgumentType(plot.funciones['pointColor'], valor, nombre_tipos[str], origin=plot.nombre_lib)
    plot.set_point_color(valor)

def set_point_size(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if type(valor) != int:
        raiseFunctionIncorrectArgumentType(plot.funciones['pointSize'], valor, nombre_tipos[int], origin=plot.nombre_lib)
    plot.set_point_size(valor)

def plotgraph(self, ctx, plot, ruta_programa):
    args = ctx.expr()
    args = args if isinstance(args, list) else [args]

    # ========== MANEJO DE ARGUMENTOS ==========
    if len(args) == 1:
        datos = self.visit(args[0])
        tipo_datos = obtener_tipo_dato(datos)
        tipo_esperado_lista = [construir_tipo_lista(int, 1), construir_tipo_lista(float, 1)]
        tipo_esperado_pares = [construir_tipo_lista(int, 2), construir_tipo_lista(float, 2)]

        if not isinstance(datos, list):
            raiseFunctionIncorrectArgumentType(plot.funciones['graph'], datos, nombre_tipos[list], origin=plot.nombre_lib)

        if tipo_datos in tipo_esperado_lista:
            xs = list(range(len(datos)))
            ys = datos
        elif tipo_datos in tipo_esperado_pares and all(len(v) == 2 for v in datos):
            xs = [v[0] for v in datos]
            ys = [v[1] for v in datos]
        else:
            tipos_esperados = [construir_tipo_lista(int, 1), construir_tipo_lista(float, 1), "pairs of numbers [x, y]"]
            raiseFunctionIncorrectArgumentType(plot.funciones['graph'], datos, tipos_esperados, origin=plot.nombre_lib)

    elif len(args) == 2:
        xs = self.visit(args[0])
        ys = self.visit(args[1])

        tipo_xs = obtener_tipo_dato(xs)
        tipo_ys = obtener_tipo_dato(ys)
        tipos_esperados = [construir_tipo_lista(int, 1), construir_tipo_lista(float, 1)]

        if not (tipo_xs in tipos_esperados):
            raiseFunctionIncorrectArgumentType(plot.funciones['graph'], xs, tipos_esperados, origin=plot.nombre_lib)

        if not (tipo_ys in tipos_esperados):
            raiseFunctionIncorrectArgumentType(plot.funciones['graph'], ys, tipos_esperados, origin=plot.nombre_lib)

        if len(xs) != len(ys):
            raise Exception(f"{plot.nombre_lib}.{plot.funciones['graph']}: Lists x and y must have the same length")

    else:
        raiseWrongNumberOfArgs(plot.funciones["graph"], "1 or 2", len(args), origin=plot.nombre_lib)

    contenido = plot.plotgraph(xs, ys)
    guardar_svg(contenido, ruta_programa)
    plot.reset()

def set_bar_values(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, bool):
        raiseFunctionIncorrectArgumentType(plot.funciones['barValues'], valor, nombre_tipos[bool], origin=plot.nombre_lib)
    plot.set_bar_values(valor)

def plot_bar(self, ctx, plot, ruta_programa):
    args = ctx.expr()
    if len(args) != 2:
        raiseWrongNumberOfArgs(plot.funciones["bar"], 2, len(args), origin=plot.nombre_lib)

    etiquetas = self.visit(args[0])
    valores = self.visit(args[1])

    tipo_etiquetas = obtener_tipo_dato(etiquetas)
    tipo_valores = obtener_tipo_dato(valores)
    tipo_esperado_etiquetas = construir_tipo_lista(str, 1)
    tipos_esperados_valores = [construir_tipo_lista(int, 1), construir_tipo_lista(float, 1)]

    if tipo_etiquetas != tipo_esperado_etiquetas:
        raiseFunctionIncorrectArgumentType(plot.funciones['bar'], etiquetas, tipo_esperado_etiquetas, origin=plot.nombre_lib)

    if not (tipo_valores in tipos_esperados_valores):
        raiseFunctionIncorrectArgumentType(plot.funciones['bar'], valores, tipos_esperados_valores, origin=plot.nombre_lib)

    if len(etiquetas) != len(valores):
        raise Exception(f"{plot.nombre_lib}.{plot.funciones['bar']}: labels and values must have the same length")

    contenido = plot.plot_bar(valores, etiquetas)
    guardar_svg(contenido, ruta_programa)
    plot.reset()

def set_legend(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        tipo_valor = obtener_tipo_dato(valor)
        raiseFunctionIncorrectArgumentType(plot.funciones['legend'], tipo_valor, nombre_tipos[str], origin=plot.nombre_lib)
    plot.set_legend(valor)

def plot_pie(self, ctx, plot, ruta_programa):
    args = ctx.expr()
    if len(args) != 2:
        raiseWrongNumberOfArgs(plot.funciones["pie"], 2, len(args), origin=plot.nombre_lib)

    etiquetas = self.visit(args[0])
    valores = self.visit(args[1])

    tipo_etiquetas = obtener_tipo_dato(etiquetas)
    tipo_valores = obtener_tipo_dato(valores)
    tipo_esperado_etiquetas = construir_tipo_lista(str, 1)
    tipos_esperados_valores = [construir_tipo_lista(int, 1), construir_tipo_lista(float, 1)]

    if tipo_etiquetas != tipo_esperado_etiquetas:
        raiseFunctionIncorrectArgumentType(plot.funciones['pie'], etiquetas, tipo_esperado_etiquetas, origin=plot.nombre_lib)

    if not (tipo_valores in tipos_esperados_valores):
        raiseFunctionIncorrectArgumentType(plot.funciones['pie'], valores, tipos_esperados_valores, origin=plot.nombre_lib)

    if len(etiquetas) != len(valores):
        raise Exception(f"{plot.nombre_lib}.{plot.funciones['pie']}: labels and values must have the same length")

    contenido = plot.plot_pie(valores, etiquetas)
    guardar_svg(contenido, ruta_programa)
    plot.reset()
