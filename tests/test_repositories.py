from flask import Flask

from flask_news.repositories import NewsSiteRepository
from flask_news.domain import NewsSelector


def test_news_site_repository(app: Flask) -> None:
    with app.app_context():
        news_site = NewsSiteRepository().create(
            'https://www.devmedia.com.br', NewsSelector('h3', 'a'))
        assert (NewsSiteRepository().get(1).domain ==
                'https://www.devmedia.com.br')
        assert len(NewsSiteRepository().all()) == 1


def test_news_site_repository_add_page(app: Flask) -> None:
    with app.app_context():
        NewsSiteRepository().add_page(1, 'home')
        assert NewsSiteRepository().get(1).pages == ['home']
