import graphene

from src.containers import Handlers
from src.entities.user import commands
from src.entities.user.graphql import docs, types
from src.graphql.types import Error
from src.http.utils import errors_to_graphql_errors


class UserCreatePayload(graphene.Mutation):
    user = graphene.Field(types.User)
    errors = graphene.List(Error)

    class Arguments:
        input = types.UserCreateInput(
            required=True,
            description=docs.USER_CREATE_INPUT
        )

    def mutate(self, info, input: types.UserCreateInput):
        command = commands.UserCreateCommand(
            first_name=input.first_name,
            last_name=input.last_name,
            email=input.email,
            password=input.password
        )
        user, errors = Handlers.user_create().handle(command)
        _errors = errors_to_graphql_errors(errors)

        return UserCreatePayload(user=user, errors=_errors)


class UserAuthenticationPayload(graphene.Mutation):
    token = graphene.String(
        description=docs.AUTHENTICATION_PAYLOAD_TOKEN
    )
    errors = graphene.List(Error)

    class Arguments:
        input = types.UserAuthenticationInput(required=True)

    def mutate(self, info, input: types.UserAuthenticationInput):
        command = commands.UserAuthenticationCommand(
            email=input.email,
            password=input.password,
        )
        token, errors = Handlers.user_authentication().handle(command)
        _errors = errors_to_graphql_errors(errors)

        return UserAuthenticationPayload(token=token, errors=_errors)


class Mutations(graphene.ObjectType):
    user_create = UserCreatePayload.Field()
    user_authenticate = UserAuthenticationPayload.Field()
