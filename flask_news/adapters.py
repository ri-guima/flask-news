from bs4 import BeautifulSoup
from .domain import INewsGetter, News


class NewsGetter(INewsGetter):

    def findall(self, content: str) -> list[News]:
        soup = BeautifulSoup(content, 'lxml')
        titles = soup.select(self.__news_selector.titles_selector)
        urls = soup.select(self.__news_selector.urls_selector)
        return [News(titles[c].get_text(), urls[c]['href']) for c in range(len(titles))]
