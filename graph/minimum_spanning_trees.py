import heapq


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(nodes, edges):
    edges.sort()
    uf = UnionFind(nodes)
    mst = []
    mst_weight = 0

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight

    return mst_weight, mst

print("Kruskal's algorithm")
num_nodes = 5
edge_list = [
    (1, 0, 1),  # (weight, node1, node2)
    (3, 0, 2),
    (2, 1, 2),
    (4, 1, 3),
    (5, 2, 3),
    (6, 3, 4),
]

total_weight, mst_edges = kruskal(num_nodes, edge_list)
print("Total weight of MST:", total_weight)
print("Edges in MST:", mst_edges)


print("\nPrim's algorithm")

def prims_algorithm(num_nodes, edges):
    min_heap = [(0, 0, -1)]
    visited = [False] * num_nodes
    mst_edges = []
    mst_weight = 0

    while min_heap and len(mst_edges) < num_nodes - 1:
        weight, current, parent = heapq.heappop(min_heap)
        if visited[current]:
            continue
        visited[current] = True
        mst_weight += weight

        if parent != -1:
            mst_edges.append((parent, current, weight))

        for neighbor, neighbor_weight in edges[current]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (neighbor_weight, neighbor, current))

    if len(mst_edges) != num_nodes - 1:
        raise ValueError("Graph is not connected; MST cannot be formed.")

    return mst_weight, mst_edges



num_nodes = 5
adjacency_list = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (2, 2), (3, 4)],
    2: [(0, 3), (1, 2), (3, 5)],
    3: [(1, 4), (2, 5), (4, 6)],
    4: [(3, 6)],
}

total_weight, mst_edges = prims_algorithm(num_nodes, adjacency_list)
print("Total weight of MST:", total_weight)
print("Edges in MST:", mst_edges)
