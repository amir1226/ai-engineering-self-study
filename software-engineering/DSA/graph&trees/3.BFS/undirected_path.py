from collections import deque


def build_graph(edges):
    # Edge list -> adjacency list (dict).
    # Undirected, so each edge is added in BOTH directions.
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    return graph


def undirected_path(graph, src, dst):
    visited = set()
    queue = deque([src])
    visited.add(src)
    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
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
