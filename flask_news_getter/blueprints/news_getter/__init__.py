from flask import Flask
from . import views


def init_app(app: Flask) -> None:
    app.register_blueprint(views.bp)
