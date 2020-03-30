from flask import Flask
from flask import request, jsonify
import json

app = Flask(__name__)


@app.route('/post', methods=['GET', 'POST'])
def post():
    data = request.get_json()
    print(data)
    return jsonify(
        data=json.dumps(data),
        extra={
            'message': 'success'
        }
    )
