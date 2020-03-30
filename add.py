# coding=utf-8
import json
import op_db
from flask import Blueprint, request

add_server = Blueprint('add', __name__)


@add_server.route('/add', methods=['POST'])
def add():
    phone = request.values.get("phone")
    user_name = request.values.get("user_name")
    email = request.values.get("email")
    password = request.values.get("password")
    sex = request.values.get("sex")
    if sex:
        if sex == '男':
            sex = 1
        elif sex == '女':
            sex = 0
    else:
        sex = 1

    if phone and user_name and password:  # 必填参数校验

        if not phone.isdigit():  # 判断手机号格式是否正确
            res = {"error_code": 3005, "msg": "手机号输入错误"}

        else:
            sql = "select* from user where phone='%s';" % phone  # 查看数据库中是否有这个手机号，有的话说明重复
            result = op_db.login_add(sql)  # 执行sql
            if result:
                res = {"error_code": 1000, "msg": "手机号已经存在!"}

            else:
                sql = "INSERT INTO user(phone, user_name, email, password, sex)VALUES('%s','%s','%s','%s', '%s')" \
                      % (phone, user_name, email, password, sex)
                op_db.login_add(sql)
                res = {"error_code": 200, "msg": "新增成功！ "}
    else:
        res = {"error_code": 3007, "msg": "必填参数未填写!"}
    return json.dumps(res, ensure_ascii=False)  # 防止出现乱码
