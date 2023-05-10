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
        print(text)
        response = openai.Completion.create(
            model=model,
            temperature=0.6,
            #max_tokens: 256,
            prompt='''Você receberá um conjunto de User Stories (histórias do usuário) e uma lista de "smells" (problemas) comuns encontrados em requisitos de software. Seu objetivo é identificar se cada User Story contém algum "smell" que corresponda à lista fornecida.

Aqui está o formato esperado para a avaliação:

User Story:
[Descrição da User Story]

Smells Encontrados:
[Lista de "smells" presentes na User Story, separados por vírgula]

Se você identificar algum "smell" presente na User Story, enumere-o na seção "Smells Encontrados". Caso contrário, deixe a seção "Smells Encontrados" em branco.

Lembre-se de que cada User Story pode conter mais de um "smell", portanto, verifique cuidadosamente cada uma delas.

Aqui está a lista de "smells" a serem avaliados: {}, user story :  Eu como cooperado quero alterar os limites 
resposta: "Incomplete references" refere-se a referências ou termos não definidos ou incompletos em uma User Story. Isso pode causar confusão e dificuldade na compreensão dos requisitos. Para evitar esse problema, é importante garantir que todas as referências e termos utilizados sejam claramente definidos e compreendidos por todos os membros da equipe de desenvolvimento. Isso pode ser alcançado através de uma comunicação clara e do esclarecimento de dúvidas para garantir um entendimento comum dos requisitos;
user story : {}
resposta: '''.format(* get_smells, text))
        return response

    def __repr__(self) -> str:
        return "id: " + self.id + " nome: " + self.nome + " detalhe: " + self.detalhe
