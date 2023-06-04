from . import db

class Prompts(db.Model):
    __tablename__ = 'instrucao_prompt'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    instrucao = db.Column(db.String(5000))
    ativo = db.Column(db.Boolean)
    usuario_id = db.Column(db.Integer)

    def get_instrucao(self):
        return self.instrucao
    
    def set_instrucao(self, instrucao):
        self.instrucao = instrucao
    
    def get_ativo(self):
        return self.ativo
    
    def set_ativo(self, ativo):
        self.ativo = ativo

    def __repr__(self):
        return "id: " + self.id + " instrucao: " + self.instrucao + " ativo: " + self.ativo