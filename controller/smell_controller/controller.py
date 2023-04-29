from model.smell import RequirementSmell

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


    def resume_data(self):
        smell_json = self.get_all_smells()
        smell_list = []
        for i in smell_json:
            smell_list.append(str(i["id"]) + " " + i["nome"] + ": " + i["detalhe"])
        return smell_list

    def text_to_get_smells(self, prompt,  model):
        print(self.get_all_smells())
        return self.smell.get_smell(prompt, model, self.resume_data())
