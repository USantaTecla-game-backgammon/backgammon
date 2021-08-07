from src.models.command import Command


class Menu:

    def __init__(self, title: str, commands: list[Command]) -> None:
        self.title = title
        self.commands = commands

    def active_commands(self) -> list[Command]:
        return [command for command in self.commands if command.is_active()]
