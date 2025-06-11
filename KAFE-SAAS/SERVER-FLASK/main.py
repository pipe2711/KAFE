from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import tempfile
import subprocess
import os
import sys
import threading
import time

# Agregar ruta del código fuente
sys.path.append('/home/ubuntu/KAFE/src')

# Importar globals
import globals

app = Flask(__name__, static_folder='static')
CORS(app)

# Función para eliminar un archivo SVG después de cierto tiempo
def eliminar_svg_mas_tarde(ruta_svg, delay=10):
    def eliminar():
        time.sleep(delay)
        if os.path.exists(ruta_svg):
            os.remove(ruta_svg)
    threading.Thread(target=eliminar).start()

@app.route('/ejecutar', methods=['POST'])
def ejecutar_codigo():
    data = request.get_json()
    filename = data.get('filename', 'programa.kf')
    code = data.get('code', '')

    if not code:
        return jsonify({'error': 'No hay código para ejecutar.'}), 400

    try:
        # Guardar archivo temporal .kf con el nombre real
        ruta_archivo = f"/tmp/{filename}"
        with open(ruta_archivo, 'w') as f:
            f.write(code)

        # Configurar rutas globales
        globals.ruta_programa = ruta_archivo
        globals.current_dir = os.path.dirname(ruta_archivo)

        # Ejecutar el archivo con KAFE
        result = subprocess.run(
            ['python3', '/home/ubuntu/KAFE/src/Kafe.py', ruta_archivo],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout + result.stderr
        svg_filename = os.path.splitext(filename)[0] + ".svg"
        ruta_svg = os.path.join(app.static_folder, svg_filename)

        # Si se generó un SVG, programar su eliminación
        if os.path.exists(ruta_svg):
            eliminar_svg_mas_tarde(ruta_svg)

        # Detectar archivos .txt en la subcarpeta correspondiente
        nombre_programa = os.path.splitext(os.path.basename(filename))[0]
        txt_dir = os.path.join("/home/ubuntu/KAFE/KAFE-SAAS/SERVER-FLASK/archivos_usuario", nombre_programa)

        # Asegurar que la carpeta exista antes de listar archivos
        os.makedirs(txt_dir, exist_ok=True)

        archivos_txt = [f for f in os.listdir(txt_dir) if f.endswith(".txt")]

        return jsonify({
            'output': output,
            'svg_name': svg_filename if os.path.exists(ruta_svg) else None,
            'archivos_txt': archivos_txt
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/static/<path:filename>')
def serve_svg(filename):
    return send_from_directory(app.static_folder, filename)

# Descargar archivo .txt según programa
@app.route('/archivo_usuario/<programa>/<nombre>')
def descargar_archivo_txt(programa, nombre):
    base_dir = "/home/ubuntu/KAFE/KAFE-SAAS/SERVER-FLASK/archivos_usuario"
    ruta = os.path.join(base_dir, programa)
    return send_from_directory(ruta, nombre, as_attachment=True)

@app.route('/subir_csv', methods=['POST'])
def subir_csv():
    if 'archivo' not in request.files:
        return jsonify({'error': 'No se envió ningún archivo.'}), 400

    archivo = request.files['archivo']

    if archivo.filename == '':
        return jsonify({'error': 'El nombre del archivo está vacío.'}), 400

    if not archivo.filename.endswith('.csv'):
        return jsonify({'error': 'Solo se permiten archivos .csv'}), 400

    try:
        ruta_destino = '/home/ubuntu/KAFE/KAFE-SAAS/SERVER-FLASK/csv_usuario'
        os.makedirs(ruta_destino, exist_ok=True)

        ruta_final = os.path.join(ruta_destino, archivo.filename)
        archivo.save(ruta_final)

        return jsonify({'mensaje': f'Archivo {archivo.filename} subido correctamente.'}), 200

    except Exception as e:
        return jsonify({'error': f'Error al guardar el archivo: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
