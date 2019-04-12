from flask import Blueprint, request

from src.containers import AWS as aws
from src.entities.user.rest.mutations import user_create

api = Blueprint('rest_v1', __name__)


@api.route('/hello', methods=['GET'])
@aws.FlaskApiGatewayEvent(request)
def handle_hello(event, context):
    return 'Hello World!'


@api.route('/users', methods=['POST'])
@aws.FlaskApiGatewayEvent(request)
def handle_user_create(event, context):
    return user_create(event, context)
