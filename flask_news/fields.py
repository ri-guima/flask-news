from wtforms import SelectField

from .repositories import NewsSiteRepository


class NewsSiteField(SelectField):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.choices = [(m.id, m.domain) for m in NewsSiteRepository().all()]
