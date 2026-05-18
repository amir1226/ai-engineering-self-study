# n= number of vertices
# m= number of edges
"""
For a weighted graph, we can use the same adjacency matrix representation,
but instead of using 1 to indicate the presence of an edge,
we can store the weight of the edge.
"""

class Graph:
    def __init__(self, n):
        self.n = n
        # Space complexity: O(n + m) for the adjacency list
        self.adj_list = [[] for _ in range(n)]
        
    def populate(self, edges):
        self.m = len(edges)
        for u,v, w in edges:
            self.adj_list[u].append((v,w))
            self.adj_list[v].append((u,w))

    def __str__(self) -> str:
        return "\n".join([f"{i}: {neighbors}" for i, neighbors in enumerate(self.adj_list)])
    
if __name__ == "__main__":
    n = 5
    edges = [(0,1,10),(0,2,20),(1,2,30),(1,3,40),(2,4,50),(3,4,60)]
    graph = Graph(n)
    graph.populate(edges)
    print(graph)