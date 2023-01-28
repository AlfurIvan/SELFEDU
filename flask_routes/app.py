from flask import Flask, request, url_for
app = Flask(__name__)


@app.route('/')
def hello_dev():  # put application's code here
    return 'Hello Dev!'


@app.route('/user/<string:username>')
def user_route(username):
    return f"User {username} was here!!!"


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return user_route('(signed in)')
    else:
        return login_form()


@app.route('/login/form')
def login_form():
    return 'Login form on this endpoint'


@app.route('/projects/')
def project_route():
    return 'redirections'


if __name__ == '__main__':
    app.run(debug=True)
