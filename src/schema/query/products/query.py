import graphene


class Ingredient(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()


class Product(graphene.ObjectType):
    name = graphene.String()
    origin = graphene.String()
    brand = graphene.String()
    ingredients = graphene.List(Ingredient)


class Products(graphene.ObjectType):
    products = graphene.List(Product)
    total = graphene.Int()

