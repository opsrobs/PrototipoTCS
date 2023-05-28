from model.user import User
from model import db

class UserController:
    def insert(user: User):
        db.session.add(user)
        db.session.commit()
        return {"Status_code":200}