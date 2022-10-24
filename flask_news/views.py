from flask import Blueprint, Response, render_template, redirect, url_for


bp = Blueprint('news_getter', __name__, template_folder='templates')


@bp.get('/')
def index() -> Response:
    return render_template('news_getter/index.html')


@bp.get('/add-news')
def add_news_get() -> Response:
    return render_template('news_getter/add_news.html')


@bp.post('/add-news')
def add_news_post() -> Response:
    return redirect(url_for('.add_news_get'))
