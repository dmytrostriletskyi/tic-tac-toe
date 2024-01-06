"""
Provide implementation of the game's exceptions.
"""


class BoardPlayersMarksDuplicateException(Exception):
    """
    Board players' marks duplicate exception.
    """


class BoardPlayerDoesNotExistException(Exception):
    """
    Board's player does not exist exception.
    """


class BoardPositionDoesNotExistException(Exception):
    """
    Board's position does not exist exception.
    """


class BoardPositionAlreadyTakenException(Exception):
    """
    Board's position already taken exception.
    """


class ListIsNotPerfectSquareException(Exception):
    """
    List is not a perfect square exception.
    """
