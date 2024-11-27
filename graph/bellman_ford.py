class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, src):
        distance = [float('inf')] * self.V
        distance[src] = 0

        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

        for u, v, weight in self.edges:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                print("Graph contains a negative-weight cycle")
                return None

        return distance


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    source = 0
    distances = g.bellman_ford(source)

    if distances is not None:
        print(f"Shortest distances from vertex {source}:")
        for i in range(len(distances)):
            print(f"Vertex {i}: {distances[i]}")
