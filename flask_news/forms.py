from wtforms import StringField, URLField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

from .fields import NewsSiteField


class AddNewsSiteForm(FlaskForm):
    site_domain = URLField(validators=[DataRequired()])
    titles_selector = StringField(validators=[DataRequired()])
    urls_selector = StringField(validators=[DataRequired()])


class AddNewsPageForm(FlaskForm):
    site = NewsSiteField(validators=[DataRequired()])
    name = StringField(validators=[DataRequired()])
