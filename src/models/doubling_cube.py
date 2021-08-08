class DoublingCube:
    _values = [64, 2, 4, 8, 16, 32, 64]
    _doubled = False

    def __init__(self) -> None:
        self.value = self._values[0]

    def double(self) -> None:
        if self.value == 64 and self._doubled:
            raise AssertionError()
        self._doubled = True
        for k, v in enumerate(self._values):
            if v == self.value:
                self.value = self._values[k + 1]
                return None
