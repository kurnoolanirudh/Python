class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self):
        return f"Edge({self.src}, {self.dest}, {self.weight})"

    def __str__(self):
        return f"Edge => source = {self.src} , destination = {self.dest} , weight = {self.weight}"


class Graph:
    def __init__(self, directed=True):
        self.edges = dict()
        self.num_nodes = 0
        self.directed = directed
    def __repr__(self):
        return "Graph()"

    def __str__(self):
        return f"Graph => Number Of Nodes = {self.num_nodes} ; Number Of Edges = {len(self.edges)}"

    def insert_node(self, new_node):
        if new_node in self.edges:
            raise Exception(f"node - {new_node} already present in the graph")
        self.edges[new_node] = []
        self.num_nodes += 1

    def delete_node(self, node):
        if node not in self.edges:
            raise Exception(f"node - {node} not present in the graph")
        del self.edges[node]
        for _ , edges in self.edges.items():
            for i in range(len(edges)):
                if edges[i].dest == node:
                    del edges[i]

        self.num_nodes -= 1

    def insert_edge(self, src, dest, weight=None):
        if src not in self.edges:
            raise Exception(f"node - {src} not present in the graph")

        if dest not in self.edges:
            raise Exception(f"node - {dest} not present in the graph")

        self.edges[src].append(Edge(src, dest, weight))
        if not self.directed:
            self.edges[dest].append(Edge(dest, src, weight))

    def delete_edge(self, src, dest):
        if src not in self.edges:
            raise Exception(f"node - {src} not present in the graph")

        if dest not in self.edges:
            raise Exception(f"node - {dest} not present in the graph")

        for i in range(len(self.edges[src])):
            if self.edges[i].dest == dest:
                del self.edges[i]

        if not self.directed:
            for i in range(len(self.edges[dest])):
                if self.edges[i].src == src:
                    del self.edges[i]
                

    def dfs(self, start, rec=False):
        if rec:
            return Graph._dfs_rec(self, start)
        else:
            return Graph._dfs_it(self, start)

    def bfs(self, start, rec=False):
        if rec:
            return Graph._bfs_rec(self, start)
        else:
            return Graph._bfs_it(self, start)

    # what's the problem with default mutable arguments ???
    @staticmethod
    def _dfs_it(graph, start, visited=None):
        stack = [start]
        if not visited:
            visited = set()
        trav = []
        while len(stack) != 0:
            curr = stack.pop()
            visited.add(curr)
            trav.append(curr)
            for edge in graph.edges[curr]:
                if edge.dest not in visited:
                    stack.append(edge.dest)

        for node in graph.edges:
            if node not in visited:
                trav += Graph._dfs_it(graph, node ,visited)

        return trav
    
    @staticmethod
    def _dfs_rec(graph, start, stack=None, visited=None, trav=None):
        if visited == None:
            visited = set()
        if trav == None:
            trav = []
        if stack == None:
            stack = [start]

        if len(stack) == 0:
            return trav

        while len(stack) != 0:
            curr = stack.pop()
            visited.add(curr)
            trav.append(curr)
            for edge in graph.edges[curr]:
                if edge.dest not in visited:
                    stack.append(edge.dest)

        return Graph._dfs_rec(graph, start, stack, visited, trav)

    @staticmethod
    def _bfs_it(graph, start, visited=None):
        q = [start]
        if not visited:
            visited = set()
        trav = []
        while len(q) != 0:
            curr = q.pop(0)
            visited.add(curr)
            trav.append(curr)
            for edge in graph.edges[curr]:
                if edge.dest not in visited:
                    q.append(edge.dest)

        for node in graph.edges:
            if node not in visited:
                trav += Graph._dfs_it(graph, node ,visited)

        return trav
    

    @staticmethod
    def _bfs_rec(graph, start, q=None, visited=None, trav=None):
        if visited == None:
            visited = set()
        if trav == None:
            trav = []
        if q == None:
            q = [start]

        if len(q) == 0:
            return trav

        while len(q) != 0:
            curr = q.pop(0)
            visited.add(curr)
            trav.append(curr)
            for edge in graph.edges[curr]:
                if edge.dest not in visited:
                    q.append(edge.dest)

        return Graph._bfs_rec(graph, start, q, visited, trav)
    
    @staticmethod
    def _dfs_cycle_detection_directed(graph):
        def _dfs(node, parent):
            pass 
        pass

    @staticmethod
    def _dfs_cycle_detection_undirected(graph):
        pass 





def main():
    print("Hello, World")

    g = Graph()
    g.insert_node(1)
    g.insert_node(2)
    g.insert_node(3)
    g.insert_node(4)

    g.insert_edge(1, 2)
    g.insert_edge(1, 4)
    g.insert_edge(2, 3)
    g.insert_edge(3, 1)

    print(repr(g))
    print(str(g))

    print(g.dfs(1))
    print(g.dfs(1, rec=True))
    print(g.bfs(1))
    print(g.bfs(1, rec=True))

if __name__ == "__main__":
    main()


