import graphene
from graphene_django import DjangoObjectType
from .models import Customer, Product, Order
from graphql import GraphQLError
class Customer(DjangoObjectType):
    class Meta:
        model = Customer
        fields = '__all__'

def validate_phone(phone_number):
    """
    Validates a phone number format using a simple regex.
    Raises GraphQLError if the format is invalid.
    """
    phone_pattern = re.compile(r'^\+?[0-9\s-()]{7,20}$')
    if not phone_pattern.match(phone_number):
        raise GraphQLError("Invalid phone number format.")


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
        if phone is not None:
            validate_phone(phone)
        customer = Customer.objects.create(
            name=name, email=email, phone=phone
            )
        return CreateCustomer(customer=customer, success='ok')

class BulkCreateCustomers(graphene.Mutation):
    """Creates a list of customers."""
    class Arguments:
        customers = graphene.List(Customer, required=True)
    
    success = 'ok'
    
    def mutate(self, customers):
     
        