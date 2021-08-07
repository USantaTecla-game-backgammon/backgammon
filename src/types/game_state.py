import enum


class GameState(enum.Enum):
    IN_GAME = enum.auto()
    MOVING_PIECE = enum.auto()
    BETTING = enum.auto()
    END_GAME = enum.auto()
