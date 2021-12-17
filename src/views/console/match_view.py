from typing import Any, Final

from src.types.color import Color
from src.views.console import console
from src.views import MatchView as MatchViewBase


class MatchView(MatchViewBase):
    TITLE: Final = '### BACKGAMMON ###'
    CHOOSE_COLOR: Final = 'Each player should choose a color.'
    DEFINE_GOAL: Final = 'Define your goal? (1-64)'
    GOAL_RANGE: list[int] = list(range(1, 65))
    RESUME: Final = 'Do you want to resume a match? (y/n)'
    FIRST_ROLL: Final = '\nFirst roll: choosing first player ...'
    FIRST_PLAYER: Final = 'First player is {}'

    @classmethod
    def show_title(cls) -> None:
        console.show(
            f'{cls.TITLE}\n\n'
            f'{cls.CHOOSE_COLOR}\n'
        )

    def show_dices(self, game_serialized: list[dict[str, Any]]) -> None:
        dices = game_serialized.get('list_dices_rolled')
        console.show(self.FIRST_ROLL)
        for dice in dices:
            for color, value in dice.items():
                console.show(f'Player {color}: {value}')

    def show_first_player(self, color: Color) -> None:
        console.show(self.FIRST_PLAYER.format(color))

    @classmethod
    def read_goal(cls) -> int:
        return console.read_int_range(valids=cls.GOAL_RANGE, msg=cls.DEFINE_GOAL)

    @classmethod
    def read_resume(cls) -> bool:
        return console.read_bool(cls.RESUME)

    @classmethod
    def read_filename(cls) -> str:
        return console.read_str()
