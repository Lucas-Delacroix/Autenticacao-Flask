import json
from app import app, db
from app import Role
from flask import request, jsonify

@app.route("/role/add", methods=["POST"])
def role_add():
    data = request.get_json()

    if "name" not in data or data["name"] is None:
        return jsonify({"error":True, "message": "name não foi informado."}), 400
    
    role = Role(name=data["name"])

    try:
        db.session.add(role)
        db.session.commit()
        return jsonify({"error":False, "message": "Role foi criada com sucesso."})
    
    except:
        db.session.rollback()
        return jsonify({"error":True, "message": "Erro ao criar role, informações já existem no banco."}), 200


@app.route("/role/list", methods=["GET"])
def role_list():
    rolies = Role.query.all()
    arr = []
    for role in rolies:
        arr.append(role.to_dict())
    return jsonify({"elements": arr, "error": False})


@app.route("/role/edit/<int:id>", methods=["PUT"])
def role_edit(id):
    data = request.get_json()
    role = Role.query.get(id)

    if role == None:
        return jsonify({"error": True, "message": "A role informada não existe."})

    try:
        role.name = data["name"]
        db.session.commit()
        return jsonify({"error": False, "message": "Role editada com sucesso."})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao editar role."}), 200


@app.route("/role/delete/<int:id>", methods=["DELETE"])
def role_delete(id):
    role = Role.query.get(id)

    if role == None:
        return jsonify({"error": True, "message": "A role informada não existe."})

    try:
        db.session.delete(role)
        db.session.commit()
        return jsonify({"error": False, "message": "Role deletada com sucesso."})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao deletar role."}), 200


@app.route("/role/view/<int:id>", methods=["GET"])
def role_view(id):
    role = Role.query.get(id)

    if role == None:
        return jsonify({"error": True, "message": "A role informada não existe."})

    try:
        return jsonify({"data": role.to_dict(), "error": False})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao visualizar role."}), 200

