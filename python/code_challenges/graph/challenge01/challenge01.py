from collections import deque

class Node:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)


class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex
    
    def add_edge(self, node1, node2, weight=0):
        if node1 not in self.adj_list or node2 not in self.adj_list:
            return "A node does not exist"
        
        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)

    def bfs_traversal(self, start_value):
        start_node = None

        # Find the start node
        for node in self.adj_list:
            if node.value == start_value:
                start_node = node
                break
        
        if not start_node:
            return "Start node not found in the graph"
        
        visited = set()
        queue = deque([start_node])
        traversal = []

        while queue:
            current_node = queue.popleft()

            if current_node in visited:
                continue
            
            visited.add(current_node)
            traversal.append(current_node.value)

            for edge in self.adj_list[current_node]:
                if edge.vertex not in visited:
                    queue.append(edge.vertex)

        return traversal

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex} ({edge.weight}) ------> ' 
            output += '\n'
        return output 


