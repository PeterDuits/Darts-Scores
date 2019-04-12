from flask import Blueprint, request

from src.containers import AWS as aws
from src.handlers import handle_graphql

api = Blueprint('graphql', __name__)


@api.route('', methods=['POST', 'GET'])
@aws.FlaskApiGatewayEvent(request)
def handle(event, context):
    return handle_graphql(event, context)
