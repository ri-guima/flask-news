from flask.testing import FlaskClient


def test_index(client: FlaskClient) -> None:
    response = client.get(url_for('news_getter.index'))
    assert response.status_code == 200
