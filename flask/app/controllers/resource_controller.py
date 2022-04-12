import json
from app import app, db
from app import Resource
from flask import request, jsonify

@app.route("/resource/add", methods=["POST"])
def resource_add():
    data = request.get_json()

    if "action_id" not in data or data["action_id"] is None:
        return jsonify({"error":True, "message": "action_id não foi informado."}), 400
    if "controller_id" not in data or data["controller_id"] is None:
        return jsonify({"error":True, "message": "controller_id não foi informado."}), 400
    
    resource = Resource(action_id=data["action_id"], controller_id=data["controller_id"], privilegies=[])

    try:
        db.session.add(resource)
        db.session.commit()
        return jsonify({"error":False, "message": "resource foi criado com sucesso."})
    
    except:
        db.session.rollback()
        return jsonify({"error":True, "message": "Erro ao criar resource, informações já existem no banco."}), 200


@app.route("/resource/list", methods=["GET"])
def resource_list():
    resources = Resource.query.all()
    arr = []
    for resource in resources:
        arr.append(resource.to_dict())
    return jsonify({"elements": arr, "error": False})


@app.route("/resource/edit/<int:id>", methods=["PUT"])
def resource_edit(id):
    data = request.get_json()
    resource = Resource.query.get(id)

    if resource == None:
        return jsonify({"error": True, "message": "O resource informado não existe."})

    try:
        if "action_id" in data:
            resource.action_id = data["action_id"]
        if "controller_id" in data:
            resource.controller_id = data["controller_id"]
        
        db.session.commit()
        return jsonify({"error": False, "message": "Resource editada com sucesso."})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao editar resource."}), 200


@app.route("/resource/delete/<int:id>", methods=["DELETE"])
def resource_delete(id):
    resource = Resource.query.get(id)

    if resource == None:
        return jsonify({"error": True, "message": "A resource informada não existe."})

    try:
        db.session.delete(resource)
        db.session.commit()
        return jsonify({"error": False, "message": "Resource deletado com sucesso."})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao deletar resource."}), 200


@app.route("/resource/view/<int:id>", methods=["GET"])
def resource_view(id):
    resource = Resource.query.get(id)

    if resource == None:
        return jsonify({"error": True, "message": "O resource informada não existe."})

    try:
        return jsonify({"data": resource.to_dict(), "error": False})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao visualizar resource."}), 200
