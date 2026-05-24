# Depth-First Search (DFS)

def dfs_algorithm(graph,current_node=0,visited=None):
    if visited is None:
        visited=[False]*len(graph)
    if visited[current_node]:
        return
    print(current_node)
    visited[current_node] = True

    neighbours = graph[current_node]

    for neighbour in neighbours:
        dfs_algorithm(graph,current_node=neighbour,visited=visited)


if __name__ == "__main__":
    # Adjacency list:
    #   0 — 1, 9
    #   1 — 0, 8
    #   2 — 3
    #   3 — 2, 4, 5, 7
    #   4 — 3
    #   5 — 3, 6
    #   6 — 5, 7
    #   7 — 3, 6, 8, 10, 11
    #   8 — 1, 3, 7, 9
    #   9 — 0, 8
    #  10 — 7, 11
    #  11 — 7, 10
    N = 12

    edges = [
        (0, 1),
        (0, 9),
        (1, 8),
        (9, 8),
        (8, 7),
        (8, 3),
        (3, 2),
        (3, 4),
        (3, 5),
        (3, 7),
        (5, 6),
        (6, 7),
        (7, 10),
        (7, 11),
        (10, 11),
    ]

    # Build adjacency list
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    dfs_algorithm(adj)