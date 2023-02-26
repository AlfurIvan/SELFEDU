""""""

from flask import jsonify

from app import app_factory

app = app_factory()


@app.route('/hello')
def hello():
    return jsonify(Hello='World')


if __name__ == '__main__':
    app.run()
