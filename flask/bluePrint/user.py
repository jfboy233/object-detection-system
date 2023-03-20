from flask import Blueprint, request, jsonify
from models import User
from .forms import RegisterForm, LoginForm, EmailForm
from werkzeug.security import generate_password_hash, check_password_hash
from extension import db, mail
from flask_mail import Message
from utils import cpcache
import string
import random

bp = Blueprint("user", __name__, url_prefix="/api/user")


@bp.route("/login", methods=['GET', 'POST'])
def login():
    # 表单内容验证
    if request.method == 'POST':
        data = request.get_json(silent=True)
        form = LoginForm(data=data)
        if form.validate():
            username = form.username.data
            pwd = form.password.data
            user = User.query.filter_by(username=username).first()
            if check_password_hash(user.pwd, pwd):
                # cookie：储存加密后的session
                # session['user_id'] = user.id
                res = {
                    'msg': "登录成功",
                    'code': '0',
                    'data': user.to_dict()
                }
                resp = jsonify(res)
                resp.status_code = 200
                return resp
            else:
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
    else:
        res = {
            'msg': "",
            'code': '1',
        }
        return res


@bp.route("/register", methods=['GET', 'POST'])
def register():
    # 表单内容验证
    if request.method == 'POST':  # 进行数据的获取和表单验证
        data = request.get_json(silent=True)
        form = RegisterForm(data=data)
        if form.validate():
            username = form.username.data
            pwd = form.password.data
            user = User(username=username, pwd=generate_password_hash(pwd), role=1)
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


@bp.route("/person", methods=['GET', 'POST'])
def person():
    if request.method == 'POST':
        pass
    else:
        pass


@bp.route("/sendValidCode", methods=['GET', 'POST'])
def sendCode():
    if request.method == 'POST':  # 进行数据的获取和表单验证
        data = request.get_json(silent=True)
        form = EmailForm(data=data)
        if form.validate():
            email = form.email.data
            # 生成4位随机数
            source = string.digits * 4
            validCode = random.sample(source, 4)
            validCode = "".join(validCode)
            # 发送验证信息
            message = Message(subject="【深潜目标检测系统】", recipients=[email],
                              body=f"欢迎注册目标检测系统，您的验证码是{validCode}，请勿将验证码告诉他人。")
            try:
                mail.send(message)  # 发送
            except:
                res = {
                    'msg': "邮件发送失败",
                    'code': '1',
                }
                return res
            # 将验证码存入redis数据库
            cpcache.set(email, validCode)
            print(cpcache.get(email))
            res = {
                'msg': "发送成功",
                'code': '0',
            }
            return res
        else:
            errors = form.email.errors + form.username.errors
            # print(db.session.query(db.exists().where(User.username == form.username.data)).scalar())
            res = {
                'msg': errors[0],
                'code': '1',
            }
            return res
