from connect_4_Game_class import Game
from connect_4_Board_class import Board
from connect_4_exceptions import (
    FullColumnError,
    ColumnOutOfRangeError,
    NoIntColumnError
)
import pytest


def test_class_game_constructor():
    board = Board()
    game = Game(board)
    assert game.board() == board


def test_game_throw_token_player1():
    board = Board(4, 4)
    row = [0, 0, 0, 0]
    game = Game(board)
    game.throw_token_player1(1)
    assert board.gameboard() == [row, row, row, [1, 0, 0, 0]]


def test_game_throw_token_stack():
    board = Board(4, 4)
    row = [0, 0, 0, 0]
    last_row = [1, 0, 0, 0]
    game = Game(board)
    game.throw_token_player1(1)
    game.throw_token_player2(1)
    assert board.gameboard() == [row, row, [2, 0, 0, 0], last_row]


def test_game_check_victory_row():
    board = Board()
    game = Game(board)
    game.throw_token_player1(2)
    game.throw_token_player1(3)
    game.throw_token_player1(4)
    game.throw_token_player1(5)
    assert game.check_victory_player1()


def test_game_check_victory_column():
    board = Board()
    game = Game(board)
    game.throw_token_player1(3)
    game.throw_token_player1(3)
    game.throw_token_player1(3)
    game.throw_token_player1(3)
    assert game.check_victory_player1()


def test_game_check_victory_diagonal():
    board = Board(4, 4)
    game = Game(board)
    gameboard = [[0, 0, 0, 1], [0, 0, 1, 2], [0, 1, 2, 2], [1, 2, 2, 2]]
    board.set_gameboard(gameboard)
    assert game.check_victory_player1()


def test_game_check_victory_no_winner():
    board = Board()
    game = Game(board)
    assert not game.check_victory_player1()
    assert not game.check_victory_player2()


def test_game_throw_token_NoIntColumn():
    game = Game(Board())
    with pytest.raises(NoIntColumnError):
        game.throw_token_player2('a')
        game.throw_token_player1(5.5)


def test_game_throw_token_FullColumn():
    board = Board(4, 4)
    gameboard = [[1, 2, 1, 0], [1, 2, 1, 2], [1, 2, 1, 2], [2, 1, 2, 1]]
    board.set_gameboard(gameboard)
    game = Game(board)
    with pytest.raises(FullColumnError):
        game.throw_token_player1(1)
        game.throw_token_player2(2)
        game.throw_token_player2(3)


def test_game_throw_token_ColumnOutOfRange():
    game = Game(Board())
    with pytest.raises(ColumnOutOfRangeError):
        game.throw_token_player2(10)
        game.throw_token_player1(-1)
        game.throw_token_player1(0)
