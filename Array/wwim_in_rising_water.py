from typing import List
import math

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 这道题刚开始的时候没有想到用binary search来做
        # 后来是收到solution启发才想到可以用binary search的方法来做。
        n = len(grid)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(min_time, r, c) -> bool:
            if r == n - 1 and c == n - 1:
                return True
            
            res = False
            for n_dir in dirs:
                n_r, n_c = r + n_dir[0], c + n_dir[1]
                if 0 <= n_r < n and 0 <= n_c < n and (n_r, n_c) not in seen and grid[n_r][n_c] <= min_time:
                    seen.add((n_r, n_c))
                    res = res or dfs(min_time, n_r, n_c)
            
            return res
                    
        
        left, right = grid[0][0], n*n
        
        while left < right:
            mid = left + (right - left) // 2
            # 这里要注意每一次要reset 这个seen。因为每一次都是从头开始dfs
            seen = set((0,0))
            if not dfs(mid, 0, 0):
                left = mid + 1
            else:
                right = mid
        
        return left