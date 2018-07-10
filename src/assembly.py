from .router import Router
from .hello import Hello
from .schema import schema
from .core import Logger
from .products import Products


class Assembly:
    def __init__(self, config):
        self.__config = config
        self.__init_instances()
        self.__init_router()

    def __init_instances(self):
        self.__logger = Logger(self.__config['logger']['level'])
        self.__hello = Hello(self.__config, self.__logger)
        self.__products = Products(self.__config, self.__logger)
        self.__schema = schema
        self.__router = Router(self.__config, self.__logger, self.__schema, self.__hello, self.__products)

    def __init_router(self):
        self.__app = self.__router.create_router()
        self.__app.config['ENV'] = self.__config['flask']['environment']
        self.__app.config['DEBUG'] = self.__config['flask'].getboolean('debug')

    def start(self):
        self.__app.run()

