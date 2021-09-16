from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        moves = [(1, 0),(0, 1),(-1, 0),(0, -1)]
        # 刚开始还想每一次循环都要init一个新的dp，这个想法是错误的
        # dp[r][c]代表在rc这个位置的最长个数，它不会随着循环而改变的
        dp = [[0 for i in range(n)] for j in range(m)]

        def dfs(r: int, c: int) -> int:
            if dp[r][c] != 0:
                return dp[r][c]     
            
            for move in moves:
                nr, nc = r + move[0], c + move[1]
                
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    dp[r][c] = max(dfs(nr, nc), dp[r][c])
            # 之前错误的 直接return dp[r][c] + 1
            # 这样的话并没有在dp[r][c] 里加上1， 会导致运算结果出错
            dp[r][c] += 1
            return dp[r][c]
        
        if not m:
            return 0
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res