# coding=utf-8
import json
from flask import request, Blueprint
import op_db

log_server = Blueprint('login', __name__)


@log_server.route('/login', methods=['POST'])
def login():
    # 登录需要两个参数，phone和pwd
    phone_log = request.values.get('phone')
    passwd_log = request.values.get('password')
    if phone_log and passwd_log:  # 非空为真
        # 需要先写一个导入数据库的函数
        sql = "SELECT * FROM user WHERE phone='%s' AND password='%s';" % (phone_log, passwd_log)
        result = op_db.login_add(sql)  # 执行sql
        if result:
            res = {"error_code": 1000, "mag": "登录成功!"}  # 接口返回的都是json
        else:
            res = {"error_code": 3001, "mag": "账号或密码错误！"}
    else:
        res = {"error_code": 3000, "mag": "必填参数未填，请查看接口文档！"}

    return json.dumps(res, ensure_ascii=False)  # 防止出现乱码；json.dumps()函数是将字典转化为字符串
