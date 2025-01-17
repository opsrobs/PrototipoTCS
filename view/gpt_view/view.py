from flask import Blueprint, jsonify, request
from flask_cors import CORS
from controller.gpt_controller.controller import GptController
from controller.smell_controller.controller import SmellController
from controller.user_controller.controller import UserController
from controller.instrucao_prompt.controller import PromptInstrucaoController
from controller.gpt_has_smell_controller.controller import GptHasSmellController
from model.gpt import Gpt
from controller import helper
from model import db

gpt_blueprint = Blueprint('gpt_view', __name__, template_folder="templates")
CORS(gpt_blueprint)

gpt = GptController()
smell = SmellController()
user_controller = UserController()
prompt_instrucao = PromptInstrucaoController()
gpt_has_smells = GptHasSmellController()


@gpt_blueprint.route("/historias", methods=["POST"])
@helper.token_required
def historias(current_user):
    prompt = request.form["prompt"]
    response = gpt.text_to_completion(
        temperature=1, prompt=prompt, model="text-davinci-003", max_tokens=256)
    historia_output = response.choices[0].text
    gpt_model = Gpt()
    gpt_model.set_historia_output(historia_output)
    gpt_model.set_historia_input(prompt)
    gpt_model.set_usuario_id(usuario_id=current_user.id)
    db.session.add(gpt_model)
    db.session.commit()
    print(prompt)
    print("\n\n <<<<<------ " + str(prompt_instrucao.get_instrucoes(current_user.id)))
    smells = smell.text_to_get_smells(model="text-davinci-003", text=prompt, instrucoes=prompt_instrucao.get_instrucoes(current_user.id))
    resultado = {
        "historia": response.choices[0].text, "smell": smells.choices[0].text}
    id_smells = smell.get_id_smells(resultado["smell"])
    descricao_smells = smell.get_descricao_smells(resultado["smell"])
    gpt_has_smells.post_smells(id_smells, descricao_smells, gpt_model.id)
    return jsonify(resultado), 200


@gpt_blueprint.route("/gethistorias")
@helper.token_required
def get_historias(current_user):
    historias = Gpt.query.filter(Gpt.usuario_id == current_user.id)
    historias_json = []
    for historia in historias:
        historias_json.append({
            'id': historia.id,
            'UserStorie': historia.historia_input,
            'UserStoriePadronizada': historia.historia_output,
        })
    return jsonify(historias_json), 200
