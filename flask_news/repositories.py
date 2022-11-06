from flask import current_app as app

from .domain import INewsSiteRepository, NewsSite, NewsSelector
from .models import NewsSiteModel, PageModel


class NewsSiteRepository(INewsSiteRepository):

    def create(self, domain: str, news_selector: NewsSelector) -> NewsSite:
        app.db_session.add(NewsSiteModel(
            domain=domain, titles_selector=news_selector.titles_selector,
            urls_selector=news_selector.urls_selector))
        app.db_session.commit()
        return NewsSite(domain, news_selector)

    def get(self, id: int) -> NewsSite:
        m = app.db_session.query(NewsSiteModel).get(id)
        news_selector = NewsSelector(m.titles_selector, m.urls_selector)
        return NewsSite(m.domain, news_selector, [str(p) for p in m.pages])

    def all(self) -> list[NewsSite]:
        result = []
        for m in app.db_session.query(NewsSiteModel).all():
            news_selector = NewsSelector(m.titles_selector, m.urls_selector)
            result.append(NewsSite(m.domain, news_selector))
        return result

    def add_page(self, id: int, name: str) -> None:
        news_site = app.db_session.query(NewsSiteModel).get(id)
        news_site.pages.append(PageModel(name=name))
        app.db_session.commit()
