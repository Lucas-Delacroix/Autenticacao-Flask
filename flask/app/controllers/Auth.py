import json
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from app import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import datetime
import jwt
from app.controllers.__init__ import resource





""" Criar endpoints chamados 1-Login, 2-Refresh Token, 3-Me """


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if "email" not in data or data["email"] is None:
        return jsonify({"error":True, "message": "O email não foi informado."}), 400
    if "password" not in data or data["password"] is None:
        return jsonify({"error":True, "message": "A senha não foi informada."}), 400
    

    #hash_senha = generate_password_hash(data["password"], method='sha256')

    user = User.query.filter_by(email=data["email"]).first_or_404()

    if check_password_hash(user.password, data["password"]) == False:
        return jsonify({"error": True, "message": "Senha digitada está incorreta."})
    
    access_token = create_access_token(identity=user.email)
    refresh_token = create_refresh_token(identity=user.email)

    return jsonify(access_token=access_token, refresh_token=refresh_token, messagem="Seu login foi efetuado com sucesso. Seu token de acesso foi gerado.")


@app.route("/me", methods=["GET"])
@jwt_required()
def me():
    user_logado = get_jwt_identity()
    return jsonify(usuario_logado=user_logado), 200

@app.route("/protegido", methods=["GET"])
@resource(controller="Admin", action="ADD")
def protegido():
    return jsonify({"msg": "Você está vendo uma mensagem protegida."})

@app.route("/refresh-token", methods=["POST"])
@jwt_required(refresh=True)
def refresh_token():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)

