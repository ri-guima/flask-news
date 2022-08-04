from flask import Blueprint, Response, render_template


bp = Blueprint(
    'news_getter', __name__, url_prefix='/news-getter',
    template_folder='templates', static_folder='static',
)


@bp.get('/')
def index_get() -> Response:
    return render_template('news_getter/index.html')
