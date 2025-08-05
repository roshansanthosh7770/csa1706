import itertools

def tsp(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_cost = float('inf')
    best_path = []
    for perm in itertools.permutations(nodes):
        path = [start] + list(perm) + [start]
        cost = sum(graph[path[i]][path[i+1]] for i in range(len(path) - 1))
        if cost < min_cost:
            min_cost = cost
            best_path = path
    return best_path, min_cost

graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

start_node = input("Enter start node (A/B/C/D): ").strip().upper()
path, cost = tsp(graph, start_node)
print("Optimal Path:", " → ".join(path))
print("Minimum Cost:", cost)
