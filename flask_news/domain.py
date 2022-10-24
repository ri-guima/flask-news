from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class News:
    title: str
    url: str
    created_at: datetime


@dataclass
class NewsSite:
    domain: str
    pages: list[str]
    title_selector: str
    url_selector: str


class INewsFinder(ABC):

    def __init__(self, content: str, news_selector: NewsSelector) -> None:
        self.__content = content
        self.__news_selector = news_selector

    @abstractmethod
    def findall(self) -> list[News]:
        raise NotImplementedError()
