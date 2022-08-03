from flask import Flask
from flask_bootstrap import Bootstrap


def init_app(app: Flask) -> None:
    Bootstrap(app)
