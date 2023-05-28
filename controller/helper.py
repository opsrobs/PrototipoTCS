from config import SECRET_KEY
import datetime
from flask import jsonify, request
import jwt
from .user_controller.controller import UserController
from werkzeug.security import check_password_hash

user_controller = UserController()

def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"message":"Náo foi possivel verificar", "Authenticate":"Login Requiredð"}), 401
    
    user = user_controller.filter_user_by_email(auth.username)
    
    if not user: 
        return jsonify({"message": "usuario nao encontrado"}), 401
    
    if user and check_password_hash(user.password, auth.password):
        token = jwt.encode({'username': user.email, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)},
                           SECRET_KEY)
        return jsonify({'message': 'Validado com sucesso', 'token': token,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=1)})

    return jsonify({'message': 'Nao foi possivel verificar', 'Authenticate': 'login necessario"'}), 401