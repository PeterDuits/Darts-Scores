import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.db import entities
from src.entities.user.graphql import docs
from src.graphql.types import Error


class User(SQLAlchemyObjectType):
    class Meta:
        model = entities.User
        exclude_fields = ['password', 'user_id']

    def resolve_id(self, info):
        return self.user_id


class UserCreateInput(graphene.InputObjectType):
    """Specifies the fields required to create a user."""
    first_name = graphene.String(
        required=True,
        description=docs.USER_FIRST_NAME
    )
    last_name = graphene.String(
        required=True,
        description=docs.USER_LAST_NAME
    )
    email = graphene.String(
        required=True,
        description=docs.USER_EMAIL
    )
    password = graphene.String(
        required=True,
        description=docs.USER_PASSWORD
    )


class UserAuthenticationInput(graphene.InputObjectType):
    """User authentication input."""
    email = graphene.String()
    password = graphene.String()


class UserPayload(graphene.ObjectType):
    user = graphene.Field(User)
    errors = graphene.List(Error)
