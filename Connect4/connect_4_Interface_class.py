import os
from connect_4_exceptions import (
    WrongBoardDimensionsValueError,
    FullColumnError,
    ColumnOutOfRangeError,
    NoIntColumnError,
    WrongSaveGameFileError,
    WrongBestScoresFileError,
    EmptyBestScoresFileError
    )
from connect_4_Board_class import Board
from connect_4_Bot_class import Bot
from connect_4_Game_class import Game
from connect_4_io import (
    save_game,
    load_game,
    save_score_player,
    save_score_bot,
    load_scores
)


class Interface:
    def main_game_interface(self):
        accepted_no = ['No', 'no', 'n', 'N', 'NO']
        accepted_yes = ['Yes', 'yes', 'y', 'Y', 'YES']

        print('Welcome to Connect 4 Game!')

        print('Would you like to start a new game?')
        start_condition = input('(Y/n) or ("h" to see high scores):\t')
        while start_condition in ('h', 'H'):
            self.show_scores()
            print('Would you like to start a new game?')
            start_condition = input('(Y/n) or ("h" to see high scores):\t')
        if start_condition in accepted_no:
            self.play_saved_game()
            return

        print('Would you like to change dimensions of the board?')
        board_mess = '(y/N):\t'
        changing_board_value = input(board_mess)
        if changing_board_value in accepted_yes:
            board = self.main_board_create()
        else:
            board = Board()

        game = Game(board)
        self.game = game

        print('Would you like to play with bot?')
        bot_message = '(Y/n):\t'
        bot_value = input(bot_message)
        if bot_value in accepted_no:
            tour = self.play_with_player(1)
            if not tour:
                return
            else:
                self.save_final_score(False, tour)
        else:
            tour = self.play_with_bot(1)
            if not tour:
                return
            else:
                self.save_final_score(True, tour)

    def save_final_score(self, bot, tour):
        accepted_yes = ['Yes', 'yes', 'y', 'Y', 'YES']
        save_score_messsage = 'Would you like to save your score? (y/N):'
        save_score_condition = input(save_score_messsage)
        if save_score_condition in accepted_yes:
            name = input('Enter your name:\t')
            if bot:
                save_score_bot(name, tour)
            else:
                save_score_player(name, tour)
            print('Your score has been saved')
        return

    def main_board_create(self):
        correct_values = False
        while not correct_values:
            try:
                height = int(input('Enter height of a board (from 4 to 9):'))
                width = int(input('Enter width of a board (from 4 to 9):'))
                board = Board(height, width)
                correct_values = True
            except WrongBoardDimensionsValueError:
                print(WrongBoardDimensionsValueError())
            except ValueError:
                print('The height and width values must be an integer.')
        print('New board has been created!')
        return board

    def play_with_player(self, tour):
        print('To save a game enter "s"!')
        game = self.game
        while not (game.check_victory_player1() or game.check_victory_player2()):
            os.system('clear')
            save_condition = self.player_move(1)
            if save_condition == 'save':
                save_game(game, False, tour)
                print('The Game has been saved.')
                return
            elif game.check_victory_player1():
                self.print_gameboard()
                print(f'Congratulations First Player has won in {tour} tours')
                return tour
            elif game.board().full_board():
                print('There is no winner!')
                return

            save_condition = self.player_move(2)
            if save_condition == 'save':
                save_game(game, False, tour, 1)
                print('The Game has been saved.')
                return
            elif game.check_victory_player2():
                self.print_gameboard()
                print(f'Congratulations Second Player has won in {tour} tours')
                return tour
            elif game.board().full_board():
                print('There is no winner!')
                return

            tour += 1

    def player_move(self, player_number):
        game = self.game
        space_in_column_condition = False
        self.print_gameboard()
        print(f'Player {player_number} turn:')
        while not space_in_column_condition:
            try:
                column = input('Which column do you choose?:')
                if (column == 'save') or (column == 's'):
                    return 'save'
                column = int(column)
                if player_number == 1:
                    game.throw_token_player1(column)
                elif player_number == 2:
                    game.throw_token_player2(column)
                space_in_column_condition = True
            except FullColumnError:
                print(FullColumnError())
            except ColumnOutOfRangeError:
                print(ColumnOutOfRangeError())
            except ValueError:
                print(NoIntColumnError())

    def play_with_bot(self, tour):
        game = self.game
        bot = Bot(game)
        print('To save a game enter "s"!')
        while not (game.check_victory_player1() or game.check_victory_player2()):
            os.system('clear')
            save_condition = self.player_move(1)
            if save_condition == 'save':
                save_game(game, True, tour)
                print('The Game has been saved.')
                return
            elif game.check_victory_player1():
                self.print_gameboard()
                print(f'Congratulations First Player has won in {tour} tours')
                return tour
            elif game.board().full_board():
                self.print_gameboard()
                print('There is no winner!')
                return

            column = bot.find_best_column()
            game.throw_token_player2(column)
            print(f'Bot has chosen {column} column')
            if game.check_victory_player2():
                self.print_gameboard()
                print(f'Bot has won in {tour} tours')
                return
            elif game.board().full_board():
                self.print_gameboard()
                print('There is no winner!')
                return
            tour += 1

    def play_saved_game(self):
        try:
            data = load_game()
        except WrongSaveGameFileError:
            print(WrongSaveGameFileError())
            return
        (gameboard, bot, last_player, tour) = data
        height = len(gameboard)
        width = len(gameboard[0])
        board = Board(height, width)
        board.set_gameboard(gameboard)
        game = Game(board)
        self.game = game
        if bot:
            self.play_with_bot(tour)
        else:
            self.play_saved_game_player(tour, last_player)

    def play_saved_game_player(self, tour, last_player):
        if last_player == 2:
            self.play_with_player(tour)
        elif last_player == 1:
            self.player_move(2)
            if self.game.board().full_board():
                print('There is no winner!')
                return
            print('')
            tour += 1
            self.play_with_player(tour)

    def print_gameboard(self):
        last_row = []
        for row in self.game.board().gameboard():
            print(row)
        print('')
        for column in range(self.game.board().width()):
            last_row.append(column + 1)
        print(last_row)

    def show_scores(self):
        try:
            scores = load_scores()
            for index, score in enumerate(scores):
                number = index + 1
                name, tour, bot = score
                if bot:
                    print(f'{number}.{name} won in {tour} moves against bot.')
                else:
                    print(f'{number}.{name} won in {tour} moves against other player.')
        except WrongBestScoresFileError:
            print(WrongBestScoresFileError())
        except EmptyBestScoresFileError:
            print(EmptyBestScoresFileError())
