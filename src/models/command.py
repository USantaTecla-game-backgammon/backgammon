class Command:
    title = 'command'

    def __call__(self) -> None:
        raise NotImplementedError

    def is_active(self) -> bool:
        raise NotImplementedError
