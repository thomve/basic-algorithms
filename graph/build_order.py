class Graph:
    def __init__(self):
        self.__nodes = []
        self.__map = {}

    def get_or_create_node(self, name: str):
        if name not in self.__map:
            node = Node(name)
            self.__nodes.append(node)
            self.__map[name] = node
        return self.__map[name]
    
    def add_edge(self, start_name: str, end_name: str):
        start = self.get_or_create_node(start_name)
        end = self.get_or_create_node(end_name)
        start.add_neighbor(end)
    
    def get_nodes(self):
        return self.__nodes
    
class Node:
    def __init__(self, name: str):
        self.name = name
        self.__children = []
        self.__map = {}
        self.__dependencies = 0

    def add_neighbor(self, node):
        if node.name not in self.__map:
            self.__children.append(node)
            self.__map[node.name] = node
            node.increment_dependencies()
    
    def increment_dependencies(self):
        self.__dependencies += 1
    
    def decrement_dependencies(self):
        self.__dependencies -= 1
    
    def get_name(self):
        return self.name

    def get_children(self):
        return self.__children
    
    def get_number_dependencies(self):
        return self.__dependencies
    
def find_build_order(dependencies):
    graph = build_graph(dependencies)
    return order_nodes(graph.get_nodes())

def build_graph(dependencies):
    graph = Graph()
    for dependency in dependencies:
        first = dependency[0]
        second = dependency[1]
        graph.add_edge(first, second)
    return graph

def order_nodes(nodes):
    order = [None] * len(nodes)
    end_of_list = add_non_dependent(order, nodes, 0)
    to_be_processed = 0
    while to_be_processed < len(order):
        current = order[to_be_processed]
        if current == None:
            return None
        children = current.get_children()
        for child in children:
            child.decrement_dependencies()
        end_of_list = add_non_dependent(order, children, end_of_list)
        to_be_processed += 1
    return order

def add_non_dependent(order, nodes, offset):
    for node in nodes:
        if node.get_number_dependencies() == 0:
            order[offset] = node
            offset += 1
    return offset


dependencies = [('A', 'D'), ('F', 'B'), ('B', 'D'), ('F', 'A'), ('D', 'C')]

build_order = find_build_order(dependencies)

for node in build_order:
    print(node.name)
# should output: ['F', 'A', 'B', 'D', 'C']
# ['F', 'B', 'A', 'D', 'C'] is also a valid output