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

@gpt_blueprint.route("/historias", methods=("GET", "POST"))
def historias():
    prompt = ""
    if request.method == "POST":
        print(request.form["prompt"])
        prompt = request.form["prompt"]
        response = gpt.text_to_completion(temperature= 1, prompt = prompt, model = "text-davinci-003", max_tokens=256)
        return redirect(url_for("gpt_view.historias", result=response.choices[0].text))
    
    result = request.args.get("result")
    if result != None:
        gpt_model = Gpt()
        gpt_has_smell = GptHasSmell()
        gpt_model.set_historia_output(result)
        gpt_model.set_historia_input(prompt)
        db.session.add(gpt_model)
        db.session.commit()
        last_id = gpt_model.id
        smells = smell.text_to_get_smells(model="gpt-3.5-turbo", prompt=result)
        print("id smell --> " + smells.choices[0].message['content'])
        print(''.join(filter(str.isdigit, smells.choices[0].message['content'])))
        smell_by_id = smell.get_smell_by_id(''.join(filter(str.isdigit, smells.choices[0].message['content'])))
        gpt_has_smell.set_id_gpt(last_id)
        gpt_has_smell.set_id_smell(smell_by_id["id"])
        db.session.add(gpt_has_smell)
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

    return render_template("gethistorias.html", result=historias_json)

