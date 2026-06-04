from collections import deque

def has_path_queue(graph, src, dst):
    visited = set()
    queue = deque()
    queue.append(src)
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

    print(has_path_queue(graph, "f", "k"))  # True   (f → i → k)
    print(has_path_queue(graph, "f", "j"))  # False  (nothing points back to j)