from collections import deque

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def print_board(state):
    for row in state:
        print(row)
    print()

def get_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def copy_state(state):
    return [row[:] for row in state]

def is_goal(state):
    return state == goal_state

def bfs(start):
    visited = set()
    queue = deque()
    queue.append((start, []))  # (state, path)

    while queue:
        state, path = queue.popleft()
        state_str = str(state)

        if state_str in visited:
            continue
        visited.add(state_str)

        if is_goal(state):
            return path

        x, y = get_blank(state)

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = copy_state(state)
                # Swap blank with adjacent
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                move = (new_state[x][y], dx, dy)
                queue.append((new_state, path + [new_state]))

    return None

start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = bfs(start_state)

if solution:
    print("Steps to solve:")
    for step in solution:
        print_board(step)
else:
    print("No solution found.")
