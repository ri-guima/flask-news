from flask import current_app as app

from .domain import INewsSiteRepository


class NewsSiteRepository(INewsSiteRepository):

    def all(self) -> list[str]:
        return [str(m) for m in app.db_session.query(NewsSiteModel).all()]

