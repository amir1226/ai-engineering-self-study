# Breadth-First Search (BFS)

BFS explores a graph **level by level**: it visits all neighbours of a node before moving on to their neighbours. Complexity is **O(V + E)** (every vertex and every edge visited once).

This folder has one implementation:

| File | Approach |
|------|----------|
| `BFS_algorithm.py` | Iterative, using a `deque` as a FIFO queue |

## Why a queue (FIFO)?

BFS uses a **queue**: `popleft()` returns the **first** item enqueued (First-In-First-Out). That ordering is exactly what produces the level-by-level exploration.

This is the one structural difference from DFS:

| | Data structure | Behaviour |
|---|---|---|
| **DFS** | stack (LIFO, `pop()`) | go as deep as possible first |
| **BFS** | queue (FIFO, `popleft()`) | explore level by level |

The rest of the skeleton (mark visited, loop over neighbours) is identical. `collections.deque` is used instead of a plain list because `popleft()` on a list is O(n), while on a deque it's O(1).

## `visited` strategy: mark-on-enqueue

The node is marked `visited` the moment it is added to the queue:

```python
for node in graph[current]:
    if not visited[node]:
        q.append(node)
        visited[node] = True   # mark as soon as it's enqueued
```

This guarantees each node enters the queue **at most once**, so no `if visited[current]: continue` guard is needed after `popleft()`.