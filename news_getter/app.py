from flask import Flask
from news_getter.extensions import configuration


def create_app() -> Flask:
    app = Flask(__name__)
    configuration.init_app(app)
    return app
