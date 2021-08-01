from functools import total_ordering
from typing import List

class largestIsland:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # # solution 1: dfs
        # # Time: O(N**4)
        # # Space: O(N**2)
        # def helper(row: int, col:int, seen) -> int:
        #     if grid[row][col] == 0:
        #         return len(seen)
        #     for (next_row, next_col) in ((row + 1, col), (row - 1, col),(row, col + 1),(row, col - 1)):
        #         if  0 <= next_row < len(grid) and \
        #         0 <= next_col < len(grid[0]) and \
        #         (next_row, next_col) not in seen and \
        #         grid[next_row][next_col]:

        #             seen.add((next_row, next_col))
        #             helper(next_row, next_col, seen)
        #     return len(seen)

        # res = 0
        # n = len(grid)
        # has_zero = False
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 0:
        #             has_zero = True
        #             grid[i][j] = 1
        #             res = max(res, helper(i, j, seen={(i, j)}))
        #             grid[i][j] = 0
                
        # return res if has_zero else n * n

        # solution 2: dfs with map
        # Time:O(2*(n**2)) which is O(n**2)
        # Space:O(n**2)
        # 这道题的主题思路：
        # 先把整个grid里面的岛划分成不同的groupid，同时再生成一个groupid: total_element 一个hashmap
        # 有了这个map 在iterate 所有的0 的位置去把能够相邻的岛的total_element 都加起来 取一个最大值

        # 有很多的小trick在这个题里
        # 1. neighbors function的用法之前没有见到过
        # 2. max(area.values() or [0]) 

        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r + 1, c),(r - 1, c),(r, c + 1),(r, c - 1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc
        
        def dfs(r: int, c: int, idx: int) -> int:
            res = 1
            grid[r][c] = idx
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    res += dfs(nr, nc, idx)
            return res

        area = {}
        idx = 2

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[idx] = dfs(r, c, idx)
                    idx += 1
        
        res = max(area.values() or [0])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    res = max(res, 1 + sum(area[i] for i in seen))
        return res

    def call_function(self) -> None:
        self.largestIsland([[1, 0],[0,1]])