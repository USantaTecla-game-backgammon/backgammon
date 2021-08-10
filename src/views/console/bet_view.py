from src.views import BetView as BetViewBase
from src.views.console import console


class BetView(BetViewBase):
    @classmethod
    def show_ask(cls) -> None:
        console.show(cls.ASK)

    @classmethod
    def read_answer(cls) -> bool:
        return console.read_bool(cls.ANSWER)

    @classmethod
    def show_answer(cls, answer: bool) -> None:
        if answer:
            console.show(cls.ACCEPT)
        else:
            console.show(cls.REJECT)
