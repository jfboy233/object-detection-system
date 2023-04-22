from flask import Blueprint, request, jsonify
from model import User, Cache
from .forms import RegisterForm, LoginForm, EmailForm
from werkzeug.security import generate_password_hash, check_password_hash
from extension import db, mail
from flask_mail import Message
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
                # 设置cookie
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
            validCode = form.code.data
            email = form.email.data
            cache = Cache.query.filter_by(email=email).first()
            # 验证码是否正确
            if validCode == cache.validCode:
                user = User(email=email, username=username, pwd=generate_password_hash(pwd), role=1)
                db.session.add(user)
                db.session.commit()
                db.session.query(Cache).filter(Cache.email == email).delete()
                res = {
                    'msg': "注册成功",
                    'code': '0',
                }
                return res
            else:
                res = {
                    'msg': "验证码错误",
                    'code': '1',
                }
                return res
        else:
            errors = form.username.errors + form.password.errors + form.email.errors + form.validCode.errors
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
            # 将验证码存入Cache表中
            ## 验证表中是否有数据冲突，若冲突，删除
            if email == Cache.query.filter_by(email=email).first().email:
                db.session.query(Cache).filter(Cache.email == email).delete()
            ## 在数据库表中加入验证码条目
            cache = Cache(email=email, validCode=validCode)
            db.session.add(cache)
            db.session.commit()
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
