from src.controllers.controller import Controller


class ResumeController(Controller):

    def __call__(self) -> bool:
        return self.view_factory.create_match_view().read_resume()
