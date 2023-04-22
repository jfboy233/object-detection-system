import wtforms
from wtforms.validators import Length, EqualTo, Email
from model import User


class EmailForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    username = wtforms.StringField(validators=[Length(min=3, max=11, message="用户名格式错误！")])

    # 自定义验证
    # 验证用户名是否已经存在于数据库中
    def validate_username(self, field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if user:
            raise wtforms.ValidationError(message="该用户名已存在！")


class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    code = wtforms.StringField(validators=[Length(max=4, message="验证码格式错误")])
    username = wtforms.StringField(validators=[Length(min=3, max=11, message="用户名格式错误！")])
    password = wtforms.StringField(validators=[Length(min=3, max=16, message="密码格式错误!")])
    confirm = wtforms.StringField(validators=[EqualTo("password")])

    # 自定义验证
    # 验证用户名是否已经存在于数据库中
    def validate_username(self, field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if user:
            raise wtforms.ValidationError(message="该用户名已存在！")


class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=3, max=11, message="用户名格式错误！")])
    password = wtforms.StringField(validators=[Length(min=3, max=16, message="密码格式错误!")])

    # 自定义验证
    # 验证用户名是否存在于数据库中
    def validate_username(self, field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if not user:
            raise wtforms.ValidationError(message="该用户名不存在！")



