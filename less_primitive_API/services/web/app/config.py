import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
