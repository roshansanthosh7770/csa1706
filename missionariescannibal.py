from collections import deque

def is_valid(m1, c1, m2, c2):
    return (m1 == 0 or m1 >= c1) and (m2 == 0 or m2 >= c2)

def get_successors(state):
    m1, c1, m2, c2, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    successors = []
    for m, c in moves:
        if boat == 1:
            new_state = (m1 - m, c1 - c, m2 + m, c2 + c, 0)
        else:
            new_state = (m1 + m, c1 + c, m2 - m, c2 - c, 1)
        if 0 <= new_state[0] <= 3 and 0 <= new_state[1] <= 3 and \
           0 <= new_state[2] <= 3 and 0 <= new_state[3] <= 3 and \
           is_valid(new_state[0], new_state[1], new_state[2], new_state[3]):
            successors.append(new_state)
    return successors

def bfs():
    start = (3, 3, 0, 0, 1)
    goal = (0, 0, 3, 3, 0)
    visited = set()
    queue = deque()
    queue.append((start, [start]))
    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        if state == goal:
            return path
        for successor in get_successors(state):
            queue.append((successor, path + [successor]))
    return None

path = bfs()
if path:
    for step in path:
        print(step)
else:
    print("No solution found.")
