import pickle
from pathlib import Path

from src.models.match import Match


class SaveController:
    def __init__(self, match: Match, filename: str) -> None:
        self.match = match
        self.filename = filename

    def __call__(self) -> None:
        folder = Path('saved')
        folder.mkdir(exist_ok=True)
        with open(f'saved/{self.filename}', 'wb') as f:
            f.write(pickle.dumps(self.match.__dict__))
