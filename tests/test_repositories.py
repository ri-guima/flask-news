from flask_news.repositories import NewsSiteRepository


def test_news_site_repository() -> None:
    news_site = NewsSiteRepository().create(domain='https://www.devmedia.com.br', titles_selector='h3', urls_selector='a')
    assert NewsSiteRepository().all() == [news_site]


def test_news_site_repository_add_page() -> None:
    NewsSiteRepository().add_page(1, 'home')
    assert NewsSiteRepository().all()[0].pages == ['home']
