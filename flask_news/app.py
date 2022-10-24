from flask import Flask
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

from flask_news import FlaskNews


def create_app(testing: bool = False) -> Flask:
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.testing = testing
    load_dotenv('.env')
    db = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))
    FlaskNews(app, db)
    return app
