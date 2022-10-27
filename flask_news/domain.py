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


@dataclass
class NewsSite:
    domain: str
    pages: list[str]
    news_selector: NewsSelector


class INewsGetter(ABC):

    @abstractmethod
    def get_from(self, content: str) -> list[News]:
        raise NotImplementedError()


class INewsSiteRepository(ABC):

    @abstractmethod
    def create(self, domain: str, titles_selector: str, urls_selector: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def all(self) -> list[NewsSite]:
        raise NotImplementedError()
