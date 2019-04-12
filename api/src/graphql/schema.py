import graphene

import src.config.graphql as grapql


class RootQuery(*grapql.queries, graphene.ObjectType):
    pass


class RootMutation(*grapql.mutations, graphene.ObjectType):
    pass
