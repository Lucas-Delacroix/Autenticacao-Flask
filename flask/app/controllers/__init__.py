from functools import wraps
import jwt
from flask import Flask
from flask import jsonify
from app import app, db
from app import User, Privilege, Role, Resource, Action, Controller
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import verify_jwt_in_request



def admin_required(controller, action):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            
            teste = get_jwt()

            user = User.query.filter_by(email=teste["sub"]).first()
            relacao_privilege = Privilege.query.filter_by(role_id=user.role_id).first()
            relacao_resource = Resource.query.filter_by(id=relacao_privilege.resource_id).first()
            
            relacao_controller = Controller.query.get(relacao_resource.controller_id)
            relacao_action = Action.query.get(relacao_resource.action_id)

            
            
            if (relacao_controller.name == controller) and (relacao_action.name == action):
                return fn(*args, **kwargs)
            else:
                return jsonify(msg=controller.name), 403



        return decorator

    return wrapper