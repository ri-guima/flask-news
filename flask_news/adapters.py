from bs4 import BeautifulSoup
from .domain import INewsGetter, News, NewsSelector


class NewsGetter(INewsGetter):

    def __init__(self, news_selector: NewsSelector) -> None:
        self.__news_selector = news_selector

    def get_from(self, content: str) -> list[News]:
        soup = BeautifulSoup(content, 'lxml')
        titles = soup.select(self.__news_selector.titles_selector)
        urls = soup.select(self.__news_selector.urls_selector)
        return [News(titles[c].get_text(), urls[c]['href']) for c in range(len(titles))]
