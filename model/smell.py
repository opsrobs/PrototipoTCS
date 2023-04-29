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
    
    def get_smell(self, prompt, model):
        response = openai.ChatCompletion.create(
        model=model,
        messages=[{ "role": "product Owner", "message": '''Answer the storie below based on this parameters, answer with only the numbers correspondents to the storie
                1 gaps factor: is characterized by scenarios that have one or more optional actions in the story.
                2 incomplete references: occurs when artifacts such as complementary story content, such as documentation, technical terms or laws, are mentioned, but the references to these contents are not available or incomplete.
                3 problem orientation:  refers to the scenario in which a story presents only the problem by specifying it without any solution.
                4 comparative, superlative, and subjective language:  present specifications in comparison or subjective interpretations of the user's needs.
                5 ambiguity: can arise from the lack of verification of words that are not specific by nature and tend to cause more than one interpretation and make parameterization difficult.
                6 The conflict: occurs when two or more requirements cause inconsistencies between them.
                7 testable: is detected in the absence or inaccuracy of the parameters specified in the stories that make it impossible to create metrics or parameters for testing.
                8 Without errors!
                Storie: ''' + prompt }])
        return response
    
    def __repr__(self) -> str:
        return "id: " + self.id