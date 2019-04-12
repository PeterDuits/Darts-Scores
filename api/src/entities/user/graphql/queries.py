import graphene

from src.containers import Handlers, Kernel
from src.entities.user import commands
from src.entities.user.graphql import docs, types
from src.graphql.types import Error
from src.http.utils import errors_to_graphql_errors
from src.services import auth
from src.services.wrappers import auth_self


class Queries(graphene.ObjectType):
    user = graphene.Field(types.UserPayload)

    def resolve_user(self, info):
        user_id = Kernel.auth().get_account_id()
        command = commands.UserCommand(id=user_id)

        user, errors = Handlers.user().handle(command)
        _errors = errors_to_graphql_errors(errors)

        return types.UserPayload(user, _errors)
