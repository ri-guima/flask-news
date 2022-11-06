from flask import Blueprint, Response, render_template, redirect, url_for

from .forms import AddNewsSiteForm


bp = Blueprint('flask_news', __name__,
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
