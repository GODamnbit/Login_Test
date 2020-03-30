# coding=utf-8
from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)  # 实例化app对象

testInfo = {}
num = 10


@app.route('/test_post/nn', methods=['GET', 'POST'])  # 路由
def test_post():
    global num
    """receive data"""
    recv_data = request.get_data()
    if recv_data:
        print(recv_data)
        json_re = json.loads(recv_data)
        print(json_re['email'])
        print(json_re['phone'])
    else:
        print("receive data is empty")

    '''send data'''
    num = num + 1
    testInfo['name'] = 'xiaoming'
    testInfo['age'] = num
    return json.dumps(testInfo)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    return render_template('try.html')


if __name__ == '__main__':
    app.run(debug=True)
