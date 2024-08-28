from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, start, end):
        self.adjacency_list[start].append(end)

    def bfs(self, start, end):
        if start == end:
            return True

        visited = set()
        queue = deque([start])

        while queue:
            current_node = queue.popleft()

            if current_node == end:
                return True

            visited.add(current_node)

            for neighbor in self.adjacency_list[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return False

    def dfs(self, start, end):
        if start == end:
            return True

        visited = set()

        def dfs_recursive(node):
            if node == end:
                return True
            visited.add(node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    if dfs_recursive(neighbor):
                        return True
            return False

        return dfs_recursive(start)

graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')
graph.add_edge('E', 'F')
graph.add_edge('A', 'G')

start_node = 'A'
end_node = 'E'

print("BFS:", graph.bfs(start_node, end_node))  # Output: True

print("DFS:", graph.dfs(start_node, end_node))  # Output: True
