import math

player = 'X'
opponent = 'O'

def is_moves_left(board):
    for row in board:
        if '_' in row:
            return True
    return False

def evaluate(board):
    for row in board:
        if row.count(player) == 3:
            return 10
        if row.count(opponent) == 3:
            return -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == player:
                return 10
            if board[0][col] == opponent:
                return -10
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == player:
            return 10
        if board[0][0] == opponent:
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == player:
            return 10
        if board[0][2] == opponent:
            return -10
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = '_'
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = '_'
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                move_val = minimax(board, 0, False)
                board[i][j] = '_'
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

board = [
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['_', '_', '_']
]

move = find_best_move(board)
print(f"Best move: Row {move[0]}, Column {move[1]}")
