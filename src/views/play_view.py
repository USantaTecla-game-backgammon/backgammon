from typing import Final


class PlayView:
    START: Final[str] = '-- Starting new game --\n'

    @classmethod
    def show(cls):
        raise NotImplementedError
