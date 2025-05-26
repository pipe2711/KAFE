import os

from TypeUtils import cadena_t
from global_utils import check_sig
import globals

@check_sig([1], [cadena_t])
def create(filename):
    filename = os.path.join(globals.current_dir, filename)
    try:
        with open(filename, 'x'):
            pass
    except FileExistsError:
        raise Exception(f"create: File {os.path.basename(filename)} already exists")

@check_sig([1], [cadena_t])
def read(filename):
    filename = os.path.join(globals.current_dir, filename)
    try:
        with open(filename, 'r') as f:
            contenido = f.read()
        return contenido.rstrip('\n')
    except FileNotFoundError:
        raise Exception(f"read: File {os.path.basename(filename)} doesn't exist")

@check_sig([2], [cadena_t], [cadena_t])
def write(filename, content):
    filename = os.path.join(globals.current_dir, filename)
    try:
        with open(filename, 'a') as f:
            f.write(content + "\n")
    except Exception as e:
        raise Exception(f"write: Error writing on {os.path.basename(filename)}: {e}")

@check_sig([1], [cadena_t])
def delete(filename):
    filename = os.path.join(globals.current_dir, filename)
    try:
        os.remove(filename)
    except FileNotFoundError:
        raise Exception(f"delete: File {os.path.basename(filename)} doesn't exist")
