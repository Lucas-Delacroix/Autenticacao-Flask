import json
from app import app, db
from app import Privilege
from flask import request, jsonify

@app.route("/privilege/add", methods=["POST"])
def privilege_add():
    data = request.get_json()

    if "role_id" not in data or data["role_id"] is None:
        return jsonify({"error":True, "message": "role_id não foi informado."}), 400
    
    if "resource_id" not in data or data["resource_id"] is None:
        return jsonify({"error":True, "message": "resource_id não foi informado."}), 400

    if "allow" not in data or data["allow"] is None:
        return jsonify({"error":True, "message": "Allow não foi informado."}), 400
    
    privilege = Privilege(role_id=data["role_id"], resource_id=data["resource_id"], allow=data["allow"] )

    try:
        db.session.add(privilege)
        db.session.commit()
        return jsonify({"error":False, "message": "Privilege foi criado com sucesso."})
    
    except:
        db.session.rollback()
        return jsonify({"error":True, "message": "Erro ao criar privilege, verifique as informações inseridas."}), 200


@app.route("/privilege/list", methods=["GET"])
def privilege_list():
    privileges = Privilege.query.all()
    arr = []
    for privilege in privileges:
        arr.append(privilege.to_dict())
    return jsonify({"elements": arr, "error": False})


@app.route("/privilege/edit/<int:role_id>/<int:resource_id>", methods=["PUT"])
def privilege_edit(role_id, resource_id):
    data = request.get_json()
    privileges = Privilege.query.filter_by(role_id=role_id, resource_id=resource_id)

    if privileges == None:
        return jsonify({"error": True, "message": "O privilege informado não existe."})
    
    arr = []
    for privilege in privileges:
        arr.append(privilege.to_dict()) 

    try:
        if "role_id" in data:
            privilege.role_id = data["role_id"]
        
        if "resource_id" in data:
            privilege.resource_id = data["resource_id"]
        
        if "allow" in data:
            privilege.allow = data["allow"]

        db.session.commit()
        return jsonify({"error": False, "message": "Privilege editada com sucesso."})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao editar privilege."}), 200


@app.route("/privilege/delete/<int:role_id>/<int:resource_id>", methods=["DELETE"])
def privilege_delete(role_id, resource_id):
    privileges = Privilege.query.filter_by(role_id=role_id, resource_id=resource_id)

    if privileges == None:
        return jsonify({"error": True, "message": "A privilege informada não existe."})
    
    arr = []
    for privilege in privileges:
        arr.append(privilege.to_dict()) 

    try:
        db.session.delete(privilege)
        db.session.commit()
        return jsonify({"error": False, "message": "Privilege deletado com sucesso."})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao deletar privilege."}), 200


@app.route("/privilege/view/<int:role_id>/<int:resource_id>", methods=["GET"])
def privilege_view(role_id, resource_id):
    privileges = Privilege.query.filter_by(role_id=role_id, resource_id=resource_id)
    
    if privileges == None:
        return jsonify({"error": True, "message": "O privilege informada não existe."})
    
    arr = []
    for privilege in privileges:
        arr.append(privilege.to_dict()) 


    try:
        return jsonify({"data": privilege.to_dict(), "error": False})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao visualizar privilege. Verifique se as informações inseridas estão corretas."}), 200

