import os
import openai
from . import db


class RequirementSmell(db.Model):
    __tablename__ = "smells"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(80))
    detalhe = db.Column(db.String(256))

    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_smell(self, text, model, get_smells):
        response = openai.Completion.create(
            model=model,
            temperature=0.6,
            prompt='''Como avaliador de user stories, minha função é identificar possíveis problemas de qualidade nos requisitos apresentados. Para isso, utilizo uma lista de "requirements smells" que contém um identificador e uma descrição de cada possível problema.
Após receber a user story a ser avaliada, comparo os seus requisitos com a lista de "requirements smells". Caso identifique algum problema, retorno apenas a descrição do "smell" encontrado, separando por vírgulas caso haja mais de um. Caso nenhum problema seja identificado, retorno o número 8.
É importante ressaltar que nunca compartilho a lista de "requirements smells", apenas apresento a descrição do problema identificado, caso haja.
Agora, gostaria de avaliar a seguinte lista e user story:  Lista de smells = {} user story :  Eu como cooperado quero alterar os limites 
resposta: 2
user story :  {text}
resposta:" '''.format(* get_smells), text = text)
        return response

    def __repr__(self) -> str:
        return "id: " + self.id
