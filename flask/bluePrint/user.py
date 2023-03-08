from flask import Blueprint, request, jsonify
from models import User
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from extension import db

bp = Blueprint("user", __name__, url_prefix="/api/user")


@bp.route("/login", methods=['GET', 'POST'])
def login():
    # 表单内容验证
    if request.method == 'POST':
        data = request.get_json(silent=True)
        form = LoginForm(data=data)
        if form.validate():
            print("1")
            username = form.username.data
            pwd = form.password.data
            user = User.query.filter_by(username=username).first()
            if check_password_hash(user.pwd, pwd):
                # cookie：储存加密后的session
                # session['user_id'] = user.id
                res = {
                    'msg': "登录成功",
                    'code': '0',
                    'data': data
                }
                resp = jsonify(res)
                resp.status_code = 200
                return resp
            else:
                print("3")
                res = {
                    'msg': "密码错误！",
                    'code': '1',
                }
                return res
        else:
            errors = form.username.errors + form.password.errors
            # print(db.session.query(db.exists().where(User.username == form.username.data)).scalar())
            res = {
                'msg': errors[0],
                'code': '1',
            }
            return res

    return "login"


@bp.route("/register", methods=['GET', 'POST'])
def register():
    # 表单内容验证
    if request.method == 'POST':  # 进行数据的获取和表单验证
        data = request.get_json(silent=True)
        form = RegisterForm(data=data)
        if form.validate():
            username = form.username.data
            pwd = form.password.data
            user = User(username=username, pwd=generate_password_hash(pwd))
            db.session.add(user)
            db.session.commit()
            res = {
                'msg': "注册成功",
                'code': '0',
            }
            return res
        else:
            errors = form.username.errors + form.password.errors
            # print(db.session.query(db.exists().where(User.username == form.username.data)).scalar())
            res = {
                'msg': errors[0],
                'code': '1',
            }
            return res


