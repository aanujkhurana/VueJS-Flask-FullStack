from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.after_request
def add_cors_headers(response):
    # Add headers to see if CORS is set
    print("Response Headers:", response.headers)
    return response

@app.route('/', methods=['GET'])
def shark():
    return jsonify(message='THIS IS A SHARK 🦈')

if __name__ == '__main__':
    app.run(debug=True)
