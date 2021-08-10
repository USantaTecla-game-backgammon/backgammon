from src.controllers.controller import Controller


class ResumeController(Controller):

    def __call__(self) -> bool:
        return self.match.is_goal()
