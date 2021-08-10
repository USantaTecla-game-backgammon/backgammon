from src.views import PlayView as PlayViewBase
from src.views.console import console


class PlayView(PlayViewBase):
    @classmethod
    def show(cls):
        console.show(cls.START)
