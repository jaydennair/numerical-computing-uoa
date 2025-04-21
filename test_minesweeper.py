import pytest
from functions_minesweeper import *

def test_count_adjacent_mines_in_corner():
    board = [
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'X', 'O', 'O',
        'O', 'X', 'O', 'X', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O'
    ]
    count = count_adjacent_mines(board, 2, 2)
    assert (count == 3)



def test_insert_mines():

        board = initialise_board()
        positions = [[1, 2], [3, 2]]
        insert_mines(board, positions)

        assert board[1 * 5 + 2 ] == "X"
        assert board[3 * 5 + 2] == "X"

def test_safe_play_turn():
    board = initialise_board()
    r = 2
    c = 3
    board, mine_triggered = play_turn(board, r, c)
    assert mine_triggered == False


def test_unsafe_play_turn():
    board = initialise_board()
    positions = [[3, 1], [1, 0]]
    insert_mines(board, positions)
    r = 3
    c = 1
    board, mine_triggered = play_turn(board, r, c)
    assert mine_triggered == True



def test_False_check_win():
    board = initialise_board()
    assert check_win(board) == False

def test_True_check_win():
        board = initialise_board()
        positions = [[1, 4], [2, 3]]
        insert_mines(board, positions)
        for i in range(len(board)):
            row = i // 5
            col = i % 5
            if [row,col] not in positions:
                board[i] = " "
        assert check_win(board) == True






