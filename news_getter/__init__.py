from flask import Flask
from sqlalchemy.orm import Session, Engine


class NewsGetter:

    def __init__(self, app: Flask = None, db: Engine = None) -> None:
        if app is not None and db is not None:
            self.init_app(app, db)

    def init_app(self, app: Flask, db: Engine) -> None:
        app.news_getter = self
        app.db = db
        app.db_session = Session(db)
