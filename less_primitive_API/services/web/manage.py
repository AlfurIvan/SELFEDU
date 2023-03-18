from flask.cli import FlaskGroup

from wsgi import app
from app.models.db_init import db
from app.models import User, Post

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()


@cli.command("seed")
def seed():
    pass_hash = "pbkdf2:sha256:260000$1vws2iwuvhAFLw3y$74fa7d731c012db93eacba831daa1d0f2f07cc45f8aa9c48cb2eef01e8d38ebb"
    # assignment is necessary to crete object before adding
    user1 = User(username="Alpha", password=pass_hash, email="alpha@bet", )
    user2 = User(username="Beta", password=pass_hash, email="beta@bet")
    post1 = Post(author_id=1, title="I'm alpha", body="that's true")
    post2 = Post(author_id=2, title="I'm beta", body="that's true twice")
    with app.app_context():
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        db.session.add(post1)
        db.session.add(post2)
        db.session.commit()


if __name__ == "__main__":
    cli()
