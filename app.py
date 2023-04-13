from controller.controller import GptController
from flask import Flask, redirect, render_template, request, url_for, Blueprint

app = Flask(__name__)


gpt = GptController()


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = gpt.text_to_completion(temperature= 1, prompt = prompt, model = "text-davinci-003", max_tokens=256)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

