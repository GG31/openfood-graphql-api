from flask import Flask
from flask_graphql import GraphQLView


class Router:
    def __init__(self, config, logger, schema, hello, products):
        self.__config = config
        self.__logger = logger.get_logger(__name__)
        self.__schema = schema
        self.__hello = hello
        self.__products = products

    def create_router(self):
        this = self
        app = Flask(self.__config['project']['name'])

        app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=self.__schema, graphiql=True, context={ 'products': self.__products }))

        @app.route('/')
        @app.route('/<username>')
        def hello(username='Bob'):
            this.__logger.info('/ called')
            return '%s %s' % (this.__hello.say_hello(), username)

        return app
