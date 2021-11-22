import copy
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(cur, res, n, k, start):
            if len(cur) == k:
                res.append(copy.deepcopy(cur))
            
            for i in range(start, n + 1):
                cur.append(i)
                dfs(cur, res, n, k, i + 1)
                cur.pop()

        res = []
        cur = []
        
        dfs(cur, res, n, k, 1)
        return res
        
        
        
    #                     []
    #         [1]                         [2]                      [3]        [4]
    # [1,2]       [1,3]  [1,4]           [2, 3]   [2, 4]          [3,4]       