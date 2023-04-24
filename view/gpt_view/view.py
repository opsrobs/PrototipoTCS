from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from controller.controller import GptController
from model.gpt import Gpt
from model import db

gpt_blueprint = Blueprint('gpt_view', __name__, template_folder="templates")

gpt_blueprint.static_folder='gpt_view/static'
gpt = GptController()

@gpt_blueprint.route("/historias", methods=("GET", "POST"))
def historias():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = gpt.text_to_completion(temperature= 1, prompt = prompt, model = "text-davinci-003", max_tokens=256)
        return redirect(url_for("gpt_view.historias", result=response.choices[0].text))
    
    result = request.args.get("result")
    gpt_model = Gpt()
    gpt_model.set_descricao(result)
    db.session.add(gpt_model)
    db.session.commit()
    return render_template("gpt.html", result=result)


@gpt_blueprint.route("/gethistorias")
def get_historias():
    historias = Gpt.query.all()

    historias_json = []
    for historia in historias:
        historias_json.append({
            'id': historia.id,
            'descricao': historia.descricao
        })

    return jsonify(historias_json)
