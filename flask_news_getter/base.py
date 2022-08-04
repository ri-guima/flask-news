from flask import Flask
from importlib import import_module

from flask_news_getter.extensions import configuration


class NewsGetter:

    def __init__(self, app: Flask=None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(app: Flask) -> None:
        configuration.init_app(app)
