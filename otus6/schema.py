import graphene
from university.schema import Query as UniversityQuery
from custom_user.schema import Query as UserQuery, Mutation as UserMutation


class Query(UniversityQuery, UserQuery, graphene.ObjectType):
    pass


class Mutation(UserMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
