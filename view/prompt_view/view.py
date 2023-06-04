from flask import Blueprint, jsonify
from flask_cors import CORS
from controller import helper
from controller.instrucao_prompt.controller import PromptInstrucaoController

prompt_blueprint = Blueprint('prompt_view', __name__, template_folder="templates")
CORS(prompt_blueprint)

prompt_controller = PromptInstrucaoController()

@prompt_blueprint.route("/instrucao", methods=["GET"])
@helper.token_required
def get_instructions(current_user):
    instrucoes = prompt_controller.get_instrucoes(current_user.id)
    instrucoes_json = []
    for instrucao in instrucoes:
        instrucoes_json.append({
            'id': instrucao.id,
            'instrucao': instrucao.instrucao,
            'ativo': instrucao.ativo,
            'usuario_id': instrucao.usuario_id
        })
    return jsonify(instrucoes_json), 201
        