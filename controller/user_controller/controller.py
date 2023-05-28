from model.user import User
from model import db

class UserController:
    def insert(user: User):
        db.session.add(user)
        db.session.commit()
        return {"Status_code":200}
    
    def filter_user_by_email(self, email):
        try:
            return User.query.filter(User.email == email).one()
        except:
            return None