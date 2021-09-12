import copy

class Solution:
    def knightDialer(self, n: int) -> int:
        directions = [(2, 1), (1, 2), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        r, c = 4, 3
        dp = [[1 for i in range(c)] for j in range(r)]
        # ***** 特别注意！！ List 想要copy 必须要deep copy，要不然就是shadow copy
        dp_next = copy.deepcopy(dp)
        forbid = ([3, 0], [3, 2])
        
        for a in range(n - 1):
            dp, dp_next = dp_next, dp
            
            for i in range(r):
                for j in range(c):
                    if [i, j] in forbid:
                        continue
                    cur_jumps = 0
                    for direction in directions:
                        tmp_i, tmp_j = i + direction[0], j + direction[1]
                        if  0 <= tmp_i < r and 0 <= tmp_j < c and [tmp_i, tmp_j] not in forbid:
                            cur_jumps += dp[tmp_i][tmp_j]

                    dp_next[i][j] = cur_jumps
        
        res = sum([sum(i) for i in dp_next]) - 2
        res = res % (10**9 + 7)
        return res