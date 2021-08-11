from src.views import BetView as BetViewBase
from src.views.console import console


class BetView(BetViewBase):
    ANSWER = 'Do you accept bet? (y/n)'
    ACCEPT = 'Player accepted bet'
    REJECT = 'Player rejected bet'

    def read(self) -> bool:
        return console.read_bool(self.ACCEPT)

    def show_accept(self) -> None:
        console.show(self.ACCEPT)

    def show_reject(self) -> None:
        console.show(self.REJECT)
