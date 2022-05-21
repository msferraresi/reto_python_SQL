from werkzeug.utils import find_modules, import_string
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from config.swagger import template, swagger_config

db = SQLAlchemy()
ma = Marshmallow()

def create_app(environment=None):
    app = Flask(__name__)

    if environment is None:
        environment = 'development'
    app.config.from_pyfile('../config/{}.py'.format(environment))
        
    ma.init_app(app)
    db.init_app(app)
    
    Swagger(app, config=swagger_config, template=template)
    with app.app_context():
        register_blueprint(app)
        db.create_all()
        
    return app
    
def register_blueprint(app):
    for module in find_modules('src.services'):
        app.register_blueprint(import_string(module).app)