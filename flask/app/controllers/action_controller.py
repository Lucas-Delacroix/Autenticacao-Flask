import json
from app import app, db
from app import Action
from flask import request, jsonify

@app.route("/action/add", methods=["POST"])
def action_add():
    data = request.get_json()

    if "name" not in data or data["name"] is None:
        return jsonify({"error":True, "message": "name não foi informado."}), 400
    
    action = Action(name=data["name"], resources=[])

    try:
        db.session.add(action)
        db.session.commit()
        return jsonify({"error":False, "message": "Action foi criado com sucesso."})
    
    except:
        db.session.rollback()
        return jsonify({"error":True, "message": "Erro ao criar Action, informações já existem no banco."}), 200


@app.route("/action/list", methods=["GET"])
def action_list():
    actions = Action.query.all()
    arr = []
    for action in actions:
        arr.append(action.to_dict())
    return jsonify({"elements": arr, "error": False})


@app.route("/action/edit/<int:id>", methods=["PUT"])
def action_edit(id):
    data = request.get_json()
    action = Action.query.get(id)

    if action == None:
        return jsonify({"error": True, "message": "O action informado não existe."})

    try:
        action.name = data["name"]
        db.session.commit()
        return jsonify({"error": False, "message": "Action editada com sucesso."})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao editar action."}), 200


@app.route("/action/delete/<int:id>", methods=["DELETE"])
def action_delete(id):
    action = Action.query.get(id)

    if action == None:
        return jsonify({"error": True, "message": "A action informada não existe."})

    try:
        db.session.delete(action)
        db.session.commit()
        return jsonify({"error": False, "message": "Action deletado com sucesso."})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao deletar action."}), 200


@app.route("/action/view/<int:id>", methods=["GET"])
def action_view(id):
    action = Action.query.get(id)

    if action == None:
        return jsonify({"error": True, "message": "O action informada não existe."})

    try:
        return jsonify({"data": action.to_dict(), "error": False})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao visualizar action."}), 200

