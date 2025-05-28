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

# Función para eliminar un archivo después de un tiempo
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

        # Configurar ruta global para que plot.guardar_svg lo use
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

        # Si el archivo SVG se generó, programar su eliminación
        if os.path.exists(ruta_svg):
            eliminar_svg_mas_tarde(ruta_svg)

        return jsonify({
            'output': output,
            'svg_name': svg_filename if os.path.exists(ruta_svg) else None
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/static/<path:filename>')
def serve_svg(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
