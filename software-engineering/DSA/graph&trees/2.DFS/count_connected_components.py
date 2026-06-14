def build_graph(edges):
    # Undirected, so each edge is added in BOTH directions.
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    return graph

def count_connected_components(graph):
    visited = set()
    count = 0
    for node in graph:
        if node not in visited:
            traverse(graph, node, visited)
            count += 1
    return count
            
def traverse(graph, node, visited: set):
    if node in visited:
        return
    visited.add(node)
    for neighbour in graph[node]:
        traverse(graph, neighbour, visited)
        

if __name__ == "__main__":
    # Undirected graph given as an edge list:
    #   1 — 2          (component 1)
    #   3              (component 2, isolated)
    #   4 — 6 — 5      (component 3)
    #       6 — 8
    #       6 — 7
    edges = [
        [1, 2],
        [4, 6],
        [5, 6],
        [6, 8],
        [6, 7],
    ]
    graph = build_graph(edges)
    graph.setdefault(3, [])  # Node 3 is isolated — add it explicitly
    
    count = count_connected_components(graph)
    print(count)


