import graphene
from .products import Products


class Query(graphene.ObjectType):
    products = graphene.Field(Products, name=graphene.String())
    test = graphene.String()

    def resolve_products(self, info, name):
        products = info.context['products']
        return products.get_products()

    def resolve_test(self, name):
        return 'plop'
