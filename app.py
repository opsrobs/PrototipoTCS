from flask import Flask, render_template
from view.gpt_view.view import gpt_blueprint

app = Flask(__name__)

app.register_blueprint(gpt_blueprint)


@app.route('/')
def index():
    return render_template('index.html')