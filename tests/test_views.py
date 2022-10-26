from flask import url_for
from flask.testing import FlaskClient


def test_index(client: FlaskClient) -> None:
    response = client.get(url_for('flask_news.index'))
    assert response.status_code == 200


def test_add_news_get(client: FlaskClient) -> None:
    response = client.get(url_for('flask_news.add_news_get'))
    assert response.status_code == 200


def test_add_news_post(client: FlaskClient) -> None:
    response = client.post(url_for('flask_news.add_news_post'))
    assert response.status_code == 302
