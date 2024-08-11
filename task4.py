def is_valid(board, row, col, num):
    # Check if the number is not repeated in the current row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is not repeated in the current column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is not repeated in the current 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # No empty cells left, puzzle solved

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Undo the current cell value and backtrack

    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # Empty cell is represented by 0
                return (i, j)
    return None

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(board[i][j], end=" ")
        print()

# Example Sudoku puzzle to solve
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Original Sudoku board:")
print_board(board)

if solve_sudoku(board):
    print("\nSolved Sudoku board:")
    print_board(board)
else:
    print("No solution exists for the given Sudoku puzzle.")
