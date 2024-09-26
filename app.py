from flask import Flask, request, jsonify
import os
from read_reviews import read_reviews
from model import analyze_sentiment

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload-file', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        filename = file.filename
        
        if not filename.endswith(('.xlsx', '.csv')):
            return jsonify({'error': 'Invalid file format. Please upload an XLSX or CSV file.'}), 400
        
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
    else:
        return jsonify({'error': 'No file part'}), 400

    try:
        sentiment = read_reviews(filepath)
        return jsonify(sentiment), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred during file processing: {str(e)}'}), 500


@app.route('/review', methods=['POST'])
def review():
    try:
        review = request.form.get('review')

        if not review:
            return jsonify({'error': 'Review text is required.'}), 400
        
        sentiment = analyze_sentiment(review)
        return jsonify(sentiment), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred during sentiment analysis: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
