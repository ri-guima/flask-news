from wtforms import SelectField

from .repositories import NewsSiteRepository


class NewsSiteField(SelectField):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.choices = [(n, n) for n in NewsSiteRepository().all()]
