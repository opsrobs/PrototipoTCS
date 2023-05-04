import os
import openai
from . import db

class RequirementSmell(db.Model):
    __tablename__ =  "smells"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(80))
    detalhe = db.Column(db.String(256))

    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
    
    def get_smell(self, prompt, model, get_smells):
        response = openai.ChatCompletion.create(
        model=model,
        temperature=1,
        messages=[{ "role": "user", "content": '''Suponhamos que você é um avaliador de user stories e você é bastante critico no que diz respeito a requirements smells. Sempre que lhe é informada uma user storie você consulta uma lista de requirements smells que contem um id e os detalhes dos requirements. A partir dessa lista você compara a lista com a user storie enviada. Após ter feito a comparação retorne o id do smell que está presente e caso haja mais de um apresente os ids separados por virgula. caso não haja nenhum você retorna 8. Como avaliador foi lhe passada a seguinte lista + user storie:
                Storie: '''.format(* get_smells) + prompt }])
        return response
    
    def __repr__(self) -> str:
        return "id: " + self.id