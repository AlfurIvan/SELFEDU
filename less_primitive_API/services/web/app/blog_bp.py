from flask import Blueprint, render_template, g, request, flash, redirect, url_for, session
from werkzeug.exceptions import abort

from .models import Post, User
from .models.db_init import db
from .auth_bp import login_required

bp = Blueprint("blog", __name__)


def get_post(post_id, check_author=True):
    """"""
    post = db.session.execute(
        db.select(Post.id, Post.title, Post.body, Post.created, Post.author_id, User.username)
        .join_from(User, Post)
        .where(Post.id == post_id)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {post_id} does not exist.")

    if check_author and post.author_id != g.user.id:
        abort(403)

    return post


@bp.route("/")
def index():
    posts = db.session.execute(
        db.select(
            Post.id, Post.title, Post.body, Post.created, Post.author_id,
            User.username
        ).join_from(User, Post)
    ).fetchall()
    return render_template("blog/index.html", posts=posts)


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """"""
    if request.method == "POST":
        n_title = request.form["title"]
        n_body = request.form["body"]
        error = None

        if not n_title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:

            author_id = g.user.id
            n_post = Post(author_id, n_title, n_body)
            db.session.add(n_post)
            db.session.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/create.html")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """"""
    post = get_post(id)
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db.session.execute(db.update(Post)
                               .where(Post.id == id)
                               .values(title=title, body=body)
                               )
            db.session.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/update.html", post=post)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """"""
    get_post(id)
    db.session.execute(db.delete(Post)
                       .where(Post.id == id)
                       )
    db.session.commit()
    return redirect(url_for("blog.index"))
