from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from model.user import User
from controller.user_controller.controller import UserController
from flask_cors import CORS
from controller import helper
from model import db

user_blueprint = Blueprint('user_view', __name__, template_folder="templates")
CORS(user_blueprint)


user_controller = UserController()

@user_blueprint.route("/register", methods=["GET", "POST"])
def register_user():
    if request.method == 'POST':
        user_model = User()
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        if user_controller.filter_user_by_email(email) != None:
            return jsonify({'message': 'Este nome de usuario ja esta em uso'}), 401
        user_model.set_email(email)
        user_model.set_password(senha)
        user_model.set_nome(nome)
        db.session.add(user_model)
        db.session.commit()
        return render_template('register.html')
        
    return render_template('register.html')

@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return render_template("login.html")
    return render_template("login.html")

@user_blueprint.route("/auth", methods=["POST"])
def authenticate():
    return helper.auth()