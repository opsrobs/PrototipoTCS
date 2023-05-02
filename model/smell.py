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
        messages=[{ "role": "user", "content": '''Below, various requirements smells will be listed. Compare them with the user story that will be given and return the numbers corresponding to the identified requirements smells in the story. If none are found, respond with the corresponding number listed above that indicates without smells.
                {}
                Storie: '''.format(* get_smells) + prompt }])
        return response
    
    def __repr__(self) -> str:
        return "id: " + self.id