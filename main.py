import sys

from src.backgammon import Backgammon
from src.views.console.console_view_factory import ConsoleViewFactory
from src.views.gui.gui_view_factory import GUIViewFactory
from src.views.view_factory import ViewFactory


factories = {
    'default': ConsoleViewFactory(),
    'console': ConsoleViewFactory(),
    'gui': GUIViewFactory(),
}


def read_settings_from_arguments() -> ViewFactory:
    arguments = sys.argv[1:]
    key = arguments[0] if arguments else 'default'

    if key in factories.keys():
        return factories.get(key)
    return factories.get('default')


if __name__ == '__main__':
    view_factory = read_settings_from_arguments()
    Backgammon(view_factory).play()
