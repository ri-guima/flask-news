from flask import Blueprint, Response, render_template, redirect, url_for

from .forms import AddNewsSiteForm, AddPageForm


bp = Blueprint('flask_news', __name__, url_prefix='/news',
               template_folder='templates', static_folder='static')


@bp.get('/')
def index() -> Response:
    return render_template('flask_news/index.html')


@bp.get('/add-news-site')
def add_news_site_get() -> Response:
    return render_template('flask_news/add_news_site.html', form=AddNewsSiteForm())


@bp.post('/add-news-site')
def add_news_site_post() -> Response:
    return redirect(url_for('.add_news_site_get'))


@bp.get('/add-page')
def add_page_get() -> Response:
    return render_template('flask_news/add_page.html', form=AddPageForm())


@bp.post('/add-page')
def add_page_post() -> Response:
    return redirect(url_for('.add_page_get'))
