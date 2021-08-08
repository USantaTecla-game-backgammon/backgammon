class DoublingCube:
    _values = [64, 2, 4, 8, 16, 32, 64]
    _doubled = False

    def __init__(self) -> None:
        self.value = self._values[0]

    def double(self) -> None:
        if self.value == 64 and self._doubled:
            raise AssertionError()
        self._doubled = True
        for key, val in enumerate(self._values):
            if val == self.value:
                self.value = self._values[key + 1]
                return
