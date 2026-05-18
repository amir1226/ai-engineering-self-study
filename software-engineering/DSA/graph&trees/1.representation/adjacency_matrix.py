# n= number of vertices
# m= number of edges

class Graph:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        # Space complexity: O(n^2) for the adjacency matrix
        self.adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    def populate(self, edges):
        for u,v in edges:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
    
    def __str__(self) -> str:
        return "\n".join([" ".join(map(str,row)) for row in self.adj_matrix])
            
if __name__ == "__main__":
    n = 5
    m = 6
    edges = [(0,1),(0,2),(1,2),(1,3),(2,4),(3,4)]
    graph = Graph(n,m)
    graph.populate(edges)
    print(graph)