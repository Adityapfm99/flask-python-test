from flask import Flask, send_file, jsonify

from flask_cors import CORS

from service import *
from config import *

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route('/')
def index():
    return 'index.html'

@app.route('/api/v1/generate')
def generatefile():
    try:
        filename = generate()
        url = baseUrl + '/api/v1/download'
        data = {'link': url, 'message': "Generate txt successfully, It's saved in output.txt",'status': 200}
        return jsonify(data), 200
    except:
        return 404

@app.route('/api/v1/download')
def getfile():
    try:
        return send_file(fileName, as_attachment="True"), 200
    except:
        return 404

@app.route('/api/v1/report')
def objectcount():
    try:
        result = get_object_count()
        return jsonify(result), 200
    except:
        return 404


if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0", port=5000, debug=True)
