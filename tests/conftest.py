import pytest
from flask import Flask
from flask.testing import FlaskClient

from news_getter.app import create_app


@pytest.fixture(scope='module')
def app() -> Flask:
    app = create_app(testing=True)
    yield app


@pytest.fixture(scope='module')
def client(app: Flask) -> FlaskClient:
    return app.test_client()
