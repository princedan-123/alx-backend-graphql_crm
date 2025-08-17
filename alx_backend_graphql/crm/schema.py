import graphene
from graphene_django import DjangoObjectType
from .models import Customer, Product, Order
from graphql import GraphQLError
class Customer(DjangoObjectType):
    class Meta:
        model = Customer
        fields = '__all__'

class CreateCustomer(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String()
    
    success = graphene.String()
    customer = graphene.Field(Customer)

    def mutate(self, name, email, phone=None):
        """Creating a Customer"""
        #  validate email and phone number before saving it
        if Customer.objects.filter(email=email).exists():
            raise GraphQLError('Email already exists')
        
        customer = Customer.objects.create(
            name=name, email=email, phone=phone
            )
        return CreateCustomer(customer=customer, success='ok')