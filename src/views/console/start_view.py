from src.views import StartView as StartViewBase
from src.views.console import console


class StartView(StartViewBase):
    def show(cls) -> None:
        console.show(
            f'{cls.TITLE}\n\n'
            f'{cls.MSG_CHOOSE_COLOR}\n'
        )
