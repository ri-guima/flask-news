import pytest
from flask import Flask
from flask.testing import FlaskClient

from flask_news.app import create_app
from flask_news.models import Base


@pytest.fixture(scope='module')
def app() -> Flask:
    app = create_app(testing=True)
    Base.metadata.drop_all(app.db)
    Base.metadata.create_all(app.db)
    yield app


@pytest.fixture(scope='module')
def client(app: Flask) -> FlaskClient:
    return app.test_client()
