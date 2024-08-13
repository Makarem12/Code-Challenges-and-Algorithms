class Graph:
    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs_util(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self._dfs_util(i, visited)

    def _get_transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def is_strongly_connected(self):
        visited = [False] * self.V

        # Step 1: Do a DFS from the first vertex
        self._dfs_util(0, visited)

        # If any vertex is not visited, then the graph is not strongly connected
        if any(not v for v in visited):
            return "Not strongly connected"

        # Step 2: Transpose the graph
        gr = self._get_transpose()

        # Step 3: Do a DFS for the transposed graph starting from the first vertex
        visited = [False] * self.V
        gr._dfs_util(0, visited)

        # If all vertices are visited in the second DFS, then the graph is strongly connected
        if any(not v for v in visited):
            return "Not strongly connected"

        return "Strongly connected"

