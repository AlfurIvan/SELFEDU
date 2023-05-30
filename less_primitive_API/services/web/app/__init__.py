from flask import Flask, jsonify
from flask_migrate import Migrate

from .models.db_init import db
from . import auth_bp, blog_bp

MIGRATE = Migrate()


def app_factory():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    db.init_app(app)

    @app.route('/hello')
    def hello():
        return jsonify(Hello='World')

    app.register_blueprint(auth_bp.bp)
    app.register_blueprint(blog_bp.bp)
    MIGRATE.init_app(app, db)

    return app
