from model.smell import RequirementSmell

class SmellController:
    def __init__(self):
        self.smell = RequirementSmell()

    def text_to_get_smells(self, prompt,  model):
        return self.smell.get_smell(prompt, model)
