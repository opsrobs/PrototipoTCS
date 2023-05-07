from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from controller.smell_controller.controller import SmellController
from model.smell import RequirementSmell
from model import db

smell_blueprint = Blueprint('smell_view', __name__, template_folder="templates")

smell = SmellController()

model_smell = RequirementSmell()

@smell_blueprint.route("/smell/<id>")
def get_smell_by_id(id):
    smell_by_id = model_smell.query.get(id)
    smell_by_id_dict = {"id": smell_by_id.id, "nome": smell_by_id.nome, "detalhe": smell_by_id.detalhe}
    return smell_by_id_dict