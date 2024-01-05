"""
Provide tests for the game board's getting.
"""
from game.board import Board
from game.enums import PlayerMark


def test_board_get():
    """
    Case: get a board.
    Expect: a list of players' marks or empty cells.
    """
    expected_board = board_ = [
        PlayerMark.CLASSIC_X, Board.EMPTY_CELL, Board.EMPTY_CELL,
        Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
        Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
    ]

    board = Board(players=[], size=3)
    board.board = board_

    assert expected_board == board.get()
