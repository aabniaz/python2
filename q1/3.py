#sudoku ???
"""def is_valid_sudoku(board):
    def is_valid(arr):
        arr = [cell for cell in arr if cell != '.']
        return len(arr) == len(set(arr))

    # Check rows
    for i in range(9):
        if not is_valid(board[i]):
            return False

    # Check columns
    for j in range(9):
        if not is_valid([board[i][j] for i in range(9)]):
            return False

    # Check 3x3 blocks
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid(block):
                return False

    return True

# Example usage
sudoku = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(is_valid_sudoku(sudoku))  # Output: True
"""