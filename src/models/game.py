from src.models.board import Board
from src.models.dice import Dice
from src.models.turn import Turn
from src.models.player import Player
from src.models.doubling_cube import doubling_cube
from src.types import Color, Endgame, GameState, Position


class Game:
    def __init__(self, turn: Turn) -> None:
        self.board: Board = Board()
        self.state: GameState = GameState.IN_GAME
        self.turn: Turn = turn
        self._last_roll: list[Dice] = []
        self.possible_moves: list[int] = []

    @property
    def current_player(self) -> Player:
        return self.turn.current_player

    @property
    def last_roll(self) -> list[Dice]:
        return self._last_roll

    @last_roll.setter
    def last_roll(self, dices: list[Dice]) -> None:
        self._last_roll = dices

        possibles = [dice.value for dice in dices]
        if len(possibles) == 2 and possibles[0] == possibles[1]:
            possibles += possibles

        self.possible_moves = possibles

    def roll_current_player(self) -> None:
        self.last_roll = self.turn.roll_current_player()
        self.state = GameState.MOVING_PIECE

    def change_turn(self) -> None:
        self.turn.change()
        self.state = GameState.IN_GAME

    def is_endgame(self) -> bool:
        return (
            self.board.is_all_pieces_off_board(Color.BLACK) or
            self.board.is_all_pieces_off_board(Color.RED) or
            self.state == GameState.END_GAME
        )

    def type_endgame(self) -> Endgame:
        assert self.is_endgame()

        looser_color: Color = Color.RED
        if self.board.is_all_pieces_off_board(Color.RED):
            looser_color = Color.BLACK

        if self.board.is_any_piece_off_board(looser_color):
            return Endgame.SIMPLE

        if (
            not self.board.is_any_piece_at_first_square(looser_color) and
            not self.board.is_any_piece_in_bar(looser_color)
        ):
            return Endgame.GAMMON

        return Endgame.BACKGAMMON

    def give_score(self) -> None:
        if self.board.is_all_pieces_off_board(Color.BLACK):
            self.turn.winner_by_color(Color.BLACK)

        if self.board.is_all_pieces_off_board(Color.RED):
            self.turn.winner_by_color(Color.RED)

        self.turn.give_score_to_winner(
            self.type_endgame().value * doubling_cube.value
        )

    def move_piece(self, amount: int, position: int) -> None:
        position_to = position - amount
        self.board.move_piece(position, position_to, self.current_player.color)
        self.possible_moves.remove(amount)

    def get_pieces(self, position: Position) -> list[Color]:
        return self.board.get_pieces(self.current_player.color, position)
