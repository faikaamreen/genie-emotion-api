from flask import Flask, request, jsonify
from deepface import DeepFace
import numpy as np
import cv2
import base64

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect_emotion():
    try:
        # Get base64 image data from the request
        img_data = request.json['image']
        img_bytes = base64.b64decode(img_data)
        np_arr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Analyze emotion
        result = DeepFace.analyze(img, actions=['emotion'])
        emotion = result[0]['dominant_emotion']

        return jsonify({'emotion': emotion})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)