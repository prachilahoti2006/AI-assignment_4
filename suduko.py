sudoku = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def display_board(board):
    for row in board:
        for value in row:
            print(value, end=" ")
        print()

def empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def valid_number(board, row, col, number):
    for i in range(9):
        if board[row][i] == number:
            return False

        if board[i][col] == number:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == number:
                return False

    return True

def sudoku_solver(board):
    cell = empty_cell(board)

    if cell is None:
        return True

    row, col = cell

    for number in range(1, 10):
        if valid_number(board, row, col, number):
            board[row][col] = number

            if sudoku_solver(board):
                return True

            board[row][col] = 0

    return False

print("Input Sudoku:\n")
display_board(sudoku)

if sudoku_solver(sudoku):
    print("\nSolved Sudoku:\n")
    display_board(sudoku)
else:
    print("No solution exists")
