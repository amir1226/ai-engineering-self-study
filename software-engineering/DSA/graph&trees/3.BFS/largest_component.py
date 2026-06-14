def build_graph(edges):
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    return graph

def largest_component(graph):
    visited = set()
    count = 0
    for node in graph:
        if node not in visited:
            new_count = traverse(graph, node, visited)
            if new_count > count:
                count = new_count
    return count
            
def traverse(graph, node, visited: set):
    from collections import deque
    queue = deque([node])
    visited.add(node)
    count = 0
    while queue:
        current = queue.popleft()
        count +=1
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return count

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
    
    count = largest_component(graph)
    print(count)


