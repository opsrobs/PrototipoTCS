from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from controller.smell_controller.controller import SmellController
from controller.gpt_has_smell_controller.controller import GptHasSmellController
from model.smell import RequirementSmell
from flask_cors import CORS
from model import db

smell_blueprint = Blueprint('smell_view', __name__, template_folder="templates")
CORS(smell_blueprint)


smell_controller = SmellController()
gpt_has_smell_controller = GptHasSmellController()
smell_model = RequirementSmell()

@smell_blueprint.route("/smell/<id>")
def get_smell_by_id(id):
    smell_by_id = smell_model.query.get(id)
    smell_by_id_dict = {"id": smell_by_id.id, "nome": smell_by_id.nome, "detalhe": smell_by_id.detalhe}
    return smell_by_id_dict

@smell_blueprint.route("/get_smell_status")
def get_smell_status():
    all_smells = smell_controller.get_all_smells()
    return gpt_has_smell_controller.get_count_smells(all_smells)