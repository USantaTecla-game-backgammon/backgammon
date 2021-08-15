from src.models.dice import Dice
from src.models.game import Game
from src.types import Color, GameState


def game_factory(match_turn_color: Color, first_roll: list[Dice]) -> Game:
    game = Game()
    if first_roll:
        game.last_roll = first_roll
        game.state = GameState.MOVING_PIECE

    game.turn.current_color = match_turn_color
    return game
