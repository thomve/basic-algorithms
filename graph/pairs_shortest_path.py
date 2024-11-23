
def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

if __name__ == "__main__":
    graph = [
        [0, 3, float('inf'), 5],
        [2, 0, float('inf'), 4],
        [float('inf'), 1, 0, float('inf')],
        [float('inf'), float('inf'), 2, 0]
    ]

    shortest_paths = floyd_warshall(graph)
    
    print("Shortest distance matrix:")
    for row in shortest_paths:
        print(row)
