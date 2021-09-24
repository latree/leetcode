from typing import List
import math

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[math.inf for i in range(n)] for j in range(m)]
        
        res = math.inf
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        # 刚开始是按照recursion的base case 写的，所以开始的时候i是倒着递减的
        for i in range(1,m):
            for j in range(n):
                min_next = math.inf
                # 每一层有三个move (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
                for k in (-1, 0, 1):
                    nj = j + k
                    # 但是出边界的要忽略掉
                    if 0 <= nj < n:
                        min_next = min(dp[i - 1][nj], min_next)
                # 三个上一层的最小值 加上当前的值和dp[i][j] 比较
                dp[i][j] = min(dp[i][j], min_next + matrix[i][j])
                
        # dp的最后一行就是base case
        return min(dp[m-1])
                
                