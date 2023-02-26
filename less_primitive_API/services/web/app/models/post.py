""""""

from datetime import datetime
from .db_init import db


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(3000), nullable=False)

    def __init__(self, author_id, title, body):
        self.author_id = author_id
        self.title = title
        self.body = body

