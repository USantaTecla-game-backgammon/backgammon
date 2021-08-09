class DoublingCube:

    def __init__(self) -> None:
        self.value = 1

    def double(self) -> None:
        self.value *= 2

    def reset(self) -> None:
        self.value = 1


doubling_cube = DoublingCube()
