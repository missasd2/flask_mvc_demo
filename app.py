from flask import Flask
from flask import url_for
from flask import request
from markupsafe import escape
import logging
from logging.config import dictConfig
from flask import render_template
from logging.handlers import SMTPHandler
from werkzeug.utils import secure_filename
from flask import make_response

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
app.config["port"] = 80



# URL Building
@app.route("/")
def index():
    return render_template("index.html")

    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"


with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="/"))
    print(url_for("profile", username="Lee Chen"))
    print(url_for("static", filename="style.css"))


with app.test_request_context("/greet", method="GET"):
    assert request.method == "GET"
    assert request.path == "/greet"


# About Response
@app.errorhandler(404)
def not_found(error):
    return render_template("error.html"), 404

if __name__ == '__main__':
    app.run()