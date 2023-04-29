from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from controller.gpt_controller.controller import GptController
from controller.smell_controller.controller import SmellController
from model.gpt import Gpt
from model.gpt_has_smell import GptHasSmell
from model.smell import RequirementSmell
from model import db

gpt_blueprint = Blueprint('gpt_view', __name__, template_folder="templates")


gpt = GptController()
smell = SmellController()

@gpt_blueprint.route("/historias", methods=("GET", "POST"))
def historias():
    prompt = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = gpt.text_to_completion(temperature= 1, prompt = prompt, model = "text-davinci-003", max_tokens=256)
        return redirect(url_for("gpt_view.historias", result=response.choices[0].text))
    
    result = request.args.get("result")
    print(result)
    if result != None:
        gpt_model = Gpt()
        smell_model = RequirementSmell()
        gpt_has_smell = GptHasSmell()
        gpt_model.set_historia_output(result)
        gpt_model.set_historia_input(prompt)
        db.session.add(gpt_model)
        db.session.commit()
        ultimo_id = gpt_model.id
        smells = smell.text_to_get_smells(model="gpt-3.5-turbo", prompt=result)
        print(smells.choices[0].message['content'])
        #Falta ir na model do smell e setar para que compare com que smell é, pra assim poder ser escolhido corretamente
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

