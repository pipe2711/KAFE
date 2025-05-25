import os

nombre_lib = "files";
funciones = {
    "create": "create",
    "read": "read",
    "write": "write",
    "delete": "delete"
};

def create(filename):
    try:
        with open(filename, 'x'):
            pass
    except FileExistsError:
        raise Exception(f"{nombre_lib}.{funciones['create']}: File {os.path.basename(filename)} already exists")

def read(filename):
    try:
        with open(filename, 'r') as f:
            contenido = f.read()
        return contenido.rstrip('\n')
    except FileNotFoundError:
        raise Exception(f"{nombre_lib}.{funciones['read']}: File {os.path.basename(filename)} doesn't exist")

def write(filename, content):
    try:
        with open(filename, 'a') as f:
            f.write(content + "\n")
    except Exception as e:
        raise Exception(f"{nombre_lib}.{funciones['write']}: Error writing on {os.path.basename(filename)}: {e}")

def delete(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        raise Exception(f"{nombre_lib}.{funciones['delete']}: File {os.path.basename(filename)} doesn't exist")
