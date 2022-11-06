from flask import current_app as app

from .domain import INewsSiteRepository, NewsSelector
from .models import NewsSiteModel, PageModel


class NewsSiteRepository(INewsSiteRepository):

    def create(self, domain: str, news_selector: NewsSelector) -> None:
        news_site = NewsSiteModel(
            domain=domain, titles_selector=news_selector.titles_selector,
            urls_selector=news_selector.urls_selector)
        app.db_session.add(news_site)
        app.db_session.commit()

    def all(self) -> list[str]:
        return [str(m) for m in app.db_session.query(NewsSiteModel).all()]

    def add_page(self, id: int, name: str) -> None:
        news_site = app.db_session.query(NewsSiteModel).get(id)
        news_site.pages.append(PageModel(name=name))
        app.db_session.commit()
