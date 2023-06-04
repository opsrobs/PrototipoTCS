from model.prompt import Prompts

class PromptInstrucao:
    def get_instrucoes(self, user_id):
        instrucoes = Prompts.query.filter(Prompts.usuario_id == user_id)
        return instrucoes
