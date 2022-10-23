from news_getter.domain import NewsSelector
from news_getter.adapters import NewsFinder


def test_news_getter(news_selector: NewsSelector) -> None:
    expected = json.load(open('tests/expected_news.json', 'r'))
    content = open('tests/test_content.html', 'r').read()
    assert NewsFinder(content, news_selector).findall() == expected
