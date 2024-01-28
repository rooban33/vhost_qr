from flask import Flask, jsonify, request
from flask_cors import CORS
import cv2
import webbrowser

app = Flask(__name__)
CORS(app)

@app.route('/api/scan_qr_code', methods=['GET', 'POST'])
def scan_qr_code():
    print("I am Called")
    # Your QR code scanning logic here
    return jsonify({'message': 'API endpoint for QR code scanning'})

@app.route('/api/handle_root', methods=['GET', 'POST'])
def handle_root():
    if request.method == 'POST':
        print('Hello Shajith!!')
        return jsonify({'message': 'POST request processed successfully'})
    else:
        return jsonify({'message': 'Hello, this is a GET request!'})

if __name__ == '__main__':
    app.run(debug=True)
