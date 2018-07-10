import graphene


class Product(graphene.ObjectType):
    name = graphene.String()


class Products(graphene.ObjectType):
    products = graphene.List(Product)
    total = graphene.Int()

