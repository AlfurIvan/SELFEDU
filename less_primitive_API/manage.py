from flask.cli import FlaskGroup

from wsgi import app
from app.models.db_init import db

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


# TODO: make seeder
@cli.command("seed_db")
def seed_db():
    pass


if __name__ == '__main__':
    cli()
