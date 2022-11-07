from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class News:
    title: str
    url: str


@dataclass
class NewsSelector:
    titles_selector: str
    urls_selector: str


class NewsSite:

    def __init__(self, id: int, domain: str, news_selector: NewsSelector, pages: list[str] = []):
        self.id = id
        self.domain = domain
        self.news_selector = news_selector
        self.pages = pages


class INewsGetter(ABC):

    @abstractmethod
    def get_from(self, content: str) -> list[News]:
        raise NotImplementedError()


class INewsSiteRepository(ABC):

    @abstractmethod
    def create(self, domain: str, news_selector: NewsSelector) -> NewsSite:
        raise NotImplementedError()

    @abstractmethod
    def get(self, id: int) -> NewsSite:
        raise NotImplementedError()

    @abstractmethod
    def all(self) -> list[NewsSite]:
        raise NotImplementedError()

    @abstractmethod
    def add_page(self, id: int, name: str) -> None:
        raise NotImplementedError()
