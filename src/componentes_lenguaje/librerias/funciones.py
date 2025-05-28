from errores import raiseLibraryNotImported, raiseFunctionNotDefined, raiseVariableNotDefined

def revisar_libreria(library, libraries_dict):
    libreriaExistente = libraries_dict.get(library) != None
    if not libreriaExistente:
        raiseLibraryNotImported(library)

    seImporto = libraries_dict[library][1]
    if not seImporto:
        raiseLibraryNotImported(library)


def libraryFunctionCall(self, ctx):
    library = ctx.ID(0).getText()
    revisar_libreria(library, self.libraries)

    name = ctx.ID(1).getText()
    args = [self.visit(e) for e in ctx.expr()]
    func = getattr(self.libraries[library][0], name, None)

    if func is None:
        raiseFunctionNotDefined(name, origin=library)

    try:
        resultado = func(*args)
    except Exception as e:
        raise Exception(f"{library}: {str(e)}")

    return resultado

def libraryConstant(self, ctx):
    library = ctx.ID(0).getText()
    revisar_libreria(library, self.libraries)

    name = ctx.ID(1).getText()
    const = getattr(self.libraries[library][0], name, None)

    if const is None:
        raiseVariableNotDefined(name, origin=library)

    return const
