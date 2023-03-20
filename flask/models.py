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

