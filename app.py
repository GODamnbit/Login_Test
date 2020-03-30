from flask import Flask
import add
import login
import fabu
app = Flask(__name__)


@app.route('/')
def index():
    return '这是首页！'


app.register_blueprint(login.log_server)
app.register_blueprint(add.add_server)
app.register_blueprint(fabu.fa)


if __name__ == '__main__':
    app.run(debug=True)
