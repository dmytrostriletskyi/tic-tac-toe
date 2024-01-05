"""
Provide tests for the game board's player.
"""
import pytest

from game.board import Board
from game.dto import Player
from game.enums import PlayerMark
from game.exceptions import BoardPlayersMarksDuplicateException


def test_board_players_dont_have_unique_marks():
    """
    Case: initiate a board.
    When: providing players with duplicated marks.
    Expect: the board players' marks duplicate exception is raised.
    """
    player_x = Player(mark=PlayerMark.CLASSIC_X)
    player_y = Player(mark=PlayerMark.CLASSIC_X)

    with pytest.raises(BoardPlayersMarksDuplicateException):
        Board(players=[player_x, player_y], size=3)
