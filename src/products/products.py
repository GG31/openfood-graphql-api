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
            query['origins'] = kwargs['origin']
        if 'brand' in kwargs:
            query['brands'] = kwargs['brand']
        cursor = self.__collection.find(query, skip=kwargs['after'], limit=kwargs['first'])
        result = [Products.format_product(product) for product in cursor]
        result = Object(products=result, total=len(result))
        return result

    @staticmethod
    def format_product(product):
        print(product)
        formatted_product = Object()
        if 'product_name' in product:
            formatted_product.name = product['product_name']
        if 'ingredients' in product:
            ingredients = [Object(id=ingredient['id'], name=ingredient['text']) for ingredient in product['ingredients']]
            formatted_product.ingredients = ingredients
        if 'origins' in product:
            formatted_product.origin = product['origins']
        if 'brands' in product:
            formatted_product.brand = product['brands']

        return formatted_product
