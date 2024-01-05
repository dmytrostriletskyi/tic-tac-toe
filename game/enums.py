"""
Provide implementation of the game's enumerates.
"""
from enum import Enum


class BoardCheckResultDecision(Enum):
    """
    Board check result's decision enum implementation.
    """

    WIN = 'win'
    TIE = 'tie'
    CONTINUE = 'continue'


class PlayerMark(Enum):
    """
    Player mark enum implementation.

    It is assumed players might choose personal style of their marks.
    """

    CLASSIC_X = 'x'
    CLASSIC_Y = 'o'
    MODERN_X = '✘'
    MODERN_Y = '𝐎'
