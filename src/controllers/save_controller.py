import pickle
from pathlib import Path
from typing import Final

from src.models.match import Match


class SaveController:
    FOLDER: Final[str] = 'saved'

    def __init__(self, match: Match, filename: str) -> None:
        self.match = match
        self.filename = filename

    def __call__(self) -> None:
        folder = Path(self.FOLDER)
        folder.mkdir(exist_ok=True)
        with open(f'{self.FOLDER}/{self.filename}', 'wb') as f:
            f.write(pickle.dumps(self.match.__dict__))
