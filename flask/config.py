class Config(object):
    pass


class ProConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    # SQLite
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:gzw123456@127.0.0.1:3306/flask_test"
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

    # mail_config
    MAIL_SERVER = "smtp.163.com"
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USERNAME = "gzw3986@163.com"
    MAIL_PASSWORD = "OXCZQIPCSIQSWHRM"
    MAIL_DEFAULT_SENDER = "gzw3986@163.com"


