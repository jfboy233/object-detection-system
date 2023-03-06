from flask import Flask
from extension import db
from config import DevConfig
from flask_migrate import Migrate
from flask_cors import CORS
from bluePrint.user import bp as login_bp

app = Flask(__name__)
CORS(app)
# 绑定配置文件
app.config.from_object(DevConfig)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(login_bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
