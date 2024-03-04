from collections import deque

def bfs(graph, start):
    """
    breadth first search
    
    Suitable for finding the shortest path in an unweighted graph, 
    testing if a graph is bipartite, and solving puzzles like 
    the shortest path in a maze.
    """
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(adjacent for adjacent in graph[node] if adjacent not in visited)


def dfs(graph, start, visited=None):
    """
    depth first search

    Suitable for topological sorting, cycle detection in a graph, 
    finding connected components in an undirected graph, 
    and solving puzzles like the 8-puzzle problem.

    """
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

start_node = 'A'

print("BFS Traversal:")
bfs(graph, start_node)

print("DFS Traversal:")
dfs(graph, start_node)


def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]

directed_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("Topological sort\n", topological_sort(directed_graph))
