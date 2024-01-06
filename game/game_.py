"""
Provide implementation of the game.
"""
import sys

from game.board import Board
from game.dto import Player
from game.enums import (
    BoardCheckResultDecision,
    PlayerMark,
)
from game.exceptions import (
    BoardPositionAlreadyTakenException,
    BoardPositionDoesNotExistException,
)
from game.ui import Ui


class Game:
    """
    The game implementation.
    """

    CONTINUE = True
    POSITION_IS_VALID = False
    SYSTEM_EXIT_STATUS = 1

    def __init__(self):
        """
        Construct the object.
        """
        self.player_x = Player(mark=PlayerMark.CLASSIC_X)
        self.player_y = Player(mark=PlayerMark.CLASSIC_Y)

        self.board = Board(players=[self.player_x, self.player_y])
        self.ui = Ui(board=self.board)

    def start(self):
        """
        Start a game.
        """
        self.ui.show_title()
        self.ui.show_how_to_play()
        self.ui.show_current_board()

        current_player = self.player_x

        while Game.CONTINUE:
            while not self.POSITION_IS_VALID:
                position = input(f'Player {current_player.mark.value}, enter a position: ')

                if not position.isdigit():
                    self.ui.show_position_is_invalid()
                    continue

                position = int(position)

                try:
                    self.board.mark(player=current_player, position=position)

                except BoardPositionDoesNotExistException:
                    self.ui.show_position_is_invalid()
                    continue

                except BoardPositionAlreadyTakenException:
                    self.ui.show_position_is_invalid()
                    continue

                break

            board_state = self.board.check()
            self.ui.show_current_board()

            if board_state.decision == BoardCheckResultDecision.CONTINUE:
                current_player = self.player_y if current_player == self.player_x else self.player_x
                continue

            if board_state.decision == BoardCheckResultDecision.TIE:
                self.ui.show_tie_result()
                sys.exit(Game.SYSTEM_EXIT_STATUS)

            if board_state.decision == BoardCheckResultDecision.WIN:
                self.ui.show_win_result(player=current_player)
                sys.exit(Game.SYSTEM_EXIT_STATUS)


if __name__ == '__main__':
    game = Game()
    game.start()
