"""
Provide implementation of the game's utils.
"""
import math

from game.exceptions import ListIsNotPerfectSquareException


def get_horizontal_sublists(list_: list, chunks: int) -> list[list]:
    """
    Get «horizontal» sublists.

    It «horizontally» partitions a given list into sublists, each containing a specified number of elements (chunks).
    Is used to understand if any of game's players have only their marks in one of the sublists, thus won
    «horizontally».

    Returns:
        A «horizontally» partitioned list by chunks as list of lists.
    """
    list_length = len(list_)
    sublists = []

    for index in range(0, list_length, chunks):
        sublist = list_[index:index+chunks]
        sublists.append(sublist)

    return sublists


def get_vertical_sublists(list_: list, chunks: int) -> list[list]:
    """
    Get «vertical» sublists.

    It «vertically» partitions a given list into sublists, each containing a specified number of elements (chunks),
    with each sublist containing elements from the same position across multiple sublists. Is used to understand if
    any of game's players have only their marks in one of the sublists, thus won «vertically».

    Returns:
        A «vertically» partitioned list by chunks as list of lists.
    """
    sublists = []

    for index in range(chunks):
        sublist = list_[index::chunks]
        sublists.append(sublist)

    return sublists


def get_diagonal_sublists(list_: list) -> list[list]:
    """
    Get «diagonal» sublists.

    It «diagonally» partitions a given list into sublists: the first sublist represents the elements along the main
    diagonal, and the second sublist represents the elements along the secondary diagonal of the square matrix.

    Raises:
        ListIsNotPerfectSquare: if the list, representing a matrix, is not a perfect square.

    Returns:
        A «diagonally» partitioned list.
    """
    list_length = len(list_)

    if list_length != math.isqrt(list_length) ** 2:
        raise ListIsNotPerfectSquareException

    size = math.isqrt(list_length)

    first_diagonal_sublist = []
    increment = 0

    for _ in range(size):
        element = list_[increment]
        first_diagonal_sublist.append(element)
        increment += size + 1

    second_diagonal_sublist = []
    increment = size - 1

    for _ in range(size):
        element = list_[increment]
        second_diagonal_sublist.append(element)
        increment += size - 1

    return [first_diagonal_sublist, second_diagonal_sublist]


def is_list_has_equal_elements(list_: list) -> bool:
    """
    Check if elements of a list are equal.

    Is used to understand if any of game's players have only their marks in one of the sublists, thus won
    «horizontally», «vertically» or «diagonally».

    Return:
        True, if elements of a list are equal.
        Otherwise, False.
    """
    unique_elements = set(list_)

    if len(unique_elements) >= 2:
        return False

    return True
