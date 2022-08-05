from flask import Flask


class NewsGetter:

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(app: Flask) -> None:
        extensions = [
            'flask_news_getter.extensions.appearence:init_app',
            'flask_news_getter.blueprints.news_getter:init_app',
        ]
        app.config['EXTENSIONS'].extend(extensions)
