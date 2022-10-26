from wtforms import StringField, URLField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class AddNewsSiteForm(FlaskForm):
    site_url = URLField(validators=[DataRequired()])
    titles_selector = StringField(validators=[DataRequired()])
    urls_selector = StringField(validators=[DataRequired()])
