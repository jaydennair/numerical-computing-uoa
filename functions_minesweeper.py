# The MineSweeper game
# Author: Jayden Krish Nair

def initialise_board():
    """
       function 1 - initialises a 1D board containing 25 'O' characters

       arguments:
       None

       returns:
       board - a 1D list of 25 'O' characters representing the minesweeper board

       """
    board = ["O"] * 25
    return board



def display_board(board):
    """
        function 2 - this function will display the 1D board as a 2D 5x5 array of 'O' characters
        it will also ensure that the bombs marked as X will be hidden (displayed as zeros)

        arguments:
        board -  a 1D list of 25 'O' characters representing the minesweeper board

        returns:
        None

        """
    for i in range(25):
        if board[i] == "X":
            print("O", end=" ")
        else:
            print(board[i], end=" ")
        if (i + 1) % 5 == 0:
            print()



def insert_mines(board, positions):
    """
        function 3 - this function will insert the mines into the appropriate positions
        based on the formula the bombs will be assigned to board[index]

        arguments:
        board - a 1D list of 25 'O' characters representing the minesweeper board
        positions: a list of lists containing each mine location

        returns:
        None

        """
    for [row, col] in positions:
        index = row * 5 + col
        board[index] = "X"



def count_adjacent_mines(board, r_count, c_count):
    """
        function 4 - this function will count the mines adjacent
        to the selected square

        arguments:
        board -  a 1D list of 25 'O' characters representing the minesweeper board
        r_count - an int representing the row (0-4) of the square being checked for adjacent mines
        c_count - an int representing the col (0-4) of the square being checked for adjacent mines

        returns:
        count - an int representing the number (0-8) of adjacent mines

        """
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
    """
        function 5 - this function implements the game logic
        by determining the outcome if the square selected is a mine, empty square, etc

        arguments:
        board -  a 1D list of 25 'O' characters representing the minesweeper board
        r - an int representing the row (0-4) of the position being selected
        c - an int representing the col (0-4) of the position being selected

        returns:
        board - a list representing the updated board
        mine_triggered - a boolean value that is True if the square selected is a mine and False otherwise

        """
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
    """
        function 6 - the function will check if the player has won by
        checking if there are any unselected empty safe squares remaining

        arguments:
        board -  a 1D list of 25 'O' characters representing the minesweeper board

        returns:
        win - a boolean value that is True if the player has won the game and False otherwise

        """
    for i in range(len(board)):
        if board[i] == "O":
            return False
    return True





def play_game(mine_locations):
    """
        function 7 - the function will play a round of the minesweeper game
        from start to finish

        arguments:
        mine_locations - a list of lists indicating the positions the mines will be placed on the board

        returns:
        None

        """
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
