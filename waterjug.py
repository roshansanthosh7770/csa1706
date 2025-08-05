from collections import deque

A = 4
B = 3
target = 2
visited = set()

def is_goal(state):
    return state[0] == target or state[1] == target

def bfs():
    queue = deque()
    queue.append((0, 0, []))

    while queue:
        a, b, path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if is_goal((a, b)):
            return path

        next_states = [
            (A, b),
            (a, B),
            (0, b),
            (a, 0),
            (min(a + b, A), b - (min(a + b, A) - a)),
            (a - (min(a + b, B) - b), min(a + b, B))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return None

solution = bfs()

if solution:
    for step in solution:
        print(f"Jug A: {step[0]}L, Jug B: {step[1]}L")
else:
    print("No solution found.")
