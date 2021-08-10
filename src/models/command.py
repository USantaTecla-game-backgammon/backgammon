from src.types import CommandState


class Command:
    title = 'command'

    def __call__(self) -> None:
        raise NotImplementedError

    def state(self) -> CommandState:
        raise NotImplementedError
