import graphene

class Mutation(graphene.ObjectType):
    name = graphene.String()
    