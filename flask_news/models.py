from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime


Base = declarative_base()


class NewsModel(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)


class PageModel(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    news_site_id = Column(Integer, ForeignKey('news_sites.id'))

    def __str__(self) -> str:
        return self.name


class NewsSiteModel(Base):
    __tablename__ = 'news_sites'
    id = Column(Integer, primary_key=True)
    domain = Column(String, nullable=False)
    titles_selector = Column(String, nullable=False)
    urls_selector = Column(String, nullable=False)
    pages = relationship('PageModel')
