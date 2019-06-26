from flask import Blueprint

print('I got to blueprint')
api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api/v1')

print('______>>>>>>>>>>>_____', api_blueprint)