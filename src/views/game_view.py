from src.models.turn import Turn


class GameView:

    @classmethod
    def show_start(cls) -> None:
        raise NotImplementedError

    @classmethod
    def show_score(cls, turn: Turn) -> None:
        raise NotImplementedError
