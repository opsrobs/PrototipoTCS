from . import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(80))
    password = db.Column(db.String(500))
    email = db.Column(db.String(80))

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def set_password(self, password):
        self.password = generate_password_hash(password) 
    
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def __repr__(self) -> str:
        return "id: " + self.id + " nome: " + self.nome + " email: " + self.email
