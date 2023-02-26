from flask.cli import FlaskGroup

from wsgi import app
from app.models.db_init import db
from app.models import post, user

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


# TODO: finish seeder, understand commiting
@cli.command("seed_db")
def seed_db():
    db.session.add(user.User(username="Alpha", email="alpha@bet"))
    db.session.commit()
    db.session.add(user.User(username="Beta", email="beta@bet"))
    db.session.commit()
    # db.session.add(post.Post(author_id=0, title="I'm alpha", body="that's true"))
    # db.session.add(post.Post(author_id=1, title="I'm beta", body="that's true twice"))


if __name__ == '__main__':
    cli()
