from flask_news.domain import NewsSite
from flask_news.adapters import NewsFinder


def test_news_finder(news_site: NewsSite) -> None:
    expected = json.load(open('tests/expected_news.json', 'r'))
    content = open('tests/test_content.html', 'r').read()
    assert NewsFinder(content, news_selector).findall() == expected
