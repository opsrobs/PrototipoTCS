from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from controller.smell_controller.controller import SmellController
from model.smell import RequirementSmell
from model import db

smell_blueprint = Blueprint('smell_view', __name__, template_folder="templates")

smell = SmellController()

""" @smell_blueprint.route("/smells", methods=["GET", "POST"])
def smells():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = smell.text_to_get_smells(temperature= 0.3, prompt = prompt, model = "text-davinci-003", max_tokens=256)
        return redirect(url_for("smell_view.smells", result=response.choices[0].text))    
    result = request.args.get("result")
    if result != "":
        smell_model = RequirementSmell()
        smell_model.s(result)
        db.session.add(gpt_model)
        db.session.commit()
    return render_template("requirementsmell.html", result=result) """