from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import os

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"
# For macOS or Linux, uncomment the next line and comment out the above line
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    file = request.files['image']

    try:
        # Open the image file
        image = Image.open(file.stream)
        
        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(image)
        
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
