from model.smell.smell import RequirementSmell
import re

class SmellController:
    def __init__(self):
        self.smell = RequirementSmell()

    def get_all_smells(self):
        smells = self.smell.query.all()
        smell_json = []
        for smell in smells:
            smell_json.append({
                'id': smell.id,
                'nome': smell.nome,
                'detalhe': smell.detalhe
            })
        return smell_json

    def get_smell_by_id(self, id):
        smell = self.smell.query.get(id)
        smell_json = {"id": smell.id,
                      "nome": smell.nome}
        return smell_json

    def resume_data(self):
        smell_json = self.get_all_smells()
        smell_list = []
        for i in smell_json:
            smell_list.append(str(i["id"]) + " " + i["nome"] + ": " + i["detalhe"])
        return smell_list

    def text_to_get_smells(self, text,  model, instrucoes):
        print(self.get_all_smells())
        return self.smell.get_smell(text, model, self.resume_data(), instrucoes)
    
    def get_id_smells(self, text):
        numeros = re.findall(r'\[(\d+)\]', text)
        return [int(numero) for numero in numeros]

    def get_descricao_smells(self, text):
        return text.split('.', 1)[1].strip()
