from . import db

class GptHasSmell(db.Model):
    __tablename__ = "gpt_has_smell"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id_gpt = db.Column(db.Integer)
    id_smell = db.Column(db.Integer)
    descricao_smell = db.Column(db.String(5000))

    def set_id_gpt(self, id_gpt):
        self.id_gpt = id_gpt
    
    def set_id_smell(self, id_smell):
        self.id_smell = id_smell

    def set_descricao_smell(self, descricao_smell):
        self.descricao_smell = descricao_smell

    def __repr__(self):
        return "id: " + self.id + " id_gpt: " + self.id_gpt + " id_smell: " + self.id_smell + " descricao_smell: " + self.descricao_smell