N = 8  # Size of the board (8x8)

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True

def solve(board, row):
    if row == N:
        print_solution(board)
        return True

    result = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = True
            result = solve(board, row + 1) or result
            board[row][col] = False  # Backtrack
    return result

# Initialize board with False (no queens)
board = [[False] * N for _ in range(N)]

# Solve the problem
solve(board, 0)
