

from flask import Blueprint
from database.exts import db
from model.models import User

bp = Blueprint("user", __name__)

@bp.route("/")
def insert_user():
    db.session.add(User(username="job", password="123"))
    db.session.commit()
    db.session.close()
    return "Hello world"