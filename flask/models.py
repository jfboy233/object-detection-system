from extension import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    pwd = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Integer())
    head = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd

    def __repr__(self):
        return "<User '{}'>".format(self.username)
