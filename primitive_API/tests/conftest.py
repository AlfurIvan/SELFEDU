import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    """This fixture runs app in test configuration with test database"""
    # temporary database file descriptor & path
    db_fd, db_path = tempfile.mktemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    # close SQL script file & unlink
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """Fixture creates virtual client to communicate with app without running server"""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Fixture allows running cli (click) commands registered with the app"""
    return app.test_cli_runner()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post('/auth/login', data={'username': username, 'password': password})

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
