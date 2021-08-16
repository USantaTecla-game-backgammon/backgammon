from typing import Any


class GameView:

    @classmethod
    def show_start(cls) -> None:
        raise NotImplementedError

    @classmethod
    def show_score(cls, turn: Any) -> None:
        raise NotImplementedError
