import itertools

def tsp_dynamic_programming(distance_matrix):
    n = len(distance_matrix)
    memo = {}

    for i in range(n):
        memo[(1 << i, i)] = (0, -1)

    for subset_size in range(2, n + 1):
        for subset in itertools.combinations(range(n), subset_size):
            subset_mask = sum(1 << bit for bit in subset)
            for j in subset:
                if subset_size == 1 or not (subset_mask & (1 << j)):
                    continue
                prev_subset_mask = subset_mask & ~(1 << j)
                min_cost = float('inf')
                parent = -1
                for k in subset:
                    if k == j or not (prev_subset_mask & (1 << k)):
                        continue
                    cost = memo[(prev_subset_mask, k)][0] + distance_matrix[k][j]
                    if cost < min_cost:
                        min_cost = cost
                        parent = k
                memo[(subset_mask, j)] = (min_cost, parent)

    min_cost = float('inf')
    parent = -1
    subset_mask = (1 << n) - 1
    for j in range(n):
        cost = memo[(subset_mask, j)][0] + distance_matrix[j][0]
        if cost < min_cost:
            min_cost = cost
            parent = j

    path = []
    current_mask = subset_mask
    last_node = parent
    while last_node != -1:
        path.append(last_node)
        _, last_node = memo[(current_mask, last_node)]
        current_mask &= ~(1 << path[-1])
    path.reverse()
    
    return path, min_cost

distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

optimal_path, min_distance = tsp_dynamic_programming(distance_matrix)
print("Optimal path:", optimal_path)
print("Minimum distance:", min_distance)
