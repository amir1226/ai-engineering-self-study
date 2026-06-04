def build_graph(edges):
    # Undirected, so each edge is added in BOTH directions.
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    return graph


def undirected_path(graph, src, dst, visited=None):
    if visited is None:
        visited = set()
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbor in graph[src]:
        if undirected_path(graph, neighbor, dst, visited):
            return True
    return False


if __name__ == "__main__":
    # Undirected graph given as an edge list:
    #   i — j
    #   k — i
    #   m — k
    #   k — l
    #   o — n
    edges = [
        ["i", "j"],
        ["k", "i"],
        ["m", "k"],
        ["k", "l"],
        ["o", "n"],
    ]

    graph = build_graph(edges)

    print(undirected_path(graph, "j", "m"))  # True   (j — i — k — m)
    print(undirected_path(graph, "j", "o"))  # False  (o/n are a separate component)

