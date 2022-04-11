import json
from app import app, db
from app import Role
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/role/add", methods=["POST"])
def role_add():
    data = request.get_json()

    if "name" not in data or data["name"] is None:
        return jsonify({"error":True, "message": "name não foi informado."}), 400
    
    role = Role(name=data["name"], users=[], privilegies=[])

    try:
        db.session.add(role)
        db.session.commit()
        return jsonify({"error":False, "message": "O usuário foi cadastrado com sucesso."})
    
    except:
        db.session.rollback()
        return jsonify({"error":True, "message": "Erro ao cadastrar usuário, informações já existem no banco."})
