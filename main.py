# Third-party library
from flask import Flask
from flask_restplus import Api
from flask_cors import CORS

#blue print
from api import api_blueprint
from api.models.database import db

api = Api(api_blueprint, doc=False)

# function to create app
def create_app(config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    app.register_blueprint(api_blueprint)
    app.url_map.strict_slashes = False

    #bind app to db
    db.init_app(app)

    return app
