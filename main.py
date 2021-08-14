import sys

from src.backgammon import Backgammon


def read_settings_from_arguments() -> str:
    arguments = sys.argv[1:]
    return arguments[0] if arguments else ''


if __name__ == '__main__':
    SETTINGS = read_settings_from_arguments()
    Backgammon(SETTINGS).play()
