def has_path(graph, src, dst, visited=None):
    if visited is None:
        visited = set()
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited):
            return True
    return False


if __name__ == "__main__":
    # Directed graph (adjacency list as a dict):
    #   f → g, i
    #   g → h
    #   h → (none)
    #   i → g, k
    #   j → i
    #   k → (none)
    graph = {
        "f": ["g", "i"],
        "g": ["h"],
        "h": [],
        "i": ["g", "k"],
        "j": ["i"],
        "k": [],
    }

    print(has_path(graph, "f", "k"))  # True   (f → i → k)
    print(has_path(graph, "f", "j"))  # False  (nothing points back to j)