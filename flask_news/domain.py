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


class INewsGetter(ABC):

    @abstractmethod
    def get_from(self, content: str) -> list[News]:
        raise NotImplementedError()
