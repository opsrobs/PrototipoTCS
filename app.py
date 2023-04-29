from flask import Flask, render_template
from view.gpt_view.view import gpt_blueprint
from view.smell_view.view import smell_blueprint
from flask_migrate import Migrate
from model import db

app = Flask(__name__)
app.register_blueprint(gpt_blueprint)
app.register_blueprint(smell_blueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost/tcs"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

from model.gpt import Gpt

@app.route('/')
def index():
    return render_template('index.html')