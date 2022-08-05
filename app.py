from flask import Flask
from flask import url_for
from flask import request
from markupsafe import escape
import logging
from logging.config import dictConfig
from logging.handlers import SMTPHandler
from werkzeug.utils import secure_filename

# 日志配置
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)


# URL Building
@app.route("/")
def index():
    return render_template("index.html")

    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hello_name():
    return f"Hello, {escape(name)}!"

## Variable Rules
@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"

# Unique URLSs / Redirection Behavior
@app.route("/projects/")
def projects():
    return "The projcet page"

@app.route("/about")
def about():
    return "The about page"



# HTTP Methods
@app.route("/login", methods=["GET", "POST"])
def login():
    err = None
    if request.method == "POST":
        #print(request.form)
        if valid_login(request.form["username"],
                        request.form["password"]):
            log_the_user_in(request.form["username"])
            error = "success"
        else:
            error = "Invalid username/password"
    else:
        error = "Unsupport method"

    return render_template("login.html", error=error)

def valid_login(username=None, password=None):
    if username == None or password == None:
        return False
    else:
        return True

def log_the_user_in(username=None):
    return "todo"
    

@app.route("/profile/<username>")
def profile(username):
    return f"{username}\'s profile"

with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="/"))
    print(url_for("profile", username="Lee Chen"))
    print(url_for("static", filename="style.css"))


# Rendering Templates
from flask import render_template

@app.route("/greet/")
@app.route("/greet/<name>")
def greet(name=None):
    return render_template("hello.html", name=name)

# Acdessing Request Data

with app.test_request_context("/greet", method="GET"):
    assert request.method == "GET"
    assert request.path == "/greet"



# File Uploads
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")