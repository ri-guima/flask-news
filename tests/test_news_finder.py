from flask_news.domain import NewsSelector
from flask_news.adapters import NewsFinder


def test_news_finder(news_selector: NewsSelector) -> None:
    expected = json.load(open('tests/expected_news.json', 'r'))
    content = open('tests/test_content.html', 'r').read()
    assert NewsFinder(content, news_selector).findall() == expected
