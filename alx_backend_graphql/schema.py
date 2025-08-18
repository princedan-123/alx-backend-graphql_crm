import graphene
from crm.schema import Query as CRMQuery, Mutation as CRMMutation

class Query(CRMQuery, graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info, *args, **kwargs):
        return "Hello, GraphQL!"

schema = graphene.Schema(query=Query)