# 本文件存在的意义是为了解决循环调用的问题
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_cache import Cache

cache = Cache()
db = SQLAlchemy()
mail = Mail()