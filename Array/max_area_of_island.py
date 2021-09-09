from typing import List

class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        seen = set()
        res = 0
        
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n and (r, c) not in seen and grid[r][c]):
                return 0
        
            seen.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)
    
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res = max(dfs(r, c), res)
        return res

        