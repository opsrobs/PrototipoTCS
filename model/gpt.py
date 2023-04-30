import openai
import os
from . import db

class Gpt(db.Model):
    __tablename__ = 'historias'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    historia_input = db.Column(db.String(256))
    historia_output = db.Column(db.String(500))


    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def set_historia_input(self, historia_input):
        self.historia_input = historia_input
    
    def set_historia_output(self, historia_output):
        self.historia_output = historia_output

    def completion(self, prompt, temperature, model, max_tokens, frequency_penalty = 0, presence_penalty = 0):
        response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty)
        print(response)
        return response
    
    
    def __repr__(self) -> str:
        return "id: " + self.id