from copy import deepcopy
from connect_4_exceptions import FullColumnError


class Bot:
    def __init__(self, Game):
        self._game = Game

    def game(self):
        return self._game

    def create_temp_game(self):
        temp_game = deepcopy(self.game())
        return temp_game

    def find_best_column(self):
        final_score_list = self.final_score_list()
        max_score = max(final_score_list)
        max_score_index = final_score_list.index(max_score)
        best_column = max_score_index + 1
        return best_column

    def final_score_list(self):
        column_score_list = self.column_score_list()
        row_score_list = self.row_score_list()
        diag_score_list = self.diag_score_list()
        final_score_list = []
        for column in range(self.game().board().width()):
            column_score = column_score_list[column]
            row_score = row_score_list[column]
            diag_score = diag_score_list[column]
            score = column_score + row_score + diag_score
            final_score_list.append(score)
        return final_score_list

    def column_score_list(self):
        column_score_list = self.temp_score_list('column')
        return column_score_list

    def row_score_list(self):
        row_score_list = self.temp_score_list('row')
        return row_score_list

    def diag_score_list(self):
        diag_score_list = self.temp_score_list('diag')
        return diag_score_list

    def temp_score_list(self, counted_element):
        temp_score_list = []
        for column in range(1, self.game().board().width() + 1):
            temp_game = self.create_temp_game()
            score = 0
            try:
                temp_game.throw_token_player2(column)
            except FullColumnError:
                temp_score_list.append(-10)
                continue
            if counted_element == 'column':
                str_of_sth_list = temp_game.str_of_column()
            elif counted_element == 'row':
                str_of_sth_list = temp_game.str_of_row()
            elif counted_element == 'diag':
                str_of_sth_list = temp_game.str_of_diag()
            for str_of_sth in str_of_sth_list:
                if '2222' in str_of_sth:
                    score += 1000000
                if '222' in str_of_sth:
                    score += 1000
                if '22' in str_of_sth:
                    score += 100
                if '2' in str_of_sth:
                    score += 1
                if '2111' in str_of_sth:
                    score += 10000
                if '1112' in str_of_sth:
                    score += 10000
                if '1211' in str_of_sth:
                    score += 10000
                if '1121' in str_of_sth:
                    score += 10000
                if '211' in str_of_sth:
                    score += 100
                if '112' in str_of_sth:
                    score += 100
            temp_score_list.append(score)
        return temp_score_list
