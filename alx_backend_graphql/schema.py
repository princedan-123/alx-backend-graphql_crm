import graphene

class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info, *args, **kwargs):
        return "Hello, GraphQL!"

schema = graphene.Schema(query=Query)