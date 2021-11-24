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


# matrix 遍历 recursion
# 如何用recursion 来遍历嵌套for loop。比如遍历matrix
for i in range(m):
    for j in range(n):
        print(f"{i}, {j}")

# 用recursion写出来就是这样的：
def dfs(matrix, r, c, m, n):
    
    if c == n:
        return dfs(matrix, r + 1, 0, m, n)
    if r == m:
        return True
    
    print(matrix[r][c])
    if dfs(matrix, r, c + 1, m, n):
        return True
