import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(description="A hello message")

    def resolve_hello(root, info, **args):
        return "Hello, GraphQL!"

schema = graphene.Schema(query=Query)