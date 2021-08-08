from typing import Optional
from src.types.position import Position


class Move:
    def __init__(
            self,
            from_position: Optional[Position] = None,
            to_position: Optional[Position] = None
    ) -> None:
        self.from_position = from_position
        self.to_position = to_position
