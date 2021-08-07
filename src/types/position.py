import enum


class Position(enum.Enum):
    ONE = (1, 24)
    TWO = (2, 23)
    THREE = (3, 22)
    FOUR = (4, 21)
    FIVE = (5, 20)
    SIX = (6, 19)
    SEVEN = (7, 18)
    EIGHT = (8, 17)
    NINE = (9, 16)
    TEN = (10, 15)
    ELEVEN = (11, 14)
    TWELVE = (12, 13)
    THIRTEEN = (13, 12)
    FOURTEEN = (14, 11)
    FIFTEEN = (15, 10)
    SIXTEEN = (16, 9)
    SEVENTEEN = (17, 8)
    EIGHTEEN = (18, 7)
    NINETEEN = (19, 6)
    TWENTY = (20, 5)
    TWENTY_ONE = (21, 4)
    TWENTY_TWO = (22, 3)
    TWENTY_THREE = (23, 2)
    TWENTY_FOUR = (24, 1)
    BAR = (0,0)
    OFF_BOARD = (100,100)

    def __init__(self, color_a: int, color_b: int) -> None:
        self.color_a = color_a
        self.color_b = color_b

    @property
    def position_of_color_a(self) -> int:
        return self.color_a

    @property
    def position_of_color_b(self) -> int:
        return self.color_b

    @property
    def value(self) -> int:
        return self.color_a