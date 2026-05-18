# n= number of vertices
# m= number of edges

class Graph:
    def __init__(self, n):
        self.n = n
        # Space complexity: O(n + m) for the adjacency list
        self.adj_list = [[] for _ in range(n)]
        
    def populate(self, edges):
        self.m = len(edges)
        for u,v in edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def __str__(self) -> str:
        return "\n".join([f"{i}: {neighbors}" for i, neighbors in enumerate(self.adj_list)])
    
if __name__ == "__main__":
    n = 5
    edges = [(0,1),(0,2),(1,2),(1,3),(2,4),(3,4)]
    graph = Graph(n)
    graph.populate(edges)
    print(graph)