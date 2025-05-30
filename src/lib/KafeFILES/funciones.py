import os
from TypeUtils import cadena_t
from global_utils import check_sig
import globals

# Ruta base donde se almacenan archivos creados por los programas
BASE_FILES_DIR = "/home/ubuntu/KAFE/KAFE-SAAS/SERVER-FLASK/archivos_usuario"

def ruta_archivo(nombre_archivo):
    # Obtener el nombre del programa sin extensión
    nombre_programa = os.path.splitext(os.path.basename(globals.ruta_programa))[0]
    carpeta = os.path.join(BASE_FILES_DIR, nombre_programa)
    os.makedirs(carpeta, exist_ok=True)  # Crear carpeta si no existe
    return os.path.join(carpeta, nombre_archivo)

@check_sig([1], [cadena_t])
def create(filename):
    ruta = ruta_archivo(filename)
    if os.path.exists(ruta):
        raise Exception(f"create: File {os.path.basename(filename)} already exists")
    with open(ruta, 'x'):
        pass

@check_sig([1], [cadena_t])
def read(filename):
    ruta = ruta_archivo(filename)
    if not os.path.exists(ruta):
        raise Exception(f"read: File {os.path.basename(filename)} doesn't exist")
    with open(ruta, 'r') as f:
        contenido = f.read()
    return contenido.rstrip('\n')

@check_sig([2], [cadena_t], [cadena_t])
def write(filename, content):
    ruta = ruta_archivo(filename)
    try:
        with open(ruta, 'a') as f:
            f.write(content + "\n")
    except Exception as e:
        raise Exception(f"write: Error writing on {os.path.basename(filename)}: {e}")

@check_sig([1], [cadena_t])
def delete(filename):
    ruta = ruta_archivo(filename)
    if not os.path.exists(ruta):
        raise Exception(f"delete: File {os.path.basename(filename)} doesn't exist")
    os.remove(ruta)
