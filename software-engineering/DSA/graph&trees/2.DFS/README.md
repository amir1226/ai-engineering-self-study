# Depth-First Search (DFS)

DFS explores a graph by going **as deep as possible along one branch before backtracking**. Complexity is **O(V + E)** (every vertex and every edge visited once).

This folder has two equivalent implementations:

| File | Approach |
|------|----------|
| `DFS_algorithm.py` | Recursive (uses the language call stack) |
| `DFS_algorithm_stack.py` | Iterative (uses an explicit `stack` list) |

## Recursive vs. iterative

Both are valid DFS and share the same skeleton. The recursive version relies on the **call stack** (each call pushes a frame); the iterative version moves that stack into an explicit list you control.

- **Same complexity:** O(V + E) for both.
- **Recursive:** cleaner to read, but can hit Python's recursion limit (~1000) and raise `RecursionError` on very deep graphs.
- **Iterative:** more verbose, no artificial depth limit (uses the heap).

## `visited` strategy: mark-on-push vs. mark-on-pop

There are two correct ways to track visited nodes in the iterative version:

### mark-on-pop (mirrors recursion exactly)

Mark `visited` right after `pop()`, with a guard at the top of the loop:

```python
current = stack.pop()
if visited[current]:      # skip nodes already processed
    continue
visited[current] = True
```

A node can sit in the stack multiple times, but the guard prevents duplicate processing. **Guaranteed to reproduce the recursive DFS order in every graph.** Slightly more memory.

### mark-on-push (used in `DFS_algorithm_stack.py`)

Mark `visited` the moment you push, so each node enters the stack **at most once**:

```python
for node in reversed(graph[current]):
    if not visited[node]:
        stack.append(node)
        visited[node] = True
```

Lower memory, no duplicates, and correct as a traversal (every reachable node visited exactly once). **Tradeoff:** for DFS specifically, mark-on-push does **not** always reproduce the exact visit order of the recursive version.


## Summary

| | mark-on-pop | mark-on-push |
|---|---|---|
| Correct traversal? | ✅ | ✅ |
| Same order as recursion? | ✅ always | ⚠️ not always |
| Memory | a bit more | less (each node pushed once) |
