from flask import Flask
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from .views import bp


class NewsGetter:

    def __init__(self, app: Flask = None, db: Engine = None) -> None:
        if app is not None and db is not None:
            self.init_app(app, db)

    def init_app(self, app: Flask, db: Engine) -> None:
        app.news_getter = self
        app.db = db
        app.db_session = Session(db)
        app.register_blueprint(bp)
