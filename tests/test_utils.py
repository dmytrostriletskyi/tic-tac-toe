"""
Provide tests for the game's utils.
"""
import pytest

from game.utils import (
    get_diagonal_sublists,
    get_horizontal_sublists,
    get_vertical_sublists,
)


@pytest.mark.parametrize(
    'list_, chunks, expected_sublists',
    [
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            4,
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16],
            ],
        ),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            3,
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
        )
    ],
)
def test_get_horizontal_sublists(list_, chunks, expected_sublists):
    """
    Case: get horizontal sublists of a list.
    Expect: a list of sublists, each containing a specified number of elements (chunks).
    """
    sublists = get_horizontal_sublists(list_=list_, chunks=chunks)
    assert expected_sublists == sublists


@pytest.mark.parametrize(
    'list_, chunks, expected_sublists',
    [
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            3,
            [
                [1, 4, 7],
                [2, 5, 8],
                [3, 6, 9],
            ],
        ),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            4,
            [
                [1, 5, 9, 13],
                [2, 6, 10, 14],
                [3, 7, 11, 15],
                [4, 8, 12, 16],
            ],
        ),
    ],
)
def test_get_vertical_sublists(list_, chunks, expected_sublists):
    """
    Case: get vertical sublists of a list.
    Expect: a list of sublists, each containing a specified number of elements (chunks), with each sublist containing
            elements from the same position across multiple sublists.
    """
    sublists = get_vertical_sublists(list_=list_, chunks=chunks)
    assert expected_sublists == sublists


@pytest.mark.parametrize(
    'list_, expected_sublists',
    [
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [
                [1, 5, 9],
                [3, 5, 7],
            ],
        ),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            [
                [1, 6, 11, 16],
                [4, 7, 10, 13],
            ],
        ),
    ],
)
def test_get_diagonal_sublists(list_, expected_sublists):
    """
    Case: get diagonal siblists of a list.
    Expect: a list of sublists where the first sublist represents the elements along the main diagonal, and the second
            sublist represents the elements along the secondary diagonal of the square matrix.
    """
    sublists = get_diagonal_sublists(list_=list_)
    assert expected_sublists == sublists
