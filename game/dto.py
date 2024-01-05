"""
Provide implementation of the game's dataclasses.
"""
from typing import Optional

from dataclasses import dataclass

from game.enums import (
    BoardCheckResultDecision,
    PlayerMark,
)


@dataclass
class Player:
    """
    Player dataclass implementation.
    """

    mark: PlayerMark

    def __repr__(self):
        """
        Get printable representational string of the player object.
        """
        return f'Player(mark={self.mark})'


@dataclass
class BoardState:
    """
    Board's state dataclass implementation.
    """

    decision: BoardCheckResultDecision
    winning_player: Optional[Player] = None

    def __eq__(self, other: 'BoardState'):
        """
        Perform comparison to the same type of other object.

        Arguments:
            other (BoardState): board check's result.

        Returns:
            True, if objects are equals.
            Otherwise, False.
        """
        if self.decision.value != other.decision.value:
            return False

        if self.winning_player is None and other.winning_player is None:
            return True

        if self.winning_player.mark != other.winning_player.mark:
            return False

        return True
