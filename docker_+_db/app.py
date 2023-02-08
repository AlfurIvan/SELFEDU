from flask import Flask, render_template
from os import environ
from db_init import db_session, db_init
from models import User
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/db_cr')
def try_db():
    db_init()
    return "init"


@app.route('/db_s')
def seed_db():
    u = User('admin', 'admin@hmail.com')
    db_session.add(u)
    db_session.commit()
    return "Seeding"


@app.route('/db_sh')
def res_db():
    return str(User.query.all())



if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
