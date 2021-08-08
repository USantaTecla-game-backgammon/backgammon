from src.types.position import Position


class Move:
    def __init__(self, from_position: Position = None, to_position: Position = None) -> None:
        self.from_position = from_position
        self.to_position = to_position
