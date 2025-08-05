import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], 0, start, [start]))
    closed_set = set()
    while open_list:
        est_total, cost, node, path = heapq.heappop(open_list)
        if node == goal:
            return path, cost
        if node in closed_set:
            continue
        closed_set.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in closed_set:
                new_cost = cost + weight
                est = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (est, new_cost, neighbor, path + [neighbor]))
    return None, float('inf')

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 5)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 6,
    'G': 0
}

start = input("Enter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()
path, cost = a_star(graph, start, goal, heuristic)
print("Path:", " → ".join(path))
print("Total Cost:", cost)
