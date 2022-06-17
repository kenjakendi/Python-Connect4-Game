from connect_4_Board_class import Board
from connect_4_exceptions import WrongBoardDimensionsValueError
import pytest


def test_board_constructor_base_parameters():
    board = Board()
    assert board.height() == 6
    assert board.width() == 7


def test_board_constructor_other_parameters():
    board = Board(5, 8)
    assert board.height() == 5
    assert board.width() == 8


def test_board_constructor_hight_less():
    with pytest.raises(WrongBoardDimensionsValueError):
        Board(3)


def test_board_constructor_width_less():
    with pytest.raises(WrongBoardDimensionsValueError):
        Board(5, 3)


def test_board_constructor_set_height():
    board = Board(6, 6)
    assert board.height() == 6
    board.set_height(8)
    assert board.height() == 8


def test_board_constructor_set_width():
    board = Board(6, 4)
    assert board.width() == 4
    board.set_width(8)
    assert board.width() == 8


def test_board_create_gameboard():
    board = Board(4, 4)
    row = [0, 0, 0, 0]
    result = [row, row, row, row]
    assert board.create_gameboard() == result


def test_board_gameboard():
    board = Board(4, 4)
    row = [0, 0, 0, 0]
    result = [row, row, row, row]
    assert board.gameboard() == result


def test_board_full_board():
    board = Board(4, 4)
    gameboard = [[1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 2, 2], [2, 2, 1, 1]]
    board.set_gameboard(gameboard)
    assert board.full_board()


def test_board_not_full_board():
    board = Board(4, 4)
    gameboard = [[1, 1, 2, 0], [1, 1, 2, 2], [1, 1, 2, 2], [2, 2, 1, 1]]
    board.set_gameboard(gameboard)
    assert not board.full_board()
