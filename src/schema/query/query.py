import graphene
from .products import Products


class Query(graphene.ObjectType):
    products = graphene.Field(
        Products,
        first=graphene.Int(default_value=10),
        after=graphene.Int(default_value=0)
    )

    def resolve_products(self, info, first, after):
        products = info.context['products']
        return products.get_products(first, after)
