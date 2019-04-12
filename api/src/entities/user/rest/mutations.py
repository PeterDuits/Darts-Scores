from src.containers import Handlers, AWS as aws
from src.entities.user import commands
from src.entities.user.rest import schema
from src.http import responses
from src.http.utils import collect_errors
from src.http.errors import Error


@aws.LambdaProxy()
def user_create(event: aws.Event, _: dict):
    command = commands.UserCreateCommand(
        first_name=event.json('first_name'),
        last_name=event.json('last_name'),
        email=event.json('email'),
        password=event.json('password')
    )
    user, errors = Handlers.user_create().handle(command)

    schema_ = schema.UserSchema()
    data, schema_err = schema_.dump(user)

    return responses.Response(
        data,
        collect_errors(errors, schema_err)
    )
