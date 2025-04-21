# The MineSweeper game
# Author: Jayden Krish Nair

def initialise_board():

    board = ["O"] * 25
    return board



def display_board(board):

    for i in range(25):
        if board[i] == "X":
            print("O", end=" ")
        else:
            print(board[i], end=" ")
        if (i + 1) % 5 == 0:
            print()



def insert_mines(board, positions):

    for [row, col] in positions:
        index = row * 5 + col
        board[index] = "X"



def count_adjacent_mines(board, r_count, c_count):

    count = 0

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i, j in directions:

        neighbour_row = r_count + i

        neighbour_col = c_count + j

        if 0 <= neighbour_row < 5 and 0 <= neighbour_col < 5:

            index = neighbour_row * 5 + neighbour_col

            if board[index] == "X":
                count += 1
    return count



def play_turn(board, r, c):

    index = r * 5 + c
    if board[index] == "X":
        board[index] = "#"
        return board, True
    else:
        count = count_adjacent_mines(board, r, c)
        if count == 0:
            board[index] = " "
        else:
            board[index] = str(count)
        return board, False







def check_win(board):

    for i in range(len(board)):
        if board[i] == "O":
            return False
    return True





def play_game(mine_locations):
    
    board = initialise_board()
    insert_mines(board, mine_locations)
    display_board(board)
    while True:
        current_move = input("Please enter a row and column (e.g '1 1'): ")
        row_col_list = current_move.split()

        row = int(row_col_list[0])
        col = int(row_col_list[1])

        board, mine_triggered = play_turn(board, row, col)

        display_board(board)

        if mine_triggered == True:
            print("Game over")
            break

        elif check_win(board) == True:
            print("You win!")
            break
