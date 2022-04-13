from functools import wraps
import jwt
from flask import Flask
from flask import jsonify
from app import app, db
from app import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import verify_jwt_in_request



def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            teste = get_jwt()
            user = User.query.filter_by(email=teste["sub"]).first()
            return jsonify({"email": user.email, "id": user.id, "role": user.role_id})


        return decorator

    return wrapper