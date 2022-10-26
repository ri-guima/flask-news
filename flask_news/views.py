from flask import Blueprint, Response, render_template, redirect, url_for


bp = Blueprint('flask_news', __name__, template_folder='templates', static_folder='static')


@bp.get('/')
def index() -> Response:
    return render_template('flask_news/index.html')


@bp.get('/add-news')
def add_news_get() -> Response:
    return render_template('flask_news/add_news.html')


@bp.post('/add-news')
def add_news_post() -> Response:
    return redirect(url_for('.add_news_get'))
