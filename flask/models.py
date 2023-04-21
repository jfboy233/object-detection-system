from extension import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    pwd = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Integer())
    head = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False)

    def __init__(self, email, username, pwd, role):
        self.email = email
        self.username = username
        self.pwd = pwd
        self.role = role

    def __repr__(self):
        return "<User '{}'>".format(self.username)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'head': self.head,
            'phone': self.phone,
            'email': self.email,
        }

    def set_head(self, head):
        self.head = head

    def set_phone(self, phone):
        self.phone = phone


class Cache(db.Model):
    email = db.Column(db.String(255), nullable=False, primary_key=True)
    validCode = db.Column(db.String(255), nullable=False)

    def __init__(self, email, validCode):
        self.email = email
        self.validCode = validCode


class Picture(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer())
    fileName = db.Column(db.String(255), nullable=False)
    time = db.Column(db.DateTime(), nullable=False)
    state = db.Column(db.Integer())  # 1,未处理 2,处理中 3,已完成
    origin_path = db.Column(db.String(255), nullable=False)
    target_path = db.Column(db.String(255))

    def __init__(self, userId, fileName, time, path):
        self.userId = userId
        self.fileName = fileName
        self.time = time
        self.state = 1
        self.origin_path = path
