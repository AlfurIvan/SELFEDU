import functools

from flask import Blueprint, session, flash, request, render_template, redirect, url_for, g
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.exc import NoResultFound
from .models.db_init import db
from .models import User, Post

bp = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If user id is stored in session, load the user object from db in g.user"""
    if session.get("user_id"):
        g.user = db.session.execute(db.select(User)
                                    .where(User.id == session.get("user_id"))).scalar()
    else:
        g.user = None


@bp.route("/register", methods=("GET", "POST"))
def register():
    """"""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif not email:
            error = "Email is required."

        if error is None:
            user = User(username, generate_password_hash(password), email)
            try:
                db.session.add(user)
                db.session.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """"""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        error = None
        try:
            user = db.session.execute(db.select(User)
                                      .where(User.email == email)
                                      ).scalar_one()
        except NoResultFound:
            error = "Incorrect email."
        else:
            if not check_password_hash(user.password, password):
                error = "Incorrect password."
            elif error is None:
                session.clear()
                session["user_id"] = user.id
                return redirect(url_for("blog.index"))

        flash(error)

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """"""
    session.clear()
    return redirect(url_for("blog.index"))
