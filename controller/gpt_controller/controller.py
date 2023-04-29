from model.gpt import Gpt

class GptController:
    def __init__(self):
        self.gpt = Gpt()

    def text_to_completion(self, prompt, temperature, model, max_tokens):
        return self.gpt.completion(prompt, temperature, model, max_tokens)
