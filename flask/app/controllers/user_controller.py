import json
from app import app, db
from app import User
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/user/add", methods=["POST"])
def user_add():
    data = request.get_json()

    if "email" not in data or data["email"] is None:
        return jsonify({"error":True, "message": "O email não foi informado."}), 400
    if "password" not in data or data["password"] is None:
        return jsonify({"error":True, "message": "A senha não foi informada."}), 400
    
    hash_senha = generate_password_hash(data["password"], method='sha256')
    user = User(email=data["email"], password=hash_senha, role_id=data["role_id"])

    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({"error":False, "message": "O usuário foi cadastrado com sucesso."})
    
    except:
        db.session.rollback()
        return jsonify({"error":True, "message": "Erro ao cadastrar usuário, informações já existem no banco."})


#@app.route("/user/edit/<int:id>", methods=["PUT"])
#def user_edit(id):



