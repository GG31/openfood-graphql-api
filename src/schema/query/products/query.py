import graphene


class Ingredient(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()


class Origin(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()


class Category(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()


class Product(graphene.ObjectType):
    name = graphene.String()
    brands = graphene.List(graphene.String)
    origins = graphene.List(Origin)
    categories = graphene.List(Category)
    ingredients = graphene.List(Ingredient)
    quantity = graphene.String()


class Products(graphene.ObjectType):
    products = graphene.List(Product)
    total = graphene.Int()

