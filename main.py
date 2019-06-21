# Third-party library
from flask import Flask, jsonify
from flask_restplus import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager


#blue print
from api import api_blueprint
from api.middlewares.base_validator import middleware_blueprint, ValidationError
from api.models.database import db

api = Api(api_blueprint, doc='/docs')


def initialize_error_handlers(application):
    """Initialize error handlers"""
    application.register_blueprint(middleware_blueprint)
    application.register_blueprint(api_blueprint)


# function to create app
def create_app(config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    app.url_map.strict_slashes = False

    # error handlers
    initialize_error_handlers(app)

    # initialise JWT
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def my_expired_token_callback(expired_token):
        token_type = expired_token['type']
        return jsonify({
            'status': 401,
            'sub_status': 42,
            'msg': 'The {} token has expired'.format(token_type)
        }), 401

    #bind app to db
    db.init_app(app)

    #import models
    import api.models

    # import views
    import api.views

    return app


@api.errorhandler(ValidationError)
@middleware_blueprint.app_errorhandler(ValidationError)
def handle_exception(error):
    """Error handler called when a ValidationError Exception is raised"""

    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

