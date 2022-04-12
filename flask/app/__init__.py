from flask import Flask
from flask_script import Manager, Server
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand 
#from flask.ext.hashing import Hashing 


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
#hashing = Hashing(app)

host = app.config["FLASK_HOST"]
port = app.config["FLASK_PORT"]
server = Server(host=host, port=port)

manager.add_command("runserver", server)
manager.add_command("db", MigrateCommand)


from app.models.user_model import User
from app.models.role_model import Role
from app.models.resource_model import Resource
from app.models.privilege_model import Privilege
from app.models.controller_model import Controller
from app.models.action_model import Action

from app.controllers import user_controller
from app.controllers import role_controller
from app.controllers import controller_controller
from app.controllers import action_controller
from app.controllers import resource_controller



