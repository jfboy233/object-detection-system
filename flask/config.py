class Config(object):
    pass


class ProConfig(Config):
    pass


class DevConfig(Config):
    # DEBUG = True
    # SQLite
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:gzw123456@127.0.0.1:3306/flask_test"
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
