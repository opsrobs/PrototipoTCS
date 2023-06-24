from flask import Blueprint
from controller.gpt_has_smell_controller.controller import GptHasSmellController
from model.smell.smell import RequirementSmell
from flask_cors import CORS

gpt_has_smell_blueprint = Blueprint('gpt_has_smell_view', __name__, template_folder="templates")
CORS(gpt_has_smell_blueprint)

gpt_has_smell_controller = GptHasSmellController()

@gpt_has_smell_blueprint.route("/gpt_has_smell")
def get_all_gpt_has_smell():
    return gpt_has_smell_controller.get_all_gpt_has_smell(), 200