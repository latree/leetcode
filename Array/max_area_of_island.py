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

        
        # 第二遍心得：
        # moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        # m = len(grid)
        # n = len(grid[0])
        # visited = set()

        # *************** note ***************
        # # 开始的时候还用了flag，然后把visited当成每进入一个island 重置一个新的visited， 其实不用，
        # # 1，这些岛都是不连起来的（如果连起来的也不叫岛了）
        # # 每一个岛的node 都只能遍历一遍，所以有一个global的visited 就可以了
        
        # def dfs(grid: List[List[int]], r: int, c: int, visited: Set) -> int:
        #     if grid[r][c] == 0:
        #         return 0
                
        #     visited.add((r, c))
            
        #     area = 0
        #     for move in moves:
        #         n_r, n_c = r + move[0], c + move[1]
        #         if 0 <= n_r< m and 0 <= n_c < n and (n_r, n_c) not in visited:
        #             area += dfs(grid, n_r, n_c, visited)
        
        # *************** note ***************
        #     # 第二遍做的时候这里出错了：
        #     # 开始的时候写成： area += dfs(grid, n_r, n_c, visited) + 1
        #     # 每一个子node 都要加1，这是不对的，是加上所有的子node数量以后再加上当前的node 
        #     return area + 1
                    
        # res = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             cur_island_area = dfs(grid, i, j, visited)
        #             res = max(res, cur_island_area)
        
        # return res