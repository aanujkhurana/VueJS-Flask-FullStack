from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origins': '*'}})
CORS(app, resources={r'/*':{'origins': 'http://localhost:5173',"allow_headers": "Access-Control-Allow-Origin"}})

# HELLO WORLD ROUTE
@app.route('/', methods=['GET'])
def shark():
    return ('THIS IS A SHARK 🦈')


if __name__ == '__main__':
    app.run(debug=True)