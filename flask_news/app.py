from flask import Flask
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

from flask_news import FlaskNews


def create_app(testing: bool = False) -> Flask:
    app = Flask(__name__, static_folder='static', template_folder='templates')
    load_dotenv('.env')
    app.testing = testing
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    db = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))
    FlaskNews(app, db)
    return app
