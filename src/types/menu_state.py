import enum


class CommandState(enum.Enum):
    ACTIVE = enum.auto()
    LOCKED = enum.auto()
    INACTIVE = enum.auto()
