from flask import Flask
from extension import db, mail, cache
from config import DevConfig
from flask_migrate import Migrate
from flask_cors import CORS
from bluePrint.user import bp as login_bp

app = Flask(__name__)
CORS(app)
# 绑定配置文件
app.config.from_object(DevConfig)

cache.init_app(app)
db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run(debug=True)
