from connect_4_exceptions import WrongBoardDimensionsValueError


class Board:
    def __init__(self, height=6, width=7):
        self.set_height(height)
        self.set_width(width)
        self._gameboard = self.create_gameboard()

    def height(self):
        return self._height

    def width(self):
        return self._width

    def gameboard(self):
        return self._gameboard

    def set_height(self, new_height):
        if not (4 <= new_height <= 9):
            raise WrongBoardDimensionsValueError
        self._height = new_height

    def set_width(self, new_width):
        if not (4 <= new_width <= 9):
            raise WrongBoardDimensionsValueError
        self._width = new_width

    def set_gameboard(self, new_gameboard):
        self._gameboard = new_gameboard

    def create_gameboard(self):
        board = []
        for row in range(self.height()):
            board.append([])
            for column in range(self.width()):
                board[row].append(0)
        return board

    def full_board(self):
        first_row = self.gameboard()[0]
        if (0 in first_row):
            return False
        return True
