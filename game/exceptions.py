"""
Provide implementation of the game's exceptions.
"""


class BoardPlayersMarksDuplicateException(Exception):
    """
    Board players' marks duplicate exception.
    """
    pass


class BoardPlayerDoesNotExistException(Exception):
    """
    Board's player does not exist exception.
    """
    pass


class BoardPositionDoesNotExistException(Exception):
    """
    Board's position does not exist exception.
    """
    pass


class BoardPositionAlreadyTakenException(Exception):
    """
    Board's position already taken exception.
    """
    pass


class ListIsNotPerfectSquareException(Exception):
    """
    List is not a perfect square exception.
    """
    pass
