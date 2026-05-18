# n= number of vertices
# m= number of edges
"""
For a weighted graph, we can use the same adjacency matrix representation, 
but instead of using 1 to indicate the presence of an edge, 
we can store the weight of the edge.
If there is no edge between two vertices,
we can use a special value (like 0 or None) to indicate that.
"""
class Graph:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        # Space complexity: O(n^2) for the adjacency matrix
        self.adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    def populate(self, edges):
        for u,v,w in edges:
            self.adj_matrix[u][v] = w
            self.adj_matrix[v][u] = w
    
    def __str__(self) -> str:
        return "\n".join([" ".join(map(str,row)) for row in self.adj_matrix])
            
if __name__ == "__main__":
    n = 5
    m = 6
    edges = [(0,1,10),(0,2,20),(1,2,30),(1,3,40),(2,4,50),(3,4,60)]
    graph = Graph(n,m)
    graph.populate(edges)
    print(graph)