from src.views import PlayView, ResumeView, StartView
from src.views.view_factory import ViewFactory


class GUIViewFactory(ViewFactory):
    def create_start_view(self) -> StartView:
        raise NotImplementedError

    def create_play_view(self) -> PlayView:
        raise NotImplementedError

    def create_resume_view(self) -> ResumeView:
        raise NotImplementedError
