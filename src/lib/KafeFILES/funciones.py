import os

def create(filename):
    try:
        with open(filename, 'x') as f:
            pass  # Crea el archivo vacío si no existe
        print(f"[file.create] Archivo '{filename}' creado.")
    except FileExistsError:
        print(f"[file.create] El archivo '{filename}' ya existe.")

def read(filename):
    try:
        with open(filename, 'r') as f:
            contenido = f.read()
        print(f"[file.read] Contenido leído de '{filename}'.")
        return contenido
    except FileNotFoundError:
        print(f"[file.read] El archivo '{filename}' no existe.")
        return ""

def write(filename, content):
    try:
        with open(filename, 'a') as f:
            f.write(content + "\n")
        print(f"[file.write] Contenido escrito en '{filename}'.")
    except Exception as e:
        print(f"[file.write] Error al escribir en '{filename}': {e}")

def delete(filename):
    try:
        os.remove(filename)
        print(f"[file.delete] Archivo '{filename}' eliminado.")
    except FileNotFoundError:
        print(f"[file.delete] El archivo '{filename}' no existe.")
