from collections import deque

def bfs(capacity, flow, source, sink, parent):
    n = len(capacity)
    visited = [False] * n
    queue = deque([source])
    visited[source] = True

    while queue:
        current = queue.popleft()
        for neighbor in range(n):
            if not visited[neighbor] and capacity[current][neighbor] - flow[current][neighbor] > 0:
                queue.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = current
                if neighbor == sink:
                    return True
    return False

# Edmonds-Karp implementation
def edmonds_karp(capacity, source, sink):
    n = len(capacity)
    flow = [[0] * n for _ in range(n)]
    parent = [-1] * n
    max_flow = 0

    while bfs(capacity, flow, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow

if __name__ == "__main__":
    capacity = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    source = 0
    sink = 5

    max_flow = edmonds_karp(capacity, source, sink)
    print("The maximum possible flow is:", max_flow)
