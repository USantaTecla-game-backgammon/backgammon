import sys

from src.backgammon import Backgammon
from src.views.console.console_view_factory import ConsoleViewFactory
from src.views.gui.gui_view_factory import GUIViewFactory
from src.views.view_factory import ViewFactory


def read_settings_from_arguments() -> ViewFactory:
    arguments = sys.argv[1:]
    if not arguments:
        return ConsoleViewFactory()

    if arguments[0] == 'gui':
        return GUIViewFactory()

    return ConsoleViewFactory()


if __name__ == '__main__':
    view_factory = read_settings_from_arguments()
    Backgammon(view_factory).play()
