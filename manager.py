# coding=utf-8
from flask_script import Manager, Server, Command
from flask import Flask

app = Flask(__name__)
manager = Manager(app)


# class Hello(Command):
#     """hello world"""
#     def run(self):
#         print('hello world')

# @manager.command  # 使用装饰器
# def hello():
#     """hello world"""
#     print('hello world')

@manager.option('-n', '--name', dest='name', help='Your name', default='world')
@manager.option('-u', '--url', dest='url', default='www.baidu.com')
def hello(name, url):
    """hello world or hello <setting name>"""
    print('hello', name)
    print(url)


# manager.add_command('hello', Hello)  # 把Hello子类定义为命令hello
# manager.add_command("runserver", Server)  # 命令是runserver


if __name__ == '__main__':
    manager.run()
