import globals
import os

# Ruta base donde se almacenan archivos creados por los programas
BASE_FILES_DIR = "/home/ubuntu/KAFE/KAFE-SAAS/SERVER-FLASK/archivos_usuario"

def ruta_archivo(nombre_archivo):
    # Obtener el nombre del programa sin extensión
    nombre_programa = os.path.splitext(os.path.basename(globals.ruta_programa))[0]
    carpeta = os.path.join(BASE_FILES_DIR, nombre_programa)
    os.makedirs(carpeta, exist_ok=True)  # Crear carpeta si no existe
    return os.path.join(carpeta, nombre_archivo)
