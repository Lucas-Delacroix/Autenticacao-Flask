import json
from app import app, db
from app import Controller
from flask import request, jsonify

@app.route("/controller/add", methods=["POST"])
def controller_add():
    data = request.get_json()

    if "name" not in data or data["name"] is None:
        return jsonify({"error":True, "message": "name não foi informado."}), 400
    
    controller = Controller(name=data["name"], resources=[])

    try:
        db.session.add(controller)
        db.session.commit()
        return jsonify({"error":False, "message": "Controller foi criado com sucesso."})
    
    except:
        db.session.rollback()
        return jsonify({"error":True, "message": "Erro ao criar controller, informações já existem no banco."}), 200


@app.route("/controller/list", methods=["GET"])
def controller_list():
    controllers = Controller.query.all()
    arr = []
    for controller in controllers:
        arr.append(controller.to_dict())
    return jsonify({"elements": arr, "error": False})


@app.route("/controller/edit/<int:id>", methods=["PUT"])
def controller_edit(id):
    data = request.get_json()
    controller = Controller.query.get(id)

    if controller == None:
        return jsonify({"message": "O controller informado não existe."})

    try:
        controller.name = data["name"]
        db.session.commit()
        return jsonify({"error": False, "message": "Controller editada com sucesso."})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao editar controller."}), 200


@app.route("/controller/delete/<int:id>", methods=["DELETE"])
def controller_delete(id):
    controller = Controller.query.get(id)

    if controller == None:
        return jsonify({"message": "O controller informada não existe."})

    try:
        db.session.delete(controller)
        db.session.commit()
        return jsonify({"error": False, "message": "Controller deletado com sucesso."})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao deletar controller."}), 200


@app.route("/controller/view/<int:id>", methods=["GET"])
def controller_view(id):
    controller = Controller.query.get(id)

    if controller == None:
        return jsonify({"message": "O Controller informada não existe."})

    try:
        return jsonify({"data": controller.to_dict(), "error": False})

    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao deletar controller."}), 200

