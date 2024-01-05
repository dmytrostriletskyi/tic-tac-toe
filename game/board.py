"""
Provide implementation of the game's board.
"""
from game.dto import (
    BoardState,
    Player,
    PlayerMark,
)
from game.enums import BoardCheckResultDecision
from game.exceptions import (
    BoardPlayerDoesNotExistException,
    BoardPlayersMarksDuplicateException,
    BoardPositionAlreadyTakenException,
    BoardPositionDoesNotExistException,
)
from game.utils import (
    get_diagonal_sublists,
    get_horizontal_sublists,
    get_vertical_sublists,
    is_list_has_equal_elements,
)


class Board:
    """
    Board implementation.
    """

    EMPTY_CELL = None

    def __init__(self, players: [Player], size: int = 3) -> None:
        """
        Construct the object.

        Arguments:
            players (list): a list of players as list of `Player`.
            size (int): a size of a board as integer, means number of position per side in a perfect square.
        """
        self.players = players
        self.players_number = len(players)

        if not self._are_players_marks_unique():
            raise BoardPlayersMarksDuplicateException

        self.size = size

        self.board = [self.EMPTY_CELL, self.EMPTY_CELL, self.EMPTY_CELL] * size
        self.board_positions_number = len(self.board)

    def get(self) -> list:
        """
        Get a board.
        """
        return self.board

    def mark(self, player: Player, position: int) -> None:
        """
        Mark a board's cell by a player.

        It accepts the position as human-readable position meaning first position would be 1.
        For computers, in particular board representation as a list, the first position is 0.

        Arguments:
            player (Player): a player as a `Player`.
            position (int): position on a board.
        """
        if player not in self.players:
            raise BoardPlayerDoesNotExistException

        if position == 0 or position > self.board_positions_number:
            raise BoardPositionDoesNotExistException

        computer_position = position - 1
        cell = self.board[computer_position]

        if cell is not self.EMPTY_CELL:
            raise BoardPositionAlreadyTakenException

        self.board[computer_position] = player.mark

    def check(self) -> BoardState:
        """
        Check a board's state.

        It checks if board's state is a win of a player, tie or continue. It is meant to check the board state after
        each move. The algorithm is way simple: take all possible and winnable positions (all horizontals, verticals
        and diagonals) and check for all marks of them would be equal (meaning related to a single player).

        Returns:
             A board's state as a `BoardState`.
        """
        horizontal_marks = get_horizontal_sublists(list_=self.board, chunks=self.size)
        vertical_marks = get_vertical_sublists(list_=self.board, chunks=self.size)
        diagonal_marks = get_diagonal_sublists(list_=self.board)

        for direction_marks in [horizontal_marks, vertical_marks, diagonal_marks]:
            for marks in direction_marks:
                if self.EMPTY_CELL in marks:
                    continue

                are_marks_identical = is_list_has_equal_elements(list_=marks)

                if not are_marks_identical:
                    continue

                winning_player = self._get_player_from_marks(marks=marks)
                return BoardState(decision=BoardCheckResultDecision.WIN, winning_player=winning_player)

        if self.EMPTY_CELL not in self.board:
            return BoardState(decision=BoardCheckResultDecision.TIE)

        return BoardState(decision=BoardCheckResultDecision.CONTINUE)

    def _get_player_from_marks(self, marks: [PlayerMark]) -> Player:
        """
        Get a player from marks.

        It meant that provided list has marks only from the same player.

        Arguments:
            marks (list): a list of a player's marks.

        Returns:
            A player of the marks as a `Player`.
        """
        for player in self.players:
            if player.mark in marks:
                return player

    def _are_players_marks_unique(self) -> bool:
        """
        Check if players' marks are unique.
        """
        players_marks = []

        for player in self.players:
            players_marks.append(player.mark)

        unique_players_marks = set(players_marks)
        unique_players_marks_number = len(unique_players_marks)

        if self.players_number == unique_players_marks_number:
            return True

        return False
