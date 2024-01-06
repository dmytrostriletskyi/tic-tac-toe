"""
Provide implementation of the game's UI.
"""
from game.board import Board
from game.dto import Player


class Ui:
    """
    Game's UI implementation.
    """

    TITLE = """
     _____ _         _____             _____
    |_   _(_) ___   |_   _|_ _  ___   |_   _|__   ___
      | | | |/ __|____| |/ _` |/ __|____| |/ _ \\ / _ \\
      | | | | (_|_____| | (_| | (_|_____| | (_) |  __/
      |_| |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___|
    """

    BREAK = '————————————————————————————————————————————————————————————————'
    EMPTY_LINE = ''

    HOW_TO_PLAY = """
    1. The game is played on a grid that's 3 squares by 3 squares.
    2. You are «x», your friend is «o». Players take turns putting their marks in empty squares.
    3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
    4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

    More info: https://en.wikipedia.org/wiki/Tic-tac-toe
    """

    BOARD_TEMPLATE = """
     {one} | {two} | {three}
    ———+———+———
     {four} | {five} | {six}
    ———+———+———
     {seven} | {eight} | {nine}
    """

    BOARD_KEYWORDS = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

    BOARD_POSITIONS_TO_KEYWORDS = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }

    BOARD_POSITIONS_TO_PLACEHOLDERS = {
        1: '¹',
        2: '²',
        3: '³',
        4: '⁴',
        5: '⁵',
        6: '⁶',
        7: '⁷',
        8: '⁸',
        9: '⁹',
    }

    def __init__(self, board: Board) -> None:
        """
        Construct the object.

        Arguments:
            board (Board): a game's board.
        """
        self.board = board

    def show_current_board(self) -> None:
        """
        Show current board.
        """
        board = self.board.get()

        template_arguments = {}

        for computer_position, cell in enumerate(board):
            human_position = computer_position + 1

            placeholder = Ui.BOARD_POSITIONS_TO_PLACEHOLDERS[human_position]
            template_keyword = Ui.BOARD_POSITIONS_TO_KEYWORDS[human_position]

            if cell is self.board.EMPTY_CELL:
                template_arguments[template_keyword] = self._colorize_placeholder(placeholder=placeholder)

            else:
                template_arguments[template_keyword] = cell.value

        board_as_string = Ui.BOARD_TEMPLATE.format(**template_arguments)
        print(board_as_string)

    def show_break(self) -> None:
        """
        Show a break line.
        """
        print(self.BREAK)

    def show_empty_line(self) -> None:
        """
        Show an empty line.
        """
        print(self.EMPTY_LINE)

    def show_title(self) -> None:
        """
        Show a title of the game.
        """
        print(self.TITLE)
        self.show_break()

    def show_how_to_play(self) -> None:
        """
        Show how to play the game.
        """
        print(self.HOW_TO_PLAY)
        self.show_break()

    def show_tie_result(self) -> None:
        """
        Show a game's tie result.
        """
        print('The game has ended. The result of the game is tie.')
        self.show_empty_line()

    def show_win_result(self, player: Player) -> None:
        """
        Show a game's win result.

        Arguments:
            player (Player): a game's player.
        """
        print(f'The game has ended. The result of the game is a win by player {player.mark.value}.')
        self.show_empty_line()

    def show_position_is_invalid(self) -> None:
        """
        Show position is invalid message.
        """
        print('Position the player enters is not valid. It should be one of the numbers you see on the board.')
        self.show_empty_line()

    def _colorize_placeholder(self, placeholder: str) -> str:
        """
        Colorize a placeholder.

        It makes the placeholder of a color slightly seeing thing (gray-ish) just enough to not get much attention.

        Arguments:
            placeholder (str): a board template's placeholder.

        Returns:
            The colorized placeholder as a string.
        """
        return f'\033[90m{placeholder}\033[0m'
