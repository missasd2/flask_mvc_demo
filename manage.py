

from flask import Flask,request,render_template,jsonify

import config
from views.user import bp

from model.models import User
from database.exts import db
app = Flask(__name__)
app.config.from_object(config)

app.debug = True
db.init_app(app)

app.register_blueprint(bp)


if __name__ == '__main__':
    app.run()



