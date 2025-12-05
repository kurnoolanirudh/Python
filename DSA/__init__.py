from typing import TypeVar, Generic
from typing_extensions import override

T = TypeVar("T")


class Edge(Generic[T]):
    def __init__(self, src: T, dest: T, weight: float | None):
        self.src: T = src
        self.dest: T = dest
        self.weight: float | None = weight

    @override
    def __repr__(self) -> str:
        return f"Edge({self.src}, {self.dest}, {self.weight})"

    @override
    def __str__(self) -> str:
        return f"Edge => source = {self.src} , destination = {self.dest} , weight = {self.weight}"


class Graph(Generic[T]):
    def __init__(self):
        self.edges: dict[T, list[T]] = dict()
        self.num_nodes: int = 0

    @override
    def __repr__(self) -> str:
        return "Graph()"

    @override
    def __str__(self) -> str:
        return f"Graph => Number Of Nodes = {self.num_nodes} ; Number Of Edges = {len(self.edges)}"

    def insert_node(self, new_node: T):
        if new_node in self.edges:
            raise Exception(f"node - {new_node} already present in the graph")
        self.edges[new_node] = []
        self.num_nodes += 1

    def delete_node(self, node: T):
        if node not in self.edges:
            raise Exception(f"node - {node} not present in the graph")
        del self.edges[node]
        for _, edges in self.edges.items():
            for i in range(len(edges)):
                if edges[i].dest == node:
                    del edges[i]

        self.num_nodes -= 1

    def insert_edge(self, src: T, dest: T, weight: float | None = None):
        if src not in self.edges:
            raise Exception(f"node - {src} not present in the graph")

        if dest not in self.edges:
            raise Exception(f"node - {dest} not present in the graph")

        self.edges[src].append(Edge(src, dest, weight))

    def delete_edge(self, src, dest, weight):
        if src not in self.edges:
            raise Exception(f"node - {src} not present in the graph")

        if dest not in self.edges:
            raise Exception(f"node - {dest} not present in the graph")

        for i in range(len(self.edges)):
            if self.edges[i].dest == dest and self.edges[i].weight == weight:
                del self.edges[i]
                return

    def dfs(self, start, rec=False):
        if rec:
            pass
        else:
            return Graph._dfs_it(self, start)

    def bfs(self, rec=False):
        if rec:
            pass
        else:
            pass

    # what's the problem with default mutable arguments ???
    @staticmethod
    def _dfs_it(graph, start, visited=None):
        stack = [start]
        if not visited:
            visited = set()
        trav = []
        while len(stack) != 0:
            print(stack)
            curr = stack.pop()
            visited.add(curr)
            print(visited)
            trav.append(curr)
            print(trav)
            for edge in graph.edges[curr]:
                if edge.dest not in visited:
                    stack.append(edge.dest)

        for node in graph.edges:
            if node not in visited:
                trav += Graph._dfs_it(graph, node, visited)

        return trav


def main():
    print("Hello, World")

    g = Graph()
    g.insert_node(1)
    g.insert_node(2)
    g.insert_node(3)

    g.insert_edge(1, 2)
    g.insert_edge(2, 3)
    g.insert_edge(3, 1)

    print(repr(g))
    print(str(g))

    print(g.dfs(1))


if __name__ == "__main__":
    main()
