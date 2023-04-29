from . import db

class GptHasSmell(db.Model):
    __tablename__ = "gpt_has_smell"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id_gpt = db.Column(db.Integer)
    id_smell = db.Column(db.Integer)

    def __repr__(self):
        return "id_gpt: " + self.id_gpt + " id_smell: " + self.id_smell