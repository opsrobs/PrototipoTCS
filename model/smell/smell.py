import os
import openai
from .. import db
from model.smell.prompt_default import *


class RequirementSmell(db.Model):
    __tablename__ = "smell"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(80))
    detalhe = db.Column(db.String(256))

    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_smell(self, text, model, get_smells, instrucoes):
        textvar=text
        prompt_text ='''{}/n{}/n Lista de smells possiveis de serem identificados: {}/n
        {}/n{}/n Resposta: '''.format(PROMPT_DEFAULT, instrucoes, get_smells, PROMPT_FINAL, textvar)
        response = openai.Completion.create(
            model=model,
            temperature=0.05,
            top_p=0.1,
            max_tokens= 256,
            prompt=prompt_text)
        print('PROMPT: ')
        print(prompt_text)
        print('USER STORIE: ')
        print(text)
        print('RESPONSE GPT: ')
        print(response)
        return response

    def __repr__(self) -> str:
        return "id: " + self.id + " nome: " + self.nome + " detalhe: " + self.detalhe
