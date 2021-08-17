from src.models.board import Board
from src.models.dice import Dice
from src.models.turn import Turn
from src.models.player import Player
from src.models.move import Move
from src.types import Color, Endgame, GameState, Position


class Game:
    def __init__(self) -> None:
        self.board: Board = Board()
        self.state: GameState = GameState.IN_GAME
        self.turn: Turn = Turn()
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

    def get_type_endgame(self) -> Endgame:
        assert self.is_endgame()

        looser_color: Color = Color.RED
        if self.board.is_all_pieces_off_board(Color.RED):
            looser_color = Color.BLACK

        if self.board.is_any_piece_off_board(looser_color):
            return Endgame.SIMPLE

        if (
            not self.board.is_any_piece_at_last_square(looser_color) and
            not self.board.is_any_piece_in_bar(looser_color)
        ):
            return Endgame.GAMMON

        return Endgame.BACKGAMMON

    def give_score(self) -> None:
        pass

    def move_piece(self, move: Move) -> None:
        self.board.move_piece(
            sense=self.turn.current_color,
            move=move,
            color=self.turn.current_color,
        )
        self.possible_moves.remove(move.dice_value)

    def get_pieces(self, position: Position) -> list[Color]:
        return self.board.get_pieces(
            sense=self.current_player.color,
            position=position
        )

    def get_my_pieces(self, position: Position) -> int:
        return self.get_pieces(position).count(self.current_player.color)

    def get_opponent_pieces(self, position: Position) -> int:
        return self.get_pieces(position).count(self.turn.opponent_player.color)

    def try_eat_piece(self, position_to: Position) -> None:
        assert position_to != Position.BAR

        if position_to == Position.OFF_BOARD:
            return

        opponent_color = self.turn.opponent_player.color
        if self.get_pieces(position_to).count(opponent_color) == 1:
            self.board.move_piece(
                sense=self.turn.current_color,
                move=Move(position_from=position_to, position_to=Position.OFF_BOARD),
                color=opponent_color
            )
