import enum


class GameState(enum.Enum):
    CHOOSING_PLAYER = enum.auto()
    IN_GAME = enum.auto()
    ROLLING_DICE = enum.auto()
    MOVING_RED = enum.auto()
    MOVING_BLACK = enum.auto()
    BETTING = enum.auto()
    ANSWERING_BET = enum.auto()
    END_GAME = enum.auto()
