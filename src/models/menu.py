from src.models.command import Command
from src.types import CommandState


class Menu:

    def __init__(self, title: str, commands: list[Command]) -> None:
        self.title = title
        self.commands = commands

    def valid_commands(self) -> list[Command]:
        commands = []
        exist_active_command = False

        for cmd in self.commands:
            if cmd.state() == CommandState.ACTIVE:
                exist_active_command = True
                commands.append(cmd)
            elif cmd.state() == CommandState.LOCKED:
                commands.append(cmd)

        if not exist_active_command:
            commands = []

        return commands

    def serialize(self) -> list[str, str]:
        return {}
