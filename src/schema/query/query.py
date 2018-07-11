import graphene
from .products import Products


class Query(graphene.ObjectType):
    products = graphene.Field(
        Products,
        first=graphene.Int(default_value=10),
        after=graphene.Int(default_value=0),
        barcode=graphene.String(required=False),
        origin=graphene.String(required=False),
        brand=graphene.String(required=False),
    )

    def resolve_products(self, info, **kwargs):
        products = info.context['products']
        return products.get_products(**kwargs)
