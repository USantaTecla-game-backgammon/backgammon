from abc import abstractmethod


class BetView:
    @abstractmethod
    def read(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def show_accept(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def show_reject(self) -> None:
        raise NotImplementedError
