from pathlib import Path
from typing import Final

from src.models.match import Match
from src.views.view_factory import ViewFactory


class SaveController:
    FOLDER: Final[str] = 'saved'

    def __init__(self, match: Match, view_factory: ViewFactory):
        self.match = match
        self.match_view = view_factory.create_match_view()
        self._create_saved_folder()

    @property
    def filepath(self) -> Path:
        return Path(self.FOLDER, self.filename)

    def _create_saved_folder(self) -> None:
        folder = Path(self.FOLDER)
        folder.mkdir(exist_ok=True)

    def __call__(self) -> None:
        self.filename = self.match_view.read_filename()
        self.match.save(self.filepath)
