from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class News:
    title: str
    url: str
    created_at: datetime = datetime.now()


@dataclass
class NewsSelector:
    titles_selector: str
    urls_selector: str


class INewsGetter(ABC):

    def __init__(self, news_selector: NewsSelector) -> None:
        self.__news_selector = news_selector

    @abstractmethod
    def get_from(self, content: str) -> list[News]:
        raise NotImplementedError()
