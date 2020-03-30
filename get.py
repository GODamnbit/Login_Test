from flask import Flask
from flask import request, jsonify
app = Flask(__name__)


@app.route('/get', methods=['GET', 'POST'])
def get():
    name = request.args.get('name', '')
    if name == 'xuefeilong':
        age = 21
    else:
        age = 'valid name'
    return jsonify(
        data={name: age},
        extra={
            'total': '120'
        }
    )


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')
