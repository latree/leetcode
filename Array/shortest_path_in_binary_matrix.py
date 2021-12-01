from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        moves = [[-1, -1], [-1, 0],[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        queue.append((0, 0))
        steps = 1
        visited = set()
        visited.add((0, 0))
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                
                if node[0] == m - 1 and node[1] == n - 1:
                    return steps
                for move in moves:
                    r = node[0] + move[0]
                    c = node[1] + move[1]
                    if 0 <= r < m and 0 <= c < n and grid[r][c] != 1 and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))
            steps += 1
        return -1