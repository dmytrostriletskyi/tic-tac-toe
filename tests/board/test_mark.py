"""
Provide tests for the game board's marking.
"""
import pytest

from game.board import Board
from game.dto import Player
from game.enums import PlayerMark
from game.exceptions import (
    BoardPlayerDoesNotExistException,
    BoardPositionAlreadyTakenException,
    BoardPositionDoesNotExistException,
)


@pytest.mark.parametrize(
    ('position', 'expected_board'),
    [
        (
            1,
            [
                PlayerMark.CLASSIC_X, Board.EMPTY_CELL, Board.EMPTY_CELL,
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
            ],
        ),
        (
            2,
            [
                Board.EMPTY_CELL, PlayerMark.CLASSIC_X, Board.EMPTY_CELL,
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
            ],
        ),
        (
            3,
            [
                Board.EMPTY_CELL, Board.EMPTY_CELL, PlayerMark.CLASSIC_X,
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
            ],
        ),
        (
            4,
            [
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
                PlayerMark.CLASSIC_X, Board.EMPTY_CELL, Board.EMPTY_CELL,
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
            ],
        ),
        (
            5,
            [
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
                Board.EMPTY_CELL, PlayerMark.CLASSIC_X, Board.EMPTY_CELL,
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
            ],
        ),
        (
            6,
            [
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
                Board.EMPTY_CELL, Board.EMPTY_CELL, PlayerMark.CLASSIC_X,
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
            ],
        ),
        (
            7,
            [
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
                PlayerMark.CLASSIC_X, Board.EMPTY_CELL, Board.EMPTY_CELL,
            ],
        ),
        (
            8,
            [
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
                Board.EMPTY_CELL, PlayerMark.CLASSIC_X, Board.EMPTY_CELL,
            ],
        ),
        (
            9,
            [
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
                Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
                Board.EMPTY_CELL, Board.EMPTY_CELL, PlayerMark.CLASSIC_X,
            ],
        ),
    ],
)
def test_board_mark_position_not_taken(position, expected_board):
    """
    Case: mark a board.
    When: position is not taken.
    Expect: the board position's is taken by a player (and its mark).
    """
    player_x = Player(mark=PlayerMark.CLASSIC_X)

    board = Board(players=[player_x], size=3)
    board.mark(player=player_x, position=position)

    assert expected_board == board.board


def test_board_mark_player_does_not_exist():
    """
    Case: mark a board.
    When: specifying a player that does not exist on the board.
    Expect: the board's player does not exist exception is raised.
    """
    player_x = Player(mark=PlayerMark.CLASSIC_X)
    player_y = Player(mark=PlayerMark.CLASSIC_Y)

    board = Board(players=[player_x], size=3)

    with pytest.raises(BoardPlayerDoesNotExistException):
        board.mark(player=player_y, position=1)


@pytest.mark.parametrize(
    ('board_size', 'non_existing_position'),
    [
        (3, 0),
        (3, 10),
        (4, 0),
        (4, 17),
        (5, 0),
        (5, 26),
    ],
)
def test_board_mark_position_does_not_exist(board_size, non_existing_position):
    """
    Case: mark a board.
    When: specifying a position that does not exist on the board.
    Expect: the board's position does not exist exception is raised.
    """
    player_x = Player(mark=PlayerMark.CLASSIC_X)
    board = Board(players=[player_x], size=board_size)

    with pytest.raises(BoardPositionDoesNotExistException):
        board.mark(player=player_x, position=non_existing_position)


def test_board_mark_board_position_already_taken():
    """
    Case: mark a board.
    When: specifying a position that already taken.
    Expect: the board's position already taken exception is raised.
    """
    player_x = Player(mark=PlayerMark.CLASSIC_X)
    player_y = Player(mark=PlayerMark.CLASSIC_Y)

    board = Board(players=[player_x, player_y], size=3)
    board.mark(player=player_x, position=1)

    with pytest.raises(BoardPositionAlreadyTakenException):
        board.mark(player=player_x, position=1)
