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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
