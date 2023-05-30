""""""

from .db_init import db


class User(db.Model):
    """"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    posts = db.relationship('Post', backref='user', lazy=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
