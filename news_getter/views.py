from flask import Blueprint, Response, render_template


bp = Blueprint('news_getter', __name__, template_folder='templates')


@bp.get('/')
def index() -> Response:
    return render_template('news_getter/index.html')
