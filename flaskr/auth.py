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
"""
装饰器将URL：/register与 视图函数register联系起来
当flask接收到一个 /auth/register的请求，则会调用该视图函数进行处理并返回响应；
"""
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


# Login

"""
session 是一个字典，用以存储request中用户的数据；
当验证成功后，用户的id会存入一个新的session中；
数据会存入cookie，并且cookie会发送给浏览器
"""
@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if user is None:
            error = "Incorrect username"
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

        flash(error)
    return render_template("auth/login.html")

"""
该装饰器，用于注册一个函数到视图函数，以便使得该被装饰函数运行在所有视图函数之前
"""
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        )


"""
三 Logout
"""
@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


"""
四 Require Authentication in Other Views
"""

# 创建一个装饰器
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)

    return wrapped_view



