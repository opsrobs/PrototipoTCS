from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_cors import CORS
from controller.gpt_controller.controller import GptController
from controller.smell_controller.controller import SmellController
from model.gpt import Gpt
from model.gpt_has_smell import GptHasSmell
from model import db

gpt_blueprint = Blueprint('gpt_view', __name__, template_folder="templates")
CORS(gpt_blueprint)

gpt = GptController()
smell = SmellController()

@gpt_blueprint.route("/historias", methods=["GET", "POST"])
def historias():
    if request.method == "POST":
        print(request.form["prompt"])
        prompt = request.form["prompt"]
        response = gpt.text_to_completion(temperature= 1, prompt = prompt, model = "text-davinci-003", max_tokens=256)
        historia_output = response.choices[0].text
        gpt_model = Gpt()
        gpt_model.set_historia_output(historia_output)
        gpt_model.set_historia_input(prompt)
        db.session.add(gpt_model)
        db.session.commit()
        smells = smell.text_to_get_smells(model="text-davinci-003", text=prompt)
        resultado = {"historia": response.choices[0].text, "smell": smells.choices[0].text}
        return jsonify(resultado)
    return render_template("gpt.html")


@gpt_blueprint.route("/gethistorias")
def get_historias():
    historias = Gpt.query.all()
    historias_json = []
    for historia in historias:
        historias_json.append({
            'id': historia.id,
            'UserStorie': historia.historia_input,
            'UserStoriePadronizada': historia.historia_output,
        })
    return jsonify(historias_json)
    return render_template("gethistorias.html", result=historias_json)

