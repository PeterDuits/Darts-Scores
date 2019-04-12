import logging

import graphene
from graphql import GraphQLError
from graphql.execution import ExecutionResult

from src.containers import Kernel, AWS as aws
from src.db import database
from src.graphql.schema import RootMutation, RootQuery
from src.http import responses


class Context:
    def __init__(self, session, claims: dict):
        self.session = session
        self.claims = claims

    def claim(self, key, default=None):
        return self.claims.get(key, default) or default


@aws.LambdaProxy()
@database.ScopedSession()
def handle_graphql(event: aws.Event, context: dict):
    schema = graphene.Schema(RootQuery, RootMutation)

    try:
        result = schema.execute(
            event.query_param('query') or event.json('query'),
            context_value=Context(
                session=Kernel.session(),
                claims=Kernel.auth().get_claims()
            ),
            variable_values=event.json('variables', {})
        )
    except Exception as e:
        logging.exception(e)
        result = ExecutionResult(errors=[e])

    return responses.Response(
        dict(data=result.data),
        result.errors,
        200  # Always return 200 for GraphQL responses
    )
