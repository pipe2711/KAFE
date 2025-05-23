from componentes_lenguaje.errores import raiseFunctionIncorrectArgumentType, raiseWrongNumberOfArgs
from lib.KafePLOT.utils import guardar_svg

def set_xlabel(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        tipo_valor = self.obtener_tipo_dato(valor)
        raiseFunctionIncorrectArgumentType(plot.funciones['xlabel'], tipo_valor, self.nombre_tipos[str], origin=plot.nombre_lib)
    plot.set_xlabel(valor)

def set_ylabel(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        tipo_valor = self.obtener_tipo_dato(valor)
        raiseFunctionIncorrectArgumentType(plot.funciones['ylabel'], tipo_valor, self.nombre_tipos[str], origin=plot.nombre_lib)
    plot.set_ylabel(valor)

def set_title(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        tipo_valor = self.obtener_tipo_dato(valor)
        raiseFunctionIncorrectArgumentType(plot.funciones['title'], tipo_valor, self.nombre_tipos[str], origin=plot.nombre_lib)
    plot.set_title(valor)

def set_grid(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, bool):
        tipo_valor = self.obtener_tipo_dato(valor)
        raiseFunctionIncorrectArgumentType(plot.funciones['grid'], tipo_valor, self.nombre_tipos[bool], origin=plot.nombre_lib)
    plot.set_grid(valor)

def set_color(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        tipo_valor = self.obtener_tipo_dato(valor)
        raiseFunctionIncorrectArgumentType(plot.funciones['color'], tipo_valor, self.nombre_tipos[str], origin=plot.nombre_lib)
    plot.set_color(valor)

def set_point_color(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        tipo_valor = self.obtener_tipo_dato(valor)
        raiseFunctionIncorrectArgumentType(plot.funciones['pointColor'], tipo_valor, self.nombre_tipos[str], origin=plot.nombre_lib)
    plot.set_point_color(valor)

def set_point_size(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if type(valor) != int:
        tipo_valor = self.obtener_tipo_dato(valor)
        raiseFunctionIncorrectArgumentType(plot.funciones['pointSize'], tipo_valor, self.nombre_tipos[int], origin=plot.nombre_lib)
    plot.set_point_size(valor)

def plotgraph(self, ctx, plot, ruta_programa):
    args = ctx.expr()
    args = args if isinstance(args, list) else [args]

    # ========== MANEJO DE ARGUMENTOS ==========
    if len(args) == 1:
        datos = self.visit(args[0])
        tipo_datos = self.obtener_tipo_dato(datos)
        tipo_esperado_lista = [self.construir_tipo_lista(int, 1), self.construir_tipo_lista(float, 1)]
        tipo_esperado_pares = [self.construir_tipo_lista(int, 2), self.construir_tipo_lista(float, 2)]

        if not isinstance(datos, list):
            raiseFunctionIncorrectArgumentType(plot.funciones['graph'], tipo_datos, self.nombre_tipos[list], origin=plot.nombre_lib)

        if tipo_datos in tipo_esperado_lista:
            xs = list(range(len(datos)))
            ys = datos
        elif tipo_datos in tipo_esperado_pares and all(len(v) == 2 for v in datos):
            xs = [v[0] for v in datos]
            ys = [v[1] for v in datos]
        else:
            tipos_esperados = [self.construir_tipo_lista(int, 1), self.construir_tipo_lista(float, 1), "pairs of numbers [x, y]"]
            raiseFunctionIncorrectArgumentType(plot.funciones['graph'], tipo_datos, tipos_esperados, origin=plot.nombre_lib)

    elif len(args) == 2:
        xs = self.visit(args[0])
        ys = self.visit(args[1])

        tipo_xs = self.obtener_tipo_dato(xs)
        tipo_ys = self.obtener_tipo_dato(ys)
        tipos_esperados = [self.construir_tipo_lista(int, 1), self.construir_tipo_lista(float, 1)]

        if not (tipo_xs in tipos_esperados):
            raiseFunctionIncorrectArgumentType(plot.funciones['graph'], tipo_xs, tipos_esperados, origin=plot.nombre_lib)

        if not (tipo_ys in tipos_esperados):
            raiseFunctionIncorrectArgumentType(plot.funciones['graph'], tipo_ys, tipos_esperados, origin=plot.nombre_lib)

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
        tipo_valor = self.obtener_tipo_dato(valor)
        raiseFunctionIncorrectArgumentType(plot.funciones['barValues'], tipo_valor, self.nombre_tipos[bool], origin=plot.nombre_lib)
    plot.set_bar_values(valor)

def plot_bar(self, ctx, plot, ruta_programa):
    args = ctx.expr()
    if len(args) != 2:
        raiseWrongNumberOfArgs(plot.funciones["bar"], 2, len(args), origin=plot.nombre_lib)

    etiquetas = self.visit(args[0])
    valores = self.visit(args[1])

    tipo_etiquetas = self.obtener_tipo_dato(etiquetas)
    tipo_valores = self.obtener_tipo_dato(valores)
    tipo_esperado_etiquetas = self.construir_tipo_lista(str, 1)
    tipos_esperados_valores = [self.construir_tipo_lista(int, 1), self.construir_tipo_lista(float, 1)]

    if tipo_etiquetas != tipo_esperado_etiquetas:
        raiseFunctionIncorrectArgumentType(plot.funciones['bar'], tipo_etiquetas, tipo_esperado_etiquetas, origin=plot.nombre_lib)

    if not (tipo_valores in tipos_esperados_valores):
        raiseFunctionIncorrectArgumentType(plot.funciones['bar'], tipo_valores, tipos_esperados_valores, origin=plot.nombre_lib)

    if len(etiquetas) != len(valores):
        raise Exception(f"{plot.nombre_lib}.{plot.funciones['bar']}: labels and values must have the same length")

    contenido = plot.plot_bar(valores, etiquetas)
    guardar_svg(contenido, ruta_programa)
    plot.reset()

def set_legend(self, ctx, plot):
    valor = self.visit(ctx.expr())
    if not isinstance(valor, str):
        tipo_valor = self.obtener_tipo_dato(valor)
        raiseFunctionIncorrectArgumentType(plot.funciones['legend'], tipo_valor, self.nombre_tipos[str], origin=plot.nombre_lib)
    plot.set_legend(valor)

def plot_pie(self, ctx, plot, ruta_programa):
    args = ctx.expr()
    if len(args) != 2:
        raiseWrongNumberOfArgs(plot.funciones["pie"], 2, len(args), origin=plot.nombre_lib)

    etiquetas = self.visit(args[0])
    valores = self.visit(args[1])

    tipo_etiquetas = self.obtener_tipo_dato(etiquetas)
    tipo_valores = self.obtener_tipo_dato(valores)
    tipo_esperado_etiquetas = self.construir_tipo_lista(str, 1)
    tipos_esperados_valores = [self.construir_tipo_lista(int, 1), self.construir_tipo_lista(float, 1)]

    if tipo_etiquetas != tipo_esperado_etiquetas:
        raiseFunctionIncorrectArgumentType(plot.funciones['pie'], tipo_etiquetas, tipo_esperado_etiquetas, origin=plot.nombre_lib)

    if not (tipo_valores in tipos_esperados_valores):
        raiseFunctionIncorrectArgumentType(plot.funciones['pie'], tipo_valores, tipos_esperados_valores, origin=plot.nombre_lib)

    if len(etiquetas) != len(valores):
        raise Exception(f"{plot.nombre_lib}.{plot.funciones['pie']}: labels and values must have the same length")

    contenido = plot.plot_pie(valores, etiquetas)
    guardar_svg(contenido, ruta_programa)
    plot.reset()
