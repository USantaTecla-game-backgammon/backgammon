from src.views import ConfigureGoalView as ConfigureGoalViewBase
from src.views.console import console


class ConfigureGoalView(ConfigureGoalViewBase):

    def show(self, title: str) -> None:
        raise NotImplementedError

    @classmethod
    def read(cls) -> int:
        return 8  # TODO: remove
        #return console.read_int_range(valids=cls.GOAL_RANGE, msg=cls.DEFINE_GOAL)
