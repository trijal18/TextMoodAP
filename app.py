from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return jsonify({'message': f'File uploaded successfully: {file.filename}'}), 200
    else:
        return jsonify({'error': 'No file part'}), 400  
if __name__ == '__main__':
    app.run(debug=True)
