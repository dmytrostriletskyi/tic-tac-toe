"""
Provide tests for the game board's checking.
"""
import pytest

from game.board import Board
from game.dto import (
    BoardState,
    Player,
)
from game.enums import (
    BoardCheckResultDecision,
    PlayerMark,
)


@pytest.mark.parametrize(
    'board_',
    [
        [
            PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X,
            Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
            Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
        ],
        [
            Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
            PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X,
            Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
        ],
        [
            Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
            Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
            PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X,
        ],
    ],
)
def test_board_check_horizontal_win(board_):
    """
    Case: check a board state.
    When: a player has their marks in one of horizontal «lines».
    Expect: the board state is `win` with the player as a winning player.
    """
    player_x = Player(mark=PlayerMark.CLASSIC_X)

    board = Board(players=[player_x], size=3)
    board.board = board_

    expected_board_state = BoardState(
        decision=BoardCheckResultDecision.WIN,
        winning_player=player_x,
    )

    assert expected_board_state == board.check()


@pytest.mark.parametrize(
    'board_',
    [
        [
            PlayerMark.CLASSIC_X, Board.EMPTY_CELL, Board.EMPTY_CELL,
            PlayerMark.CLASSIC_X, Board.EMPTY_CELL, Board.EMPTY_CELL,
            PlayerMark.CLASSIC_X, Board.EMPTY_CELL, Board.EMPTY_CELL,
        ],
        [
            Board.EMPTY_CELL, PlayerMark.CLASSIC_X, Board.EMPTY_CELL,
            Board.EMPTY_CELL, PlayerMark.CLASSIC_X, Board.EMPTY_CELL,
            Board.EMPTY_CELL, PlayerMark.CLASSIC_X, Board.EMPTY_CELL,
        ],
        [
            Board.EMPTY_CELL, Board.EMPTY_CELL, PlayerMark.CLASSIC_X,
            Board.EMPTY_CELL, Board.EMPTY_CELL, PlayerMark.CLASSIC_X,
            Board.EMPTY_CELL, Board.EMPTY_CELL, PlayerMark.CLASSIC_X,
        ],
    ],
)
def test_board_check_vertical_win(board_):
    """
    Case: check a board state.
    When: a player has their marks in one of vertical «lines».
    Expect: the board state is `win` with the player as a winning player.
    """
    player_x = Player(mark=PlayerMark.CLASSIC_X)

    board = Board(players=[player_x], size=3)
    board.board = board_

    expected_board_state = BoardState(
        decision=BoardCheckResultDecision.WIN,
        winning_player=player_x,
    )

    assert expected_board_state == board.check()


@pytest.mark.parametrize(
    'board_',
    [
        [
            PlayerMark.CLASSIC_X, Board.EMPTY_CELL, Board.EMPTY_CELL,
            Board.EMPTY_CELL, PlayerMark.CLASSIC_X, Board.EMPTY_CELL,
            Board.EMPTY_CELL, Board.EMPTY_CELL, PlayerMark.CLASSIC_X,
        ],
        [
            Board.EMPTY_CELL, Board.EMPTY_CELL, PlayerMark.CLASSIC_X,
            Board.EMPTY_CELL, PlayerMark.CLASSIC_X, Board.EMPTY_CELL,
            PlayerMark.CLASSIC_X, Board.EMPTY_CELL, Board.EMPTY_CELL,
        ],
    ],
)
def test_board_check_diagonal_win(board_):
    """
    Case: check a board state.
    When: a player has their marks in one of diagonal «lines».
    Expect: the board state is `win` with the player as a winning player.
    """
    player_x = Player(mark=PlayerMark.CLASSIC_X)

    board = Board(players=[player_x], size=3)
    board.board = board_

    expected_board_state = BoardState(
        decision=BoardCheckResultDecision.WIN,
        winning_player=player_x,
    )

    assert expected_board_state == board.check()


@pytest.mark.parametrize(
    'board_',
    [
        [
            PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_Y, PlayerMark.CLASSIC_Y,
            PlayerMark.CLASSIC_Y, PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X,
            PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_Y,
        ],
        [
            PlayerMark.CLASSIC_Y, PlayerMark.CLASSIC_Y, PlayerMark.CLASSIC_X,
            PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_Y,
            PlayerMark.CLASSIC_Y, PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_Y,
        ],
    ],
)
def test_board_check_tie(board_):
    """
    Case: check a board state.
    When:
        - Neither of players have their marks in one of horizontal, verticals or diagonals «lines».
        - No positions to mark available.
    Expect: the board state is `tie` with `None` as a winning player.
    """
    player_x = Player(mark=PlayerMark.CLASSIC_X)
    player_y = Player(mark=PlayerMark.CLASSIC_Y)

    board = Board(players=[player_x, player_y], size=3)
    board.board = board_

    expected_board_state = BoardState(decision=BoardCheckResultDecision.TIE)

    assert expected_board_state == board.check()


@pytest.mark.parametrize(
    'board_',
    [
        [
            Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
            Board.EMPTY_CELL, PlayerMark.CLASSIC_X, Board.EMPTY_CELL,
            Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
        ],
        [
            Board.EMPTY_CELL, PlayerMark.CLASSIC_Y, Board.EMPTY_CELL,
            Board.EMPTY_CELL, PlayerMark.CLASSIC_X, Board.EMPTY_CELL,
            Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
        ],
        [
            Board.EMPTY_CELL, PlayerMark.CLASSIC_Y, Board.EMPTY_CELL,
            PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X, Board.EMPTY_CELL,
            Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
        ],
        [
            Board.EMPTY_CELL, PlayerMark.CLASSIC_Y, Board.EMPTY_CELL,
            PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_Y,
            Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL,
        ],
        [
            Board.EMPTY_CELL, PlayerMark.CLASSIC_Y, Board.EMPTY_CELL,
            PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_Y,
            Board.EMPTY_CELL, Board.EMPTY_CELL, PlayerMark.CLASSIC_X,
        ],
        [
            PlayerMark.CLASSIC_Y, PlayerMark.CLASSIC_Y, Board.EMPTY_CELL,
            PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_Y,
            Board.EMPTY_CELL, Board.EMPTY_CELL, PlayerMark.CLASSIC_X,
        ],
        [
            PlayerMark.CLASSIC_Y, PlayerMark.CLASSIC_Y, PlayerMark.CLASSIC_X,
            PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_Y,
            Board.EMPTY_CELL, Board.EMPTY_CELL, PlayerMark.CLASSIC_X,
        ],
        [
            PlayerMark.CLASSIC_Y, PlayerMark.CLASSIC_Y, PlayerMark.CLASSIC_X,
            PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_X, PlayerMark.CLASSIC_Y,
            PlayerMark.CLASSIC_Y, Board.EMPTY_CELL, PlayerMark.CLASSIC_X,
        ],
    ],
)
def test_board_check_continue(board_):
    """
    Case: check a board state.
    When:
        - Neither of players have their marks in one of horizontal, verticals or diagonals «lines».
        - Positions to mark available.
    Expect: the board state is `continue` with `None` as a winning player.
    """
    player_x = Player(mark=PlayerMark.CLASSIC_X)
    player_y = Player(mark=PlayerMark.CLASSIC_Y)

    board = Board(players=[player_x, player_y], size=3)
    board.board = board_

    expected_board_state = BoardState(decision=BoardCheckResultDecision.CONTINUE)

    assert expected_board_state == board.check()
