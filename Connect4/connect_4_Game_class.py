import numpy
from connect_4_exceptions import (
    FullColumnError,
    ColumnOutOfRangeError,
    NoIntColumnError
)


class Game:
    def __init__(self, Board):
        self._board = Board

    def board(self):
        return self._board

    def throw_token(self, column, player_symbol):
        if not (type(column) == int):
            raise NoIntColumnError
        elif not (1 <= column <= self.board().width()):
            raise ColumnOutOfRangeError
        gameboard = self.board().gameboard()
        possible_row_number = []
        for row_number in range(len(gameboard)):
            if gameboard[row_number][column - 1] == 0:
                possible_row_number.append(row_number)
            if len(possible_row_number) == 0:
                raise FullColumnError
            lowest_row = max(possible_row_number)
        gameboard[lowest_row][column - 1] = player_symbol
        self.board().set_gameboard(gameboard)

    def throw_token_player1(self, column):
        self.throw_token(column, 1)

    def throw_token_player2(self, column):
        self.throw_token(column, 2)

    def check_victory(self, player_symbol):
        victory_str = f'{player_symbol}' * 4
        for str_of_row in self.str_of_row():
            if victory_str in str_of_row:
                return True
        for str_of_column in self.str_of_column():
            if victory_str in str_of_column:
                return True
        for str_of_diag in self.str_of_diag():
            if victory_str in str_of_diag:
                return True
        return False

    def str_of_row(self):
        gameboard = self.board().gameboard()
        str_of_row_list = []
        for row in gameboard:
            str_of_row = ''.join(str(token) for token in row)
            str_of_row_list.append(str_of_row)
        return str_of_row_list

    def str_of_column(self):
        gameboard = self.board().gameboard()
        str_of_column_list = []
        for column in range(self.board().width()):
            str_of_column = ''
            for row in gameboard:
                token = str(row[column])
                str_of_column += token
            str_of_column_list.append(str_of_column)
        return str_of_column_list

    def str_of_diag(self):
        gameboard = self.board().gameboard().copy()
        height = self.board().height()
        gameboard = numpy.array(gameboard)
        diag_num = range(-height+1, height)
        diag_list1 = [numpy.diag(gameboard, num).tolist() for num in diag_num]
        gameboard = numpy.flipud(gameboard)
        diag_list2 = [numpy.diag(gameboard, num).tolist() for num in diag_num]
        alldiags = diag_list1 + diag_list2
        str_of_diag_list = []
        for diag in alldiags:
            if len(diag) < 4:
                continue
            str_of_diag = ''.join(str(token) for token in diag)
            str_of_diag_list.append(str_of_diag)
        return str_of_diag_list

    def check_victory_player1(self):
        return self.check_victory(1)

    def check_victory_player2(self):
        return self.check_victory(2)
