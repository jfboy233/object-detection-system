from flask import Flask
from extension import db, mail
from config import DevConfig
from flask_migrate import Migrate
from flask_cors import CORS
from bluePrint.user import bp as login_bp
from bluePrint.upload import bp as upload_bp

app = Flask(__name__,
            template_folder='.',  # 表示在当前目录寻找模板文件
            static_folder='',  # 空 表示为当前目录开通虚拟资源入口
            static_url_path='',
            )
CORS(app)
# 绑定配置文件
app.config.from_object(DevConfig)

db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(login_bp)
app.register_blueprint(upload_bp)

if __name__ == '__main__':
    app.run(debug=True)
