def obtener_tipo_lista(lista, nombre_tipos):
    tipo = "List["

    if len(lista) != 0:
        if type(lista[0]) is int:
            tipo += nombre_tipos[int]
        elif type(lista[0]) is float:
            tipo += nombre_tipos[float]
        elif type(lista[0]) is str:
            tipo += nombre_tipos[str]
        elif type(lista[0]) is bool:
            tipo += nombre_tipos[bool]
        else:
            tipo += obtener_tipo_lista(lista[0], nombre_tipos)

    tipo += ']'

    return tipo


def asignar_variable(self, name, valor, tipo):
    if tipo.startswith("FUNC"):
        if not callable(valor):
            raise TypeError(f"Expected function, got {type(valor).__name__}")
        self.variables[name] = (tipo, valor)
        return True

    if tipo in self.type_mapping:
        if type(valor) is not self.type_mapping[tipo]:
            raise TypeError(f"Expected {tipo}, obtained {type(valor).__name__.upper()}")
        self.variables[name] = (tipo, valor)
        return True

    if tipo.startswith("List") and any(t in tipo for t in ["INT", "FLOAT", "STR", "BOOL"]):
     
        if valor == []:  
            self.variables[name] = (tipo, valor)
            return True
        
        
        if isinstance(valor, list):
          
            if not verificarHomogeneidad(valor):
                raise TypeError("Expected homogeneous list")
            tipo_valor = obtener_tipo_lista(valor, self.nombre_tipos)
            tipo_base = tipo.replace("INT", "").replace("FLOAT", "")
            tipo_base = tipo_base.replace("STR", "").replace("BOOL", "")
            
           
            if valor and tipo_valor not in (tipo, tipo_base):
                raise TypeError(f"Expected {tipo}, obtained {tipo_valor}")
            self.variables[name] = (tipo, valor)
            return True
        
        
        if isinstance(valor, (int, float, str, bool)):
           
            lista_actual = self.variables.get(name, (None, None))[1]
            if not isinstance(lista_actual, list):
                raise TypeError(f"{name} is not a list")
            if len(lista_actual) == 0:
                raise IndexError(f"Cannot assign to index of an empty list: {name}")

           
            index = self.obtener_indice_de_lista(name)
            lista_actual[index] = valor
            self.variables[name] = (tipo, lista_actual)
            return True

    return False


def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def obtener_nivel_anidamiento(lista):
    if not isinstance(lista, list):
        return 0

    max_depth = 0
    for item in lista:
        if isinstance(item, list):
            depth = obtener_nivel_anidamiento(item)
            if depth > max_depth:
                max_depth = depth

    return max_depth + 1

def verificarHomogeneidad(lista):
    if len(lista) != 0:
        anidamiento = obtener_nivel_anidamiento(lista[0])
        for elemento in lista:
            if obtener_nivel_anidamiento(elemento) != anidamiento:
                return False

    lista = flatten_list(lista)
    if (len(lista) != 0):
        tipo = type(lista[0])
        for elemento in lista:
            if type(elemento) != tipo:
                return False

    return True
