from pathlib import Path
from typing import Final

from src.models.match import Match


class SaveController:
    FOLDER: Final[str] = 'saved'

    def __init__(self, match: Match, filename: str) -> None:
        self.match = match
        self.filename = filename
        self._create_saved_folder()

    @property
    def filepath(self) -> Path:
        return Path(self.FOLDER, self.filename)

    def _create_saved_folder(self) -> None:
        folder = Path(self.FOLDER)
        folder.mkdir(exist_ok=True)

    def __call__(self) -> None:
        self.match.save(self.filepath)
