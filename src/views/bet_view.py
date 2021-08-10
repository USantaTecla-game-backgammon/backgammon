from abc import abstractmethod


class BetView:
    ASK = 'Player double bet'
    ANSWER = 'Do you accept bet? (y/n)'
    ACCEPT = 'Player accepted bet'
    REJECT = 'Player rejected bet'

    @abstractmethod
    def show_ask(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def read_answer(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def show_answer(self, answer: bool) -> None:
        raise NotImplementedError
