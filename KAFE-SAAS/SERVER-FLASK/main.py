from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import tempfile
import os


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) #POR SEGURIDAD SE DEBE CAMBIAR 

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
          ['python3', '/home/qwerty/Documents/Lenguajes/KAFE/src/Kafe.py', temp_filename],
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
    app.run(debug=True, port=5000)
