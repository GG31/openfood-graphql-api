from ..core import Object


class Products:
    def __init__(self, config, logger, db):
        self.__config = config
        self.__logger = logger
        self.__collection = db[self.__config['databases']['collection']]

    def get_products(self, **kwargs):
        query = {}
        if 'barcode' in kwargs:
            query['code'] = kwargs['barcode']
        if 'origin' in kwargs:
            query['origins'] = { '$regex': u'.*' + kwargs['origin'] + '.*' }
        if 'brand' in kwargs:
            query['brands'] = { '$regex': u'.*' + kwargs['brand'] + '.*' }
        if 'category' in kwargs:
            query['categories'] = { '$regex': u'.*' + kwargs['category'] + '.*' }
        cursor = self.__collection.find(query, skip=kwargs['after'], limit=kwargs['first'])
        result = [Products.format_product(product) for product in cursor]
        count = self.__collection.count(query)
        result = Object(products=result, total=count)
        return result

    @staticmethod
    def format_product(product):
        formatted_product = Object()
        if 'product_name' in product:
            formatted_product.name = product['product_name']
        if 'ingredients' in product:
            ingredients = [Object(id=ingredient['id'], name=ingredient['text']) for ingredient in product['ingredients']]
            formatted_product.ingredients = ingredients
        if 'origins' in product:
            formatted_product.origins = product['origins'].split(',')
        if 'brands' in product:
            formatted_product.brands = product['brands'].split(',')
        if 'categories' in product:
            formatted_product.categories = product['categories'].split(',')
        if 'quantity' in product:
            formatted_product.quantity = product['quantity']

        return formatted_product
