from ..core import Object

class Products:
    def __init__(self, config, logger):
        self.__config = config
        self.__logger = logger

    def get_products(self):
        p1 = Object(name='p1', age=9)
        p2 = Object(name='p2', age=8)
        result = Object(products=[p1, p2], total=2)
        return result
