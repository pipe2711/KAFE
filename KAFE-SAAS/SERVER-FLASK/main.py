from flask import Flask, request, jsonify
from flask_cors import CORS
import tempfile
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route('/ejecutar', methods=['POST'])
def ejecutar_codigo():
    data = request.get_json()
    filename = data.get('filename', 'programa.kf')
    code = data.get('code', '')

    if not code:
        return jsonify({'error': 'No hay código para ejecutar.'}), 400

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.kf', mode='w') as temp_file:
            temp_file.write(code)
            temp_filename = temp_file.name

        result = subprocess.run(
            ['python3', '/home/ubuntu/KAFE/src/Kafe.py', temp_filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout + result.stderr
        os.remove(temp_filename)

        return jsonify({'output': output})

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
    app.run(host="0.0.0.0", port=5000, debug=True)
