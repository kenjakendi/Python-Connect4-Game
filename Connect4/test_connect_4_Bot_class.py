from connect_4_Bot_class import Bot
from connect_4_Board_class import Board
from connect_4_Game_class import Game


def test_bot_constructor():
    game = Game(Board())
    bot = Bot(game)
    assert bot.game() == game


def test_bot_temp_game():
    game = Game(Board())
    bot = Bot(game)
    temp_game = bot.create_temp_game()
    temp_game.throw_token_player1(1)
    assert game.board().gameboard() != temp_game.board().gameboard()


def test_bot_find_best_column_columnwin():
    game = Game(Board(4, 4))
    bot = Bot(game)
    gameboard = [[0, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0]]
    game.board().set_gameboard(gameboard)
    assert bot.find_best_column() == 1


def test_bot_find_best_column_row_win():
    game = Game(Board(4, 4))
    bot = Bot(game)
    gameboard = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 2, 0]]
    game.board().set_gameboard(gameboard)
    assert bot.find_best_column() == 4


def test_bot_find_best_column_diag_win():
    game = Game(Board(4, 4))
    bot = Bot(game)
    gameboard = [[0, 0, 0, 0], [0, 0, 2, 1], [0, 2, 1, 1], [2, 1, 1, 1]]
    game.board().set_gameboard(gameboard)
    assert bot.find_best_column() == 4


def test_bot_find_best_column_block():
    game = Game(Board(4, 4))
    bot = Bot(game)
    gameboard = [[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 2, 2], [1, 2, 2, 2]]
    game.board().set_gameboard(gameboard)
    assert bot.find_best_column() == 4


def test_bot_find_best_column_last_empty():
    board = Board(4, 4)
    game = Game(board)
    bot = Bot(game)
    gameboard = [[1, 2, 1, 0], [1, 2, 1, 2], [1, 2, 1, 2], [2, 1, 2, 1]]
    board.set_gameboard(gameboard)
    assert bot.find_best_column() == 4
