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
Após receber a user story a ser avaliada, comparo os seus requisitos com a lista de "requirements smells". Caso identifique algum problema, retorno a descrição do "smell" encontrado trazendo detalhes, separando por vírgulas caso haja mais de um. Caso nenhum problema seja identificado, retorne "Não houveram smells identificados".
É importante ressaltar que nunca compartilho a lista de "requirements smells", apenas apresento a descrição do problema identificado, caso haja.
Agora, gostaria de avaliar a seguinte lista e user story:  Lista de smells = {} : user story :  Eu como cooperado quero alterar os limites 
resposta: "Incomplete references" refere-se a referências ou termos não definidos ou incompletos em uma User Story. Isso pode causar confusão e dificuldade na compreensão dos requisitos. Para evitar esse problema, é importante garantir que todas as referências e termos utilizados sejam claramente definidos e compreendidos por todos os membros da equipe de desenvolvimento. Isso pode ser alcançado através de uma comunicação clara e do esclarecimento de dúvidas para garantir um entendimento comum dos requisitos.
user story : como um desenvovedor, quero que uma user sotrie seja formatada quando eu clicar no botão submit
resposta: '''.format(* get_smells, text))
        return response

    def __repr__(self) -> str:
        return "id: " + self.id + " nome: " + self.nome + " detalhe: " + self.detalhe
