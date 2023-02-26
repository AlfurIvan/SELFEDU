""""""

from .db_init import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    posts = db.relationship('Post', backref='user', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email
