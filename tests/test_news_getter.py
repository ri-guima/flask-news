from flask_news.domain import NewsSelector
from flask_news.adapters import NewsGetter


def test_news_getter(news_selector: NewsSelector) -> None:
    expected = json.load(open('tests/expected_news.json', 'r'))
    content = open('tests/test_content.html', 'r').read()
    assert [vars(n) for n in NewsGetter(news_selector).get_from(content)] == expected
