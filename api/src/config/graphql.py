from src.entities.user.graphql.queries import Queries as UserQueries
from src.entities.user.graphql.mutations import Mutations as UserMutations


# Register query classes here
queries = (
    UserQueries,
)

# Register mutation classes here
mutations = (
    UserMutations,
)
