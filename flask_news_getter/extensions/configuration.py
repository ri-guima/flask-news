from flask import Flask
from dynaconf import FlaskDynaconf


def init_app(app: Flask) -> None:
    FlaskDynaconf(app, extensions_list='EXTENSIONS')
