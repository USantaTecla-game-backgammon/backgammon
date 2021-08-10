from src.views import FirstRollView as FirstRollViewBase
from src.views.console import console


class FirstRollView(FirstRollViewBase):

    @classmethod
    def show(cls, dices: dict[str, int]) -> None:
        console.show(cls.FIRST_ROLL)
        for color, dice in dices.items():
            console.show(f'Player {color}: {dice}')

    @classmethod
    def show_winner(cls, color: str) -> None:
        console.show(cls.FIRST_PLAYER.format(color))
