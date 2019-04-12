import graphene
import src.graphql.docs as docs


class Error(graphene.ObjectType):
    """Represents an error in the input."""
    title = graphene.String()
    detail = graphene.String()
