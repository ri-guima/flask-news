from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime


Base = declarative_base()


class NewsModel(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created_at = Column(Datetime, default=datetime.now(), nullable=False)


class NewsSiteModel(Base):
    __tablename__ = 'news_selectors'
    id = Column(Integer, primary_key=True)
    domain = Column(String, nullable=False)
    title_selector = Column(String, nullable=False)
    url_selector = Column(String, nullable=False)

    def __str__(self) -> str:
        return self.domain
