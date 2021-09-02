# bfs vs dfs: traversal order is different
# Different from BFS, the nodes you visit earlier might not be the nodes which are closer to the root node. As a result, the first path you found in DFS might not be the shortest path.


# Return true if there is a path from cur to target.
# solution one: recursion
def dfs(cur: Node, target: Node, visited: set) -> bool:
    if cur is target:
        return True
    for neighbor in cur.neighbors:
        if neighbor not in visited:
            visited.add(neighbor)
            return dfs(neighbor, target, visited)
    return False


# solution two: stack
def dfs(root: Node, target: Node) -> bool:
    visited = set()
    visited.add(root)
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur is target:
            return True
        for neighbor in cur.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return False