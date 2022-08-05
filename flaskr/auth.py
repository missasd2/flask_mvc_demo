import functools
"""
Blueprint是一种将相关view组织起来的方式, 不用直接向应用中注册视图，而是通过blueprint来注册视图

"""
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db


# url_prefix 将被预置到所有与这个名为auth的Blueprint相关的URL。
bp = Blueprint("auth", __name__, url_prefix="/auth")



# The First View: Register
@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None

        if not username:
            error = "Username is required"
        elif not password:
            error = "Password is required"
        if error is None:
            try:
                db.execute(
                    "INSERT INTO user(username, password) VALUES(?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))
        flash(error)
    return render_template("auth/register.html")

