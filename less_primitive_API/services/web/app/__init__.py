from flask import Flask
from .models.db_init import db


def app_factory():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    db.init_app(app)
    return app
